"""Powerpoint transitions implements in VapourSynth."""
import enum
import functools
import os
import sys
from typing import Callable, Optional

import vapoursynth as vs

sys.path.insert(0, os.path.abspath('.'))
core = vs.core


class Direction(enum.Enum):
    """Direction enumeration, usually meaning *from* what direction the second clip enters."""
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()


def _check_clips(frames: int, caller: Callable, *clips: vs.VideoNode) -> None:
    """General checker for clip formats, resolutions, length."""
    same_check = set()
    for clip in clips:
        if clip.format is None:
            raise ValueError(f"{caller.__name__}: all clips must be constant-format")
        if 0 in (clip.width, clip.height):
            raise ValueError(f"{caller.__name__}: all clips must be constant-resolution")
        if clip.num_frames < frames:
            raise ValueError(f"{caller.__name__}: all clips must have at least {frames} frames")
        same_check.add((clip.format.id, clip.width, clip.height))
    if len(same_check) > 1:
        raise ValueError(f"{caller.__name__}: all clips must be same format and resolution")


def _return_combo(clip1: Optional[vs.VideoNode], clip_middle: vs.VideoNode, clip2: Optional[vs.VideoNode]) -> vs.VideoNode:
    """
    Prevents splicing empty clips.

    :param clip1:        optional start clip
    :param clip_middle:  mandatory middle clip
    :param clip2:        optional ending clip
    :return: splice of existing clips in order
    """
    if clip1 is not None and clip2 is not None:
        return clip1 + clip_middle + clip2
    elif clip1 is not None and clip2 is None:
        return clip1 + clip_middle
    elif clip1 is None and clip2 is not None:
        return clip_middle + clip2
    elif clip1 is None and clip2 is None:
        return clip_middle


def _transition_clips(clip1: vs.VideoNode, clip2: vs.VideoNode, frames: int):
    """Returns clean (non-transition) and transition sections of the given clips based on frames."""
    if clip1.num_frames == frames:
        clip1_t_zone = clip1
        clip1_clean = None
    else:
        clip1_t_zone = clip1[-frames:]
        clip1_clean = clip1[:-frames]

    if clip2.num_frames == frames:
        clip2_t_zone = clip2
        clip2_clean = None
    else:
        clip2_t_zone = clip2[:frames]
        clip2_clean = clip2[frames:]

    return clip1_clean, clip2_clean, clip1_t_zone, clip2_t_zone


def fade(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, /, use_frame_eval: bool = True) -> vs.VideoNode:
    """Cross-fade clips.
    First frame of the fade will be 100% clipa, while last frame will be 100% clipb
    As an example, say we have a 100 frame long black clip and 100 frame long white clip:

        >>> black = core.std.BlankClip(format=vs.GRAY8, color=[0], length=100)
        >>> white = core.std.BlankClip(format=vs.GRAY8, color=[255], length=100)

        >>> fade(black, white, 100)
        will result in a pure fade from black to white.
        The first frame (0) will be pure black, while the last frame (99) will be pure white.

        >>> fade(black, white, 20)
        will result in a 20-frame long fade from the end of the black clip through the beginning of the white clip.
        The first 80 frames (0-79) will be pure black.
        The first frame of the fade (80) will also be pure black. At this point, we've consumed 1 frame from the beginning of the white clip.
        The last frame of the fade (99) will be pure white. At this point, we've consumed 20 frames from the white clip.
        The last 80 frames (100-179) will be pure white.
    """
    _check_clips(frames, fade, clipa, clipb)

    clipa_clean, clipb_clean, clipa_fade_zone, clipb_fade_zone = _transition_clips(clipa, clipb, frames)

    def _fade(n: int):
        return core.std.Merge(clipa_fade_zone, clipb_fade_zone, weight=[n / (frames - 1)])

    if use_frame_eval:
        faded = core.std.FrameEval(clipa_fade_zone, _fade)
    else:
        faded = core.std.Splice([core.std.Merge(clipa_fade_zone, clipb_fade_zone, weight=[n / (frames - 1)])[n] for n in range(frames)])

    return _return_combo(clipa_clean, faded, clipb_clean)


