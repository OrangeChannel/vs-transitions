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


def fade(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int) -> vs.VideoNode:
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

    if clipa.num_frames == frames:
        clipa_fade_zone = clipa
        clipa_clean = None
    else:
        clipa_clean = clipa[:-frames]
        clipa_fade_zone = clipa[-frames:]

    if clipb.num_frames == frames:
        clipb_fade_zone = clipb
        clipb_clean = None
    else:
        clipb_clean = clipb[frames:]
        clipb_fade_zone = clipb[:frames]

    def _fade(n: int, clipa: vs.VideoNode, clipb: vs.VideoNode):
        return core.std.Merge(clipa, clipb, weight=[n / (frames - 1)])

    faded = core.std.FrameEval(clipa_fade_zone, functools.partial(_fade, clipa=clipa_fade_zone, clipb=clipb_fade_zone))

    return _return_combo(clipa_clean, faded, clipb_clean)


def fade_to_black(src_clip: vs.VideoNode, frames: int, /):
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
    return fade(src_clip, black_clip_resized, frames)


def push(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT) -> vs.VideoNode:
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
    """
    _check_clips(frames, push, clipa, clipb)

    if clipa.num_frames == frames:
        clipa_push_zone = clipa
        clipa_clean = None
    else:
        clipa_clean = clipa[:-frames]
        clipa_push_zone = clipa[-frames:]

    if clipb.num_frames == frames:
        clipb_push_zone = clipb
        clipb_clean = None
    else:
        clipb_clean = clipb[frames:]
        clipb_push_zone = clipb[:frames]

    if direction == Direction.LEFT:
        stack = core.std.StackHorizontal([clipa_push_zone, clipb_push_zone])

        def _push(n: int):
            w = stack.width // 2
            return stack.resize.Spline36(width=w, src_left=w * n / (frames-1), src_width=w)

        pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_push))

    elif direction == Direction.RIGHT:
        stack = core.std.StackHorizontal([clipb_push_zone, clipa_push_zone])

        def _push(n: int):
            w = stack.width // 2
            return stack.resize.Spline36(width=w, src_left=w-(w * n / (frames - 1)), src_width=w)

        pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_push))

    elif direction == Direction.UP:
        stack = core.std.StackVertical([clipa_push_zone, clipb_push_zone])

        def _push(n: int):
            h = stack.height // 2
            return stack.resize.Spline36(height=h, src_top=h * n / (frames-1), src_height=h)

        pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_push))

    elif direction == Direction.DOWN:
        stack = core.std.StackVertical([clipb_push_zone, clipa_push_zone])

        def _push(n: int):
            h = stack.height // 2
            return stack.resize.Spline36(height=h, src_top=h-(h * n / (frames-1)), src_height=h)

        pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_push))

    return _return_combo(clipa_clean, pushed, clipb_clean)


def wipe(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT) -> vs.VideoNode:
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

    if clipa.num_frames == frames:
        clipa_wipe_zone = clipa
        clipa_clean = None
    else:
        clipa_clean = clipa[:-frames]
        clipa_wipe_zone = clipa[-frames:]

    if clipb.num_frames == frames:
        clipb_wipe_zone = clipb
        clipb_clean = None
    else:
        clipb_clean = clipb[frames:]
        clipb_wipe_zone = clipb[:frames]

    mask = core.imwri.Read(r'./sRGB_gradient_1px_16-bit_dither.png')
    mask_horiz = mask.resize.Spline64(clipa.width, clipa.height, dither_type='error_diffusion',
                                format=mask.format.replace(bits_per_sample=clipa.format.bits_per_sample,
                                                           color_family=vs.GRAY).id)
    mask_vert = core.std.Transpose(mask).resize.Spline64(clipa.width, clipa.height, dither_type='error_diffusion',
                                format=mask.format.replace(bits_per_sample=clipa.format.bits_per_sample,
                                                           color_family=vs.GRAY).id)
    black_clip = core.std.BlankClip(mask_horiz, color=[0])
    white_clip = core.std.BlankClip(mask_horiz, color=[(1 << mask_horiz.format.bits_per_sample) - 1])

    if direction == Direction.LEFT:

        def _wipe(n: int, clipa: vs.VideoNode, clipb: vs.VideoNode):
            stack = core.std.StackHorizontal([black_clip, mask_horiz, white_clip])
            stack = stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width * n / (frames - 1), src_width=mask_horiz.width)
            return core.std.MaskedMerge(clipa, clipb, stack)

        wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_wipe, clipa=clipa_wipe_zone, clipb=clipb_wipe_zone))

    elif direction == Direction.RIGHT:

        def _wipe(n: int, clipa: vs.VideoNode, clipb: vs.VideoNode):
            stack = core.std.StackHorizontal([white_clip, core.std.FlipHorizontal(mask_horiz), black_clip])
            stack = stack.resize.Spline36(width=mask_horiz.width, src_left=2 * mask_horiz.width - (2 * mask_horiz.width * n / (frames - 1)), src_width=mask_horiz.width)
            return core.std.MaskedMerge(clipa, clipb, stack)

        wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_wipe, clipa=clipa_wipe_zone, clipb=clipb_wipe_zone))

    elif direction == Direction.UP:

        def _wipe(n: int, clipa: vs.VideoNode, clipb: vs.VideoNode):
            stack = core.std.StackVertical([black_clip, mask_vert, white_clip])
            stack = stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height * n / (frames - 1), src_height=mask_vert.height)
            return core.std.MaskedMerge(clipa, clipb, stack)

        wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_wipe, clipa=clipa_wipe_zone, clipb=clipb_wipe_zone))

    elif direction == Direction.DOWN:

        def _wipe(n: int, clipa: vs.VideoNode, clipb: vs.VideoNode):
            stack = core.std.StackVertical([white_clip, core.std.FlipVertical(mask_vert), black_clip])
            stack = stack.resize.Spline36(height=mask_vert.height, src_top=2 * mask_vert.height - (2 * mask_vert.height * n / (frames - 1)), src_height=mask_vert.height)
            return core.std.MaskedMerge(clipa, clipb, stack)

        wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), functools.partial(_wipe, clipa=clipa_wipe_zone, clipb=clipb_wipe_zone))

    return _return_combo(clipa_clean, wiped, clipb_clean)
