"""Powerpoint transitions implemented in VapourSynth."""
import enum
import math
import os
import sys
from typing import Callable, Optional, Tuple
from fractions import Fraction

import vapoursynth as vs

try:
    from ._metadata import __author__, __date__, __version__
except ImportError:
    __author__ = __date__ = __version__ = 'unknown (portable version)'

sys.path.insert(0, os.path.abspath('.'))
core = vs.core


class Direction(str, enum.Enum):
    """Direction enumeration"""
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


LEFT = Direction.LEFT
RIGHT = Direction.RIGHT
UP = Direction.UP
DOWN = Direction.DOWN
HORIZONTAL = Direction.HORIZONTAL
VERTICAL = Direction.VERTICAL


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


def _transition_clips(clip1: vs.VideoNode, clip2: vs.VideoNode, frames: int) -> Tuple[Optional[vs.VideoNode], Optional[vs.VideoNode], vs.VideoNode, vs.VideoNode]:
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

    First frame of the fade will be 100% `clipa`, while last frame will be 100% `clipb`.
    As an example, say we have a 100 frame long black clip and 100 frame long white clip:

    >>> black = core.std.BlankClip(format=vs.GRAY8, color=[0], length=100)
    >>> white = core.std.BlankClip(format=vs.GRAY8, color=[255], length=100)

    >>> fade(black, white, 100)

    will result in a pure fade from black to white.
    The first frame (``0``) will be pure black, while the last frame (``99``) will be pure white.

    >>> fade(black, white, 20)

    will result in a 20-frame long fade from the end of the black clip through the beginning of the white clip.
    The first 80 frames (``0``-``79``) will be pure black.
    The first frame of the fade (``80``) will also be pure black.
    At this point, we've consumed 1 frame from the beginning of the white clip.
    The last frame of the fade (``99``) will be pure white.
    At this point, we've consumed 20 frames from the white clip.
    The last 80 frames (``100``-``179``) will be pure white.
    The correct way to line up audio with this would be to crossfade 20 frames from the black clip into the white clip,
    i.e. using the last 20 frames worth of audio from the black clip and the first 20 frames worth of audio from the white clip.
    """
    _check_clips(frames, fade, clipa, clipb)

    clipa_clean, clipb_clean, clipa_fade_zone, clipb_fade_zone = _transition_clips(clipa, clipb, frames)

    def _fade(n: int):
        return core.std.Merge(clipa_fade_zone, clipb_fade_zone, weight=[float(Fraction(n, (frames - 1)))])

    if use_frame_eval:
        faded = core.std.FrameEval(clipa_fade_zone, _fade)
    else:
        faded = core.std.Splice([core.std.Merge(clipa_fade_zone,
                                                clipb_fade_zone,
                                                weight=[float(Fraction(n, (frames - 1)))])[n]
                                 for n in range(frames)])

    return _return_combo(clipa_clean, faded, clipb_clean)


def poly_fade(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, exponent: int = 1) -> vs.VideoNode:
    """
    Cross-fade clips according to a curve.
    The curve `exponent` is an int in the range from 1-5
    where 1 represents a parabolic curve, 2 represents a quartic curve,
    and higher powers more resembling an tight ease-in-out function with constant speed for most of the transition.
    """
    _check_clips(frames, poly_fade, clipa, clipb)

    if not (1 <= exponent <= 5):
        raise ValueError("poly_fade: exponent must be an int between 1 and 5 (inclusive)")

    clipa_clean, clipb_clean, clipa_fade_zone, clipb_fade_zone = _transition_clips(clipa, clipb, frames)

    def get_pos(x: float) -> float:
        """Returns position as a float 0-1, based on a input percentage float 0-1"""

        def _curve(x: float) -> float:
            return -(((2 * x - 1) ** (2 * exponent + 1)) / (4 * exponent + 2)) + x - 0.5

        return round(((_curve(1)-_curve(0)) ** -1) * (_curve(x) - _curve(0)), 9)

    def _fade(n: int):
        percentage = n / (frames - 1)
        return core.std.Merge(clipa_fade_zone, clipb_fade_zone, weight=[get_pos(percentage)])

    faded = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _fade)

    return _return_combo(clipa_clean, faded, clipb_clean)


def fade_to_black(src_clip: vs.VideoNode, frames: int, /, use_frame_eval: bool = True) -> vs.VideoNode:
    """Linear Transition.
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