def fade_to_black(src_clip: vs.VideoNode, frames: int, /, use_frame_eval: bool = True):
    """
    Simple convenience function to fade a clip to black. Frames will be the number of frames consumed from the end of the src_clip during the transition.
    The first frame of the transition will be 100% of the src_clip, while the last frame of the transition will be a pure black frame.

        >>> clip = core.ffms2.Source(r'/path/to/file.mp4')
        >>> fade_to_black(clip, 100)
        The last 100 frames of the clip will be fading to black, with the first frame of the transition being purely from the source,
        and the last frame of the transition being pure black, consuming 100 frames from the end of `clip`.
    """
    black_clip = core.std.BlankClip(format=vs.GRAY8, length=frames, color=[0])
    black_clip_resized = black_clip.resize.Point(
        width=src_clip.width,
        height=src_clip.height,
        format=black_clip.format.replace(
            color_family=src_clip.format.color_family,
            sample_type=src_clip.format.sample_type,
            bits_per_sample=src_clip.format.bits_per_sample,
            subsampling_w=src_clip.format.subsampling_w,
            subsampling_h=src_clip.format.subsampling_h
        ).id
    )
    return fade(src_clip, black_clip_resized, frames, use_frame_eval)


def push(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT, use_frame_eval: bool = True) -> vs.VideoNode:
    """
    Clipb pushes clipa off of the screen (coming from `direction`) during the transition.
    The first frame of the transition will be 100% of clipa, while the last frame of transition will be 100% of clipb.
    Consumes frames from the end of clipa and the start of clipb during the transition.

        >>> black = core.std.BlankClip(format=vs.GRAY8, color=[0], length=100)
        >>> white = core.std.BlankClip(format=vs.GRAY8, color=[255], length=100)

        >>> push(black, white, 100)
        The first frame (0) of the clip will be pure black, while the last frame (99) will be pure white.
        The white clip "pushes" the black clip to the left.

        >>> push(white, black, 20, Direction.UP)
        The first 80 frames (0-79) will be of the white clip.
        Frame 80, the start of the transition will be pure white.
        From frame 80-99 the black clip will push the white clip "up" off of the screen, consuming 20 frames from both clips.
        Frame 99, the end of the transition will be pure black.
        Frame 100-179 will be the remainder of the black clip.

    The parameter `use_frame_eval` exists to allow you to change a FrameEval call
    into a more complex (and probably slower) Trim/Splice series of calls.
    For normal use, leave this alone.
    But, as according to stux!, using FrameEval will cause 'Python to lock the GIL'.
    This has complications when running the vsscript multi-threaded:
    'If two threads want to each execute any FrameEval at the same time, one has to wait until the other is done.'
    """
    _check_clips(frames, push, clipa, clipb)

    clipa_clean, clipb_clean, clipa_push_zone, clipb_push_zone = _transition_clips(clipa, clipb, frames)

    if direction == Direction.LEFT:
        stack = core.std.StackHorizontal([clipa_push_zone, clipb_push_zone])
        w = stack.width // 2

        def _push(n: int):
            return stack.resize.Spline36(width=w, src_left=w * n / (frames - 1), src_width=w)

        if use_frame_eval:
            pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _push)
        else:
            pushed = core.std.Splice([stack.resize.Spline36(width=w, src_left=w * n / (frames-1), src_width=w)[n] for n in range(frames)])

    elif direction == Direction.RIGHT:
        stack = core.std.StackHorizontal([clipb_push_zone, clipa_push_zone])
        w = stack.width // 2

        def _push(n: int):
            return stack.resize.Spline36(width=w, src_left=w - (w * n / (frames - 1)), src_width=w)

        if use_frame_eval:
            pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _push)
        else:
            pushed = core.std.Splice([stack.resize.Spline36(width=w, src_left=w-(w * n / (frames - 1)), src_width=w)[n] for n in range(frames)])

    elif direction == Direction.UP:
        stack = core.std.StackVertical([clipa_push_zone, clipb_push_zone])
        h = stack.height // 2

        def _push(n: int):
            return stack.resize.Spline36(height=h, src_top=h * n / (frames-1), src_height=h)

        if use_frame_eval:
            pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _push)
        else:
            pushed = core.std.Splice([stack.resize.Spline36(height=h, src_top=h * n / (frames-1), src_height=h)[n] for n in range(frames)])

    elif direction == Direction.DOWN:
        stack = core.std.StackVertical([clipb_push_zone, clipa_push_zone])
        h = stack.height // 2

        def _push(n: int):
            return stack.resize.Spline36(height=h, src_top=h-(h * n / (frames-1)), src_height=h)

        if use_frame_eval:
            pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _push)
        else:
            pushed = core.std.Splice([stack.resize.Spline36(height=h, src_top=h-(h * n / (frames-1)), src_height=h)[n] for n in range(frames)])

    else:
        raise ValueError("push: give a proper direction")

    return _return_combo(clipa_clean, pushed, clipb_clean)