def wipe(clipa: vs.VideoNode,
         clipb: vs.VideoNode,
         frames: int,
         direction: Direction = Direction.LEFT,
         use_frame_eval: bool = True,
         gradient_image: str = r'./sRGB_gradient_1px_16-bit_dither.png') -> vs.VideoNode:
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
    if not os.path.isfile(gradient_image):
        raise FileNotFoundError(f"wipe: the gradient image {gradient_image} was not found")

    _check_clips(frames, wipe, clipa, clipb)

    clipa_clean, clipb_clean, clipa_wipe_zone, clipb_wipe_zone = _transition_clips(clipa, clipb, frames)

    mask = core.imwri.Read(gradient_image)
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


def squeeze_slide_in(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT) -> vs.VideoNode:
    """clipa gets squeezed to nothing while clipb enters the frame moving in `direction` at its initial size"""
    _check_clips(frames, squeeze_slide_in, clipa, clipb)

    clipa_clean, clipb_clean, clipa_squeeze_zone, clipb_slide_zone = _transition_clips(clipa, clipb, frames)

    if direction == Direction.LEFT:

        def _squeeze(n: int):
            scale = 1 - (n / (frames - 1))  # scale factor for clipa
            w = math.floor(scale * clipa.width)
            if w:
                resized_a = clipa_squeeze_zone.resize.Spline36(width=w)
                stack = core.std.StackHorizontal([resized_a, clipb_slide_zone])
                return stack.std.Crop(right=w)
            else:
                return clipb_slide_zone

        squeezed =  core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.RIGHT:

        def _squeeze(n: int):
            scale = 1 - (n / (frames - 1))
            w = math.floor(scale * clipa.width)
            if w:
                resized_a = clipa_squeeze_zone.resize.Spline36(width=w)
                stack = core.std.StackHorizontal([clipb_slide_zone, resized_a])
                return stack.std.Crop(left=w)
            else:
                return clipb_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.UP:

        def _squeeze(n: int):
            scale = 1 - (n / (frames - 1))
            h = math.floor(scale * clipa.height)
            if h:
                resized_a = clipa_squeeze_zone.resize.Spline36(height=h)
                stack = core.std.StackVertical([resized_a, clipb_slide_zone])
                return stack.std.Crop(bottom=h)
            else:
                return clipb_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.DOWN:

        def _squeeze(n: int):
            scale = 1 - (n / (frames - 1))
            h = math.floor(scale * clipa.height)
            if h:
                resized_a = clipa_squeeze_zone.resize.Spline36(height=h)
                stack = core.std.StackVertical([clipb_slide_zone, resized_a])
                return stack.std.Crop(top=h)
            else:
                return clipb_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    else:
        raise ValueError("squeeze_slide_in: give a proper direction")

    return _return_combo(clipa_clean, squeezed, clipb_clean)


def expand_slide_out(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT) -> vs.VideoNode:
    """clipa slides out of frame while clipb starts from 0-width and expands in moving in `direction` filling the space"""

    _check_clips(frames, expand_slide_out, clipa, clipb)

    clipa_clean, clipb_clean, clipa_slide_zone, clipb_squeeze_zone = _transition_clips(clipa, clipb, frames)

    if direction == Direction.LEFT:

        def _squeeze(n: int):
            scale = n / (frames - 1)
            w = math.floor(scale * clipa.width)
            if w:
                resized_b = clipb_squeeze_zone.resize.Spline36(width=w)
                stack = core.std.StackHorizontal([clipa_slide_zone, resized_b])
                return stack.std.Crop(left=w)
            else:
                return clipa_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.RIGHT:

        def _squeeze(n: int):
            scale = n / (frames - 1)
            w = math.floor(scale * clipa.width)
            if w:
                resized_b = clipb_squeeze_zone.resize.Spline36(width=w)
                stack = core.std.StackHorizontal([resized_b, clipa_slide_zone])
                return stack.std.Crop(right=w)
            else:
                return clipa_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.UP:

        def _squeeze(n: int):
            scale = n / (frames - 1)
            h = math.floor(scale * clipa.height)
            if h:
                resized_b = clipb_squeeze_zone.resize.Spline36(height=h)
                stack = core.std.StackVertical([clipa_slide_zone, resized_b])
                return stack.std.Crop(top=h)
            else:
                return clipa_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction == Direction.DOWN:

        def _squeeze(n: int):
            scale = n / (frames - 1)
            h = math.floor(scale * clipa.height)
            if h:
                resized_b = clipb_squeeze_zone.resize.Spline36(height=h)
                stack = core.std.StackVertical([resized_b, clipa_slide_zone])
                return stack.std.Crop(bottom=h)
            else:
                return clipa_slide_zone

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    else:
        raise ValueError("expand_slide_out: give a proper direction")

    return _return_combo(clipa_clean, squeezed, clipb_clean)


def squeeze_expand(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT):
    """clipa gets squeezed to nothing while clipb expands from nothing, clipb expands towards `direction`"""

    _check_clips(frames, squeeze_expand, clipa, clipb)

    clipa_clean, clipb_clean, clipa_squeeze_zone, clipb_squeeze_zone = _transition_clips(clipa, clipb, frames)

    if direction in [Direction.LEFT, Direction.RIGHT]:

        def _squeeze(n: int):
            clipb_width = math.floor(clipa.width * n / (frames - 1))
            clipa_width = clipa.width - clipb_width

            if clipa_width == clipa.width:
                return clipa_squeeze_zone
            elif clipb_width == clipa.width:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(width=clipa_width)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(width=clipb_width)
                if direction == Direction.LEFT:
                    return core.std.StackHorizontal([clipa_squeezed, clipb_squeezed])
                else:
                    return core.std.StackHorizontal([clipb_squeezed, clipa_squeezed])

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    elif direction in [Direction.UP, Direction.DOWN]:

        def _squeeze(n: int):
            clipb_height = math.floor(clipa.height * n / (frames - 1))
            clipa_height = clipa.height - clipb_height

            if clipa_height == clipa.height:
                return clipa_squeeze_zone
            elif clipb_height == clipa.height:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(height=clipa_height)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(height=clipb_height)
                if direction == Direction.UP:
                    return core.std.StackVertical([clipa_squeezed, clipb_squeezed])
                else:
                    return core.std.StackVertical([clipb_squeezed, clipa_squeezed])

        squeezed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _squeeze)

    else:
        raise ValueError("squeeze_expand: give a proper direction")

    return _return_combo(clipa_clean, squeezed, clipb_clean)


def cube_rotate(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: int, direction: Direction = Direction.LEFT, exaggeration: int = 0) -> vs.VideoNode:
    """
    Mimics a cube face rotation by adjusting the speed at which the squeeze boundary moves.
    Cube face containing `clipa` rotates away from the viewer in `direction`.

    `exaggeration` is an integer between 0 and 100 (inclusive) representing how much the effect of the cosine wave should be exaggerated:
        0 corresponds to a mathematically correct projection of a 90 degree rotation offset by 45 degrees
            initial and final velocities are pi/4 (0.785x), middle velocity is pi / (2 * sqrt2) (1.11x)
        100 corresponds to a fitted cosine wave where the initial and final velocities are 0, while the velocity at the middle is pi/2 (1.571x)
    """

    _check_clips(frames, cube_rotate, clipa, clipb)

    if not (0 <= exaggeration <= 100):
        raise ValueError(f"cube_rotate: exaggeration {exaggeration} not between 0 and 100")

    clipa_clean, clipb_clean, clipa_squeeze_zone, clipb_squeeze_zone = _transition_clips(clipa, clipb, frames)

    def rotation(percentage: float) -> float:
        """Return a radian rotation based on `percentage` ranging from -pi/4 at 0% to -3pi/4 at 100%"""
        return (-math.pi/2) * percentage - math.pi/4

    def position(percentage: float, bias: int) -> float:
        """
        Return position of a rotated edge as a percentage
        0% at 0%, 23% at 25%, 50% at 50%, 77% at 75%, 100% at 100%
        """
        def _projection(x: float):
            """mathmatically correct projection"""
            return (-math.cos(rotation(x)) + (math.sqrt(2)/2)) / math.sqrt(2)

        def _fitted(x: float):
            """fitted cosine wave to exaggerate the effects"""
            return -.5*math.cos(2*rotation(x) + math.pi/2)+.5

        if bias == 0:
            return round(_projection(percentage), 9)
        elif bias == 100:
            return round(_fitted(percentage), 9)
        else:
            fitted = (bias / 100) * _fitted(percentage)
            projection = ((100 - bias) / 100) * _projection(percentage)
            return round(fitted + projection, 9)

    if direction in [Direction.LEFT, Direction.RIGHT]:

        def _rotate(n: int):
            clipb_width = math.floor(clipa.width * position(n / (frames - 1), exaggeration))
            clipa_width = clipa.width - clipb_width

            if clipa_width == clipa.width:
                return clipa_squeeze_zone
            elif clipb_width == clipa.width:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(width=clipa_width)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(width=clipb_width)
                if direction == Direction.LEFT:
                    return core.std.StackHorizontal([clipa_squeezed, clipb_squeezed])
                else:
                    return core.std.StackHorizontal([clipb_squeezed, clipa_squeezed])

        rotated = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _rotate)

    elif direction in [Direction.UP, Direction.DOWN]:

        def _rotate(n: int):
            clipb_height = math.floor(clipa.height * position(n / (frames - 1), exaggeration))
            clipa_height = clipa.height - clipb_height

            if clipa_height == clipa.height:
                return clipa_squeeze_zone
            elif clipb_height == clipa.height:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(height=clipa_height)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(height=clipb_height)
                if direction == Direction.UP:
                    return core.std.StackVertical([clipa_squeezed, clipb_squeezed])
                else:
                    return core.std.StackVertical([clipb_squeezed, clipa_squeezed])

        rotated = core.std.FrameEval(core.std.BlankClip(clipa, length=frames), _rotate)

    else:
        raise ValueError("cube_rotate: give a proper direction")

    return _return_combo(clipa_clean, rotated, clipb_clean)