def wipe(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT, use_frame_eval: bool = True) -> vs.VideoNode:
    """
    A moving fade, kind of like a `fade` with a moving mask.
    The direction will be the direction the fade progresses towards.
    Uses a custom gradient as a mask (sRGB_gradient_1px_16-bit_dither.png)

        >>> black = core.std.BlankClip(format=vs.GRAY8, color=[0], length=100)
        >>> white = core.std.BlankClip(format=vs.GRAY8, color=[255], length=100)

        >>> wipe(black, white, 100)
        The first frame will be 100% black, the last frame will be 100% white.
        During the transition, the white clip gradually enters the screen from the left.
        However, unlike push, the clips DO NOT MOVE,
        the fade simply starts with the very right side of the white clip becoming visible.
        Over the duration of the fade,
        more of the white clip towards the left will fade over the black clip, until the transition is over.

        >>> wipe(white, black, 20, Direction.UP)
        The first 80 frames (0-79) will be pure white.
        Transition begins on frame 80, which is still 100% pure white.
        Gradually, over 20 frames (80-99), the black clip will become more visible starting from the bottom working up.
        The last frame of the transition (99) will be pure black.
        The transition will consume 20 frames from the end of the white clip, and the start of the black clip,
        resulting in a 80 + 20 + 80 = 180 frame long clip.
    """
    _check_clips(frames, wipe, clipa, clipb)

    clipa_clean, clipb_clean, clipa_wipe_zone, clipb_wipe_zone = _transition_clips(clipa, clipb, frames)

    mask = core.imwri.Read(r'./sRGB_gradient_1px_16-bit_dither.png')
    mask_horiz = mask.resize.Spline64(clipa.width, clipa.height, dither_type='error_diffusion',
                                format=mask.format.replace(bits_per_sample=clipa.format.bits_per_sample,
                                                           color_family=vs.GRAY).id)
    mask_vert = core.std.Transpose(mask).resize.Spline64(clipa.width, clipa.height, dither_type='error_diffusion',
                                format=mask.format.replace(bits_per_sample=clipa.format.bits_per_sample,
                                                           color_family=vs.GRAY).id)
    black_clip = core.std.BlankClip(mask_horiz, length=1, color=[0])
    white_clip = core.std.BlankClip(mask_horiz, length=1, color=[(1 << mask_horiz.format.bits_per_sample) - 1])

    if direction == Direction.LEFT:
        stack = core.std.StackHorizontal([black_clip, mask_horiz, white_clip])

        def _wipe(n: int):
            stack_ = stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width * n / (frames - 1), src_width=mask_horiz.width)
            return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        if use_frame_eval:
            wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _wipe)
        else:
            wiped = core.std.Splice([core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width * n / (frames - 1), src_width=mask_horiz.width))[n] for n in range(frames)])

    elif direction == Direction.RIGHT:
        stack = core.std.StackHorizontal([white_clip, core.std.FlipHorizontal(mask_horiz), black_clip])

        def _wipe(n: int):
            stack_ = stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width - (2 * mask_horiz.width * n / (frames - 1)), src_width=mask_horiz.width)
            return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        if use_frame_eval:
            wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _wipe)
        else:
            wiped = core.std.Splice([core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width - (2 * mask_horiz.width * n / (frames - 1)), src_width=mask_horiz.width))[n] for n in range(frames)])

    elif direction == Direction.UP:
        stack = core.std.StackVertical([black_clip, mask_vert, white_clip])

        def _wipe(n: int):
            stack_ = stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height * n / (frames - 1), src_height=mask_vert.height)
            return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        if use_frame_eval:
            wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _wipe)
        else:
            wiped = core.std.Splice([core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height * n / (frames - 1), src_height=mask_vert.height))[n] for n in range(frames)])

    elif direction == Direction.DOWN:
        stack = core.std.StackVertical([white_clip, core.std.FlipVertical(mask_vert), black_clip])

        def _wipe(n: int):
            stack_ = stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height - (2 * mask_vert.height * n / (frames - 1)), src_height=mask_vert.height)
            return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        if use_frame_eval:
            wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _wipe)
        else:
            wiped = core.std.Splice([core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height - (2 * mask_vert.height * n / (frames - 1)), src_height=mask_vert.height))[n] for n in range(frames)])

    else:
        raise ValueError("wipe: give a proper direction")

    return _return_combo(clipa_clean, wiped, clipb_clean)