# marine = core.ffms2.Source('/home/stalled/marine.mp4')
# marine = marine.resize.Bicubic(format=marine.format.replace(subsampling_w=0, subsampling_h=0).id)[:190]
# pekora = core.ffms2.Source('/home/stalled/pekora.mp4')
# pekora = pekora.resize.Bicubic(format=pekora.format.replace(subsampling_w=0, subsampling_h=0).id)[:190]
#
#
# a=poly_fade(marine, pekora, 170)
# b=poly_fade(marine, pekora, 170, 5)
# c=fade(marine, pekora, 170)
# core.std.StackVertical([a,b,c]).set_output()
#
# # # a = squeeze_expand(marine, pekora, 120).text.Text('linear')
# # # b = cube_rotate(marine, pekora, 120).text.Text('cosine projection')
# # # c = cube_rotate(marine, pekora, 120, exaggeration=50).text.Text('50% bias')
# # # d = cube_rotate(marine, pekora, 120, exaggeration=100).text.Text('fitted cosine (100% bias)')
# #
# def _blur(n: int):
#     return core.std.BoxBlur(marine, hradius=1, hpasses=n+1, vradius=1, vpasses=n+1)
# #
# core.std.FrameEval(core.std.BlankClip(marine, length=140), _blur).set_output()
#
# def _blur2(n: int):
#     return core.std.BoxBlur(marine, hradius=0, hpasses=n+1, vradius=0, vpasses=n+1)
#
# core.std.FrameEval(marine, _blur2).set_output(1)
#
# #
# # marine.std.BoxBlur(hradius=1, hpasses=1, vradius=1, vpasses=1).set_output()
# # marine.std.BoxBlur(hradius=2, hpasses=1, vradius=2, vpasses=1).set_output(1)
# # marine.std.BoxBlur(hradius=1, hpasses=2, vradius=1, vpasses=2).set_output(2)
# # marine.std.BoxBlur(hradius=2, hpasses=2, vradius=2, vpasses=2).set_output(3)
# # marine.resize.Point(width=marine.width//4, height=marine.width//4).std.Median().resize.Point(width=marine.width, height=marine.height).set_output(5)
# # marine.resize.Point(width=marine.width//4, height=marine.width//4).resize.Point(width=marine.width, height=marine.height).set_output(6)
# # marine.resize.Point(width=marine.width//8, height=marine.width//8).resize.Point(width=marine.width, height=marine.height).set_output(7)
# # marine.resize.Point(width=marine.width//12, height=marine.width//12).std.Median().resize.Point(width=marine.width, height=marine.height).set_output(8)
# # marine.resize.Point(width=marine.width//15, height=marine.width//15).resize.Point(width=marine.width, height=marine.height).set_output(9)
# #
# # # vsutil.iterate(marine, core.std.Median, 5).set_output(4)
#
#
# # def blur_fade
