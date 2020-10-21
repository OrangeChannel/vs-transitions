"""Powerpoint-like transitions implemented in VapourSynth."""
__all__ = [
    "cover",
    "cube_rotate",
    "fade",
    "fade_from_black",
    "fade_to_black",
    "linear_boundary",
    "poly_fade",
    "push",
    "reveal",
    "slide_expand",
    "squeeze_expand",
    "squeeze_slide",
    "wipe",
]

import enum
import math
from fractions import Fraction
from typing import Callable, Optional, Tuple, TYPE_CHECKING
from warnings import simplefilter, warn

import vapoursynth as vs

try:
    from ._metadata import __author__, __date__, __version__  # type: ignore
except (ImportError, ModuleNotFoundError):
    __author__ = __date__ = __version__ = "unknown (portable version)"  # type: ignore

simplefilter("always")

core = vs.core


class Direction(str, enum.Enum):
    """Direction enumeration.

    Members can be simply referenced by their names,
    i.e. ``vs_transitions.LEFT`` instead of ``vs_transitions.Direction.LEFT``.
    """

    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


LEFT = Direction.LEFT
RIGHT = Direction.RIGHT
UP = Direction.UP
DOWN = Direction.DOWN
HORIZONTAL = Direction.HORIZONTAL
VERTICAL = Direction.VERTICAL
__all__ += list(Direction.__members__)


class MiscConstants(str, enum.Enum):
    """Miscellanious enumeration for some functions.

    Members can be simply referenced by their names,
    i.e. ``vs_transitions.SLIDE`` instead of ``vs_transitions.MiscConstants.SLIDE``.
    """

    SLIDE = "slide"
    SQUEEZE = "squeeze"
    EXPAND = "expand"


SLIDE = MiscConstants.SLIDE
SQUEEZE = MiscConstants.SQUEEZE
EXPAND = MiscConstants.EXPAND
__all__ += list(MiscConstants.__members__)


def _check_clips(frames: int, caller: Callable, *clips: vs.VideoNode, **kwargs) -> None:
    """General checker for clip formats, resolutions, length, and other keywords.

    Possible kwargs:
        'subsampling': checks that all clips have 444 subsampling for resize purposes
    """
    if frames <= 0:
        raise ValueError(f"{caller.__name__}: `frames` cannot be less than 1")
    same_check = set()
    for clip in clips:
        if clip.format is None:
            raise ValueError(f"{caller.__name__}: all clips must be constant-format")
        if 0 in (clip.width, clip.height):
            raise ValueError(f"{caller.__name__}: all clips must be constant-resolution")
        if clip.num_frames < frames:
            raise ValueError(f"{caller.__name__}: all clips must have at least {frames} frames")
        same_check.add((clip.format.id, clip.width, clip.height))

        if kwargs:
            if ("subsampling" in kwargs) and kwargs["subsampling"]:
                if clip.format.subsampling_w != 0 or clip.format.subsampling_h != 0:
                    raise ValueError(
                        f"{caller.__name__}: all clips must have 444 chroma subsampling for a non-mod2 resize"
                    )

    if len(same_check) > 1:
        raise ValueError(f"{caller.__name__}: all clips must be same format and resolution")


def _return_combo(
    clip1: Optional[vs.VideoNode],
    clip_middle: vs.VideoNode,
    clip2: Optional[vs.VideoNode],
) -> vs.VideoNode:
    """Prevents splicing empty clips.

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


def _transition_clips(
    clip1: vs.VideoNode, clip2: vs.VideoNode, frames: int
) -> Tuple[Optional[vs.VideoNode], Optional[vs.VideoNode], vs.VideoNode, vs.VideoNode]:
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


def fade(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None) -> vs.VideoNode:
    """Cross-fade clips."""
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, fade, clipa, clipb)
    clipa_clean, clipb_clean, clipa_fade_zone, clipb_fade_zone = _transition_clips(clipa, clipb, frames_)

    def _fade(n: int) -> vs.VideoNode:
        progress = Fraction(n, frames_ - 1)
        if progress == 0:
            return clipa_fade_zone
        elif progress == 1:
            return clipb_fade_zone
        else:
            return core.std.Merge(
                clipa_fade_zone,
                clipb_fade_zone,
                weight=[float(progress)],
            )

    faded = core.std.FrameEval(clipa_fade_zone, _fade)

    return _return_combo(clipa_clean, faded, clipb_clean)


def poly_fade(
    clipa: vs.VideoNode,
    clipb: vs.VideoNode,
    frames: Optional[int] = None,
    exponent: int = 1,
) -> vs.VideoNode:
    """Cross-fade clips according to a curve.

    The curve `exponent` is an integer in the range from 1-5
    where 1 represents a parabolic curve, 2 represents a quartic curve,
    and higher powers more resembling an tight ease-in-out function with constant speed for most of the transition.

    An `exponent` of ``1`` is probably most useful, as higher exponents tend towards a constant speed and therefore are
    almost indistinguishable from a normal :func:`fade`.
    """
    if not (1 <= exponent <= 5):
        raise ValueError("poly_fade: exponent must be an int between 1 and 5 (inclusive)")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, fade, clipa, clipb)
    clipa_clean, clipb_clean, clipa_fade_zone, clipb_fade_zone = _transition_clips(clipa, clipb, frames_)

    def get_pos(x: Fraction) -> Fraction:
        """Returns position as a fractions.Fraction, based on a input percentage fractions.Fraction"""

        def _curve(y: Fraction) -> Fraction:
            return -(((2 * y - 1) ** (2 * exponent + 1)) / (4 * exponent + 2)) + y - Fraction(1, 2)

        return ((_curve(Fraction(1, 1)) - _curve(Fraction())) ** -1) * (_curve(x) - _curve(Fraction()))

    def _fade(n: int) -> vs.VideoNode:
        progress = Fraction(n, frames_ - 1)
        if progress == 0:
            return clipa_fade_zone
        elif progress == 1:
            return clipb_fade_zone
        else:
            return core.std.Merge(clipa_fade_zone, clipb_fade_zone, weight=[float(get_pos(progress))])

    faded = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _fade)

    return _return_combo(clipa_clean, faded, clipb_clean)


def fade_to_black(src_clip: vs.VideoNode, frames: Optional[int] = None) -> vs.VideoNode:
    """Simple convenience function to :func:`fade` a clip to black.

    `frames` will be the number of frames consumed from the end of the `src_clip` during the transition.
    The first frame of the transition will be the first frame of the `src_clip`,
    while the last frame of the transition will be a pure black frame.

    If `frames` is not given, will fade to black over the entire duration of the `src_clip`.
    """
    if src_clip.format is None:
        raise ValueError("fade_to_black: `src_clip` must be a constant format VideoNode")
    black_clip = core.std.BlankClip(format=vs.GRAY8, length=frames, color=[0])
    if TYPE_CHECKING:
        assert black_clip.format is not None
        assert src_clip.format is not None
    black_clip_resized = black_clip.resize.Point(
        width=src_clip.width,
        height=src_clip.height,
        format=black_clip.format.replace(
            color_family=src_clip.format.color_family,
            sample_type=src_clip.format.sample_type,
            bits_per_sample=src_clip.format.bits_per_sample,
            subsampling_w=src_clip.format.subsampling_w,
            subsampling_h=src_clip.format.subsampling_h,
        ).id,
    )
    return fade(src_clip, black_clip_resized, frames)


def fade_from_black(src_clip: vs.VideoNode, frames: Optional[int] = None) -> vs.VideoNode:
    """Simple convenience function to :func:`fade` a clip into view from black.

    `frames` will be the number of frames consumed from the start of the `src_clip` during the transition.
    The first frame of the transition will be a pure black frame,
    while the last frame of the transition will be the last frame of the `src_clip`.

    If `frames` is not given, will fade in over the entire duration of the `src_clip`.
    """
    if src_clip.format is None:
        raise ValueError("fade_to_black: `src_clip` must be a constant format VideoNode")
    black_clip = core.std.BlankClip(format=vs.GRAY8, length=frames, color=[0])
    if TYPE_CHECKING:
        assert black_clip.format is not None
        assert src_clip.format is not None
    black_clip_resized = black_clip.resize.Point(
        width=src_clip.width,
        height=src_clip.height,
        format=black_clip.format.replace(
            color_family=src_clip.format.color_family,
            sample_type=src_clip.format.sample_type,
            bits_per_sample=src_clip.format.bits_per_sample,
            subsampling_w=src_clip.format.subsampling_w,
            subsampling_h=src_clip.format.subsampling_h,
        ).id,
    )
    return fade(black_clip_resized, src_clip, frames)


def wipe(
    clipa: vs.VideoNode,
    clipb: vs.VideoNode,
    frames: Optional[int] = None,
    direction: Direction = Direction.LEFT,
) -> vs.VideoNode:
    """A moving directional fade.

    Similar to a :func:`fade`, but with a moving mask.
    The `direction` will be the direction the fade progresses towards.
    (i.e. the second clip begins fading in from the **opposite** given direction,
    and the first clip begins fading out starting from the **opposite** given direction,
    progressing towards `direction`)

    Uses a pure white to black gradient for the fade.
    If possible, uses `numpy <https://pypi.org/project/numpy/>`_ to generate the mask.
    If the numpy module is not found, falls back to a slower
    and possibly less accurate approach using lists
    and the ``ctypes`` module for writing to a VapourSynth frame.
    """
    if direction not in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        raise ValueError("wipe: give a proper direction")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, wipe, clipa, clipb)
    clipa_clean, clipb_clean, clipa_wipe_zone, clipb_wipe_zone = _transition_clips(clipa, clipb, frames_)

    blank_clip = core.std.BlankClip(width=1 << 16, height=1, format=vs.GRAYS, color=[0.0], length=1)
    write_frame = blank_clip.get_frame(0).copy()
    try:
        import numpy as np

        def frame_writer(n, f):
            if n is not None:
                pass
            fout = f.copy()
            ptr = np.asarray(fout.get_write_array(0))
            ptr[0] = np.linspace(0, 1, 1 << 16)
            return fout

        mask = blank_clip.std.ModifyFrame([blank_clip], frame_writer)

    except (ImportError, ModuleNotFoundError):
        warn("wipe: numpy module not found, falling back to slower less accurate method", Warning)
        import ctypes

        ptr_type = ctypes.c_float * (1 << 16)
        vs_ptr = ctypes.cast(write_frame.get_write_ptr(0), ctypes.POINTER(ptr_type))
        float_lin_array = [i / ((1 << 16) - 1) for i in list(range(1 << 16))]
        float_Arr_ptr = ctypes.pointer(ptr_type(*float_lin_array))
        vs_ptr[0] = float_Arr_ptr[0]
        mask = blank_clip.std.ModifyFrame([blank_clip], lambda n, f: write_frame)

    mask = mask.grain.Add()
    if TYPE_CHECKING:
        assert mask.format is not None
        assert clipa.format is not None
    mask_horiz = mask.resize.Spline64(
        clipa.width,
        clipa.height,
        dither_type="error_diffusion",
        format=mask.format.replace(
            bits_per_sample=clipa.format.bits_per_sample, color_family=vs.GRAY, sample_type=clipa.format.sample_type
        ).id,
        matrix_in_s="rgb",
    )
    mask_vert = core.std.Transpose(mask).resize.Spline64(
        clipa.width,
        clipa.height,
        dither_type="error_diffusion",
        format=mask.format.replace(
            bits_per_sample=clipa.format.bits_per_sample, color_family=vs.GRAY, sample_type=clipa.format.sample_type
        ).id,
        matrix_in_s="rgb",
    )
    black_clip = core.std.BlankClip(mask_horiz, length=1, color=[0])
    white_clip = core.std.BlankClip(mask_horiz, length=1, color=[(1 << clipa.format.bits_per_sample) - 1])

    if direction in [Direction.LEFT, Direction.RIGHT]:
        stack = core.std.StackHorizontal([black_clip, mask_horiz, white_clip])
        w = mask_horiz.width

        if direction == Direction.LEFT:

            def _wipe(n: int) -> vs.VideoNode:
                stack_ = stack.resize.Spline36(
                    width=w,
                    src_left=2 * w * n / (frames_ - 1),
                    src_width=w,
                )
                return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        elif direction == Direction.RIGHT:
            stack = core.std.FlipHorizontal(stack)

            def _wipe(n: int) -> vs.VideoNode:
                stack_ = stack.resize.Spline36(
                    width=w,
                    src_left=(2 * w) * (1 - n / (frames_ - 1)),
                    src_width=w,
                )
                return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

    elif direction in [Direction.UP, Direction.DOWN]:
        stack = core.std.StackVertical([black_clip, mask_vert, white_clip])
        h = mask_vert.height

        if direction == Direction.UP:

            def _wipe(n: int) -> vs.VideoNode:
                stack_ = stack.resize.Spline36(
                    height=h,
                    src_top=2 * h * n / (frames_ - 1),
                    src_height=h,
                )
                return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

        elif direction == Direction.DOWN:
            stack = core.std.FlipVertical(stack)

            def _wipe(n: int) -> vs.VideoNode:
                stack_ = stack.resize.Spline36(
                    height=h,
                    src_top=(2 * h) * (1 - n / (frames_ - 1)),
                    src_height=h,
                )
                return core.std.MaskedMerge(clipa_wipe_zone, clipb_wipe_zone, stack_)

    wiped = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _wipe)

    return _return_combo(clipa_clean, wiped, clipb_clean)


def cube_rotate(
    clipa: vs.VideoNode,
    clipb: vs.VideoNode,
    frames: Optional[int] = None,
    direction: Direction = Direction.LEFT,
    exaggeration: int = 0,
) -> vs.VideoNode:
    """Mimics a cube face rotation by adjusting the speed at which the :func:`squeeze_expand` boundary moves.

    Cube face containing `clipa` rotates away from the viewer in projected 3-D space towards `direction`.

    `exaggeration` is an integer between 0 and 100 (inclusive) representing how much the effect of the cosine wave should be exaggerated:

        `0` corresponds to a mathematically correct projection of a 90 degree rotation offset by 45 degrees.

            Initial and final velocities are ``pi/4 (0.785x)``,
            and the middle velocity is ``pi / (2 * sqrt2) (1.11x)`` (relative to the linear transition).

        `100` corresponds to a fitted cosine wave where the initial and final velocities are ``0``,
        and the velocity at the middle is ``pi/2 (1.571x)`` (relative to the linear transition).
    """
    if direction not in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        raise ValueError("cube_rotate: give a proper direction")
    if not (0 <= exaggeration <= 100):
        raise ValueError(f"cube_rotate: exaggeration {exaggeration} not between 0 and 100")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, cube_rotate, clipa, clipb)
    clipa_clean, clipb_clean, clipa_squeeze_zone, clipb_squeeze_zone = _transition_clips(clipa, clipb, frames_)

    def rotation(percentage: float) -> float:
        """Return a radian rotation based on `percentage` ranging from -pi/4 at 0% to -3pi/4 at 100%"""
        return (-math.pi / 2) * percentage - math.pi / 4

    def position(percentage: float, bias: int) -> float:
        """
        Return position of a rotated edge as a percentage
        0% at 0%, 23% at 25%, 50% at 50%, 77% at 75%, 100% at 100%
        """

        def _projection(x: float):
            """mathmatically correct projection"""
            return (-math.cos(rotation(x)) + (math.sqrt(2) / 2)) / math.sqrt(2)

        def _fitted(x: float):
            """fitted cosine wave to exaggerate the effects"""
            return -0.5 * math.cos(2 * rotation(x) + math.pi / 2) + 0.5

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
            w_inc = math.floor(clipa.width * position(n / (frames_ - 1), exaggeration))
            w_dec = clipa.width - w_inc

            if w_dec == clipa.width:
                return clipa_squeeze_zone
            elif w_inc == clipa.width:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(width=w_dec)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(width=w_inc)
                if direction == Direction.LEFT:
                    return core.std.StackHorizontal([clipa_squeezed, clipb_squeezed])
                elif direction == Direction.RIGHT:
                    return core.std.StackHorizontal([clipb_squeezed, clipa_squeezed])

    elif direction in [Direction.UP, Direction.DOWN]:

        def _rotate(n: int):
            h_inc = math.floor(clipa.height * position(n / (frames_ - 1), exaggeration))
            h_dec = clipa.height - h_inc

            if h_dec == clipa.height:
                return clipa_squeeze_zone
            elif h_inc == clipa.height:
                return clipb_squeeze_zone
            else:
                clipa_squeezed = clipa_squeeze_zone.resize.Spline36(height=h_dec)
                clipb_squeezed = clipb_squeeze_zone.resize.Spline36(height=h_inc)
                if direction == Direction.UP:
                    return core.std.StackVertical([clipa_squeezed, clipb_squeezed])
                elif direction == Direction.DOWN:
                    return core.std.StackVertical([clipb_squeezed, clipa_squeezed])

    rotated = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _rotate)

    return _return_combo(clipa_clean, rotated, clipb_clean)


def linear_boundary(
    clipa: vs.VideoNode,
    clipb: vs.VideoNode,
    clipa_movement: MiscConstants,
    clipb_movement: MiscConstants,
    frames: Optional[int] = None,
    direction: Direction = Direction.LEFT,
) -> vs.VideoNode:
    """Generalized boundary moving function for a linear transition between two stacked clips.

    `clipa` can either slide out of view (having its size unchanged) or be squeezed to nothing from its original size.
    `clipb` can either slide into view (having its size unchanged) or be expanded from nothing to its full size.
    The boundary between the two clips moves towards `direction`.

    The parameter `clipa_movement` can be :attr:`MiscConstants.SLIDE` or :attr:`MiscConstants.SQUEEZE`.
    The parameter `clipb_movement` can be :attr:`MiscConstants.SLIDE` or :attr:`MiscConstants.EXPAND`.

    See :func:`push`, :func:`slide_expand`, :func:`squeeze_slide`, or :func:`squeeze_expand`
    for simpler aliases in the same form as most other linear, directional transitions.
    """
    if clipa_movement not in [MiscConstants.SLIDE, MiscConstants.SQUEEZE]:
        raise ValueError("linear_boundary: clipa_movement must be either a slide or a squeeze")
    if clipb_movement not in [MiscConstants.SLIDE, MiscConstants.EXPAND]:
        raise ValueError("linear_boundary: clipb_movement must be either a slide or an expand")
    if direction not in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        raise ValueError("linear_boundary: give a proper direction")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    check_for_subsampling = not (
        clipa_movement == clipb_movement == MiscConstants.SLIDE
    )  # only need subsampling check if resizing
    _check_clips(frames_, linear_boundary, clipa, clipb, subsampling=check_for_subsampling)
    clipa_clean, clipb_clean, clipa_t_zone, clipb_t_zone = _transition_clips(clipa, clipb, frames_)

    if clipa_movement == clipb_movement == MiscConstants.SLIDE:
        w, h = clipa.width, clipa.height

        def _stack(clipa_: vs.VideoNode, clipb_: vs.VideoNode) -> vs.VideoNode:
            if direction == Direction.LEFT:
                return core.std.StackHorizontal([clipa_, clipb_])
            elif direction == Direction.RIGHT:
                return core.std.StackHorizontal([clipb_, clipa_])
            elif direction == Direction.UP:
                return core.std.StackVertical([clipa_, clipb_])
            elif direction == Direction.DOWN:
                return core.std.StackVertical([clipb_, clipa_])

        stack = _stack(clipa_t_zone, clipb_t_zone)

        def _push(n: int) -> vs.VideoNode:
            if direction == Direction.LEFT:
                return stack.resize.Spline36(width=w, src_left=w * n / (frames_ - 1), src_width=w)
            elif direction == Direction.RIGHT:
                return stack.resize.Spline36(width=w, src_left=w * (1 - n / (frames_ - 1)), src_width=w)
            elif direction == Direction.UP:
                return stack.resize.Spline36(height=h, src_top=h * n / (frames_ - 1), src_height=h)
            elif direction == Direction.DOWN:
                return stack.resize.Spline36(height=h, src_top=h * (1 - n / (frames_ - 1)), src_height=h)

        pushed = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _push)

        return _return_combo(clipa_clean, pushed, clipb_clean)

    elif clipa_movement == MiscConstants.SLIDE and clipb_movement == MiscConstants.EXPAND:

        def _slide_expand(n: int):
            scale = Fraction(n, frames_ - 1)

            if scale == 0:
                return clipa_t_zone
            elif scale == 1:
                return clipb_t_zone

            if direction in [Direction.LEFT, Direction.RIGHT]:
                w = math.floor(scale * clipa.width)

                if w == 0:
                    return clipa_t_zone

                if direction == Direction.LEFT:
                    stack = core.std.StackHorizontal([clipa_t_zone, clipb_t_zone.resize.Spline36(width=w)])
                    return stack.std.Crop(left=w)
                elif direction == Direction.RIGHT:
                    stack = core.std.StackHorizontal([clipb_t_zone.resize.Spline36(width=w), clipa_t_zone])
                    return stack.std.Crop(right=w)

            elif direction in [Direction.UP, Direction.DOWN]:
                h = math.floor(scale * clipa.height)

                if h == 0:
                    return clipa_t_zone

                if direction == Direction.UP:
                    stack = core.std.StackVertical([clipa_t_zone, clipb_t_zone.resize.Spline36(height=h)])
                    return stack.std.Crop(top=h)
                elif direction == Direction.DOWN:
                    stack = core.std.StackVertical([clipb_t_zone.resize.Spline36(height=h), clipa_t_zone])
                    return stack.std.Crop(bottom=h)

        slide_expanded = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _slide_expand)

        return _return_combo(clipa_clean, slide_expanded, clipb_clean)

    elif clipa_movement == MiscConstants.SQUEEZE and clipb_movement == MiscConstants.SLIDE:

        def _squeeze_slide(n: int):
            scale = 1 - Fraction(n, frames_ - 1)

            if scale == 1:
                return clipa_t_zone
            elif scale == 0:
                return clipb_t_zone

            if direction in [Direction.LEFT, Direction.RIGHT]:
                w = math.floor(scale * clipa.width)

                if w == 0:
                    return clipb_t_zone

                if direction == Direction.LEFT:
                    stack = core.std.StackHorizontal([clipa_t_zone.resize.Spline36(width=w), clipb_t_zone])
                    return stack.std.Crop(right=w)
                elif direction == Direction.RIGHT:
                    stack = core.std.StackHorizontal([clipb_t_zone, clipa_t_zone.resize.Spline36(width=w)])
                    return stack.std.Crop(left=w)

            elif direction in [Direction.UP, Direction.DOWN]:
                h = math.floor(scale * clipa.height)

                if h == 0:
                    return clipb_t_zone

                if direction == Direction.UP:
                    stack = core.std.StackVertical([clipa_t_zone.resize.Spline36(height=h), clipb_t_zone])
                    return stack.std.Crop(bottom=h)

                elif direction == Direction.DOWN:
                    stack = core.std.StackVertical([clipb_t_zone, clipa_t_zone.resize.Spline36(height=h)])
                    return stack.std.Crop(top=h)

        squeeze_slided = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _squeeze_slide)

        return _return_combo(clipa_clean, squeeze_slided, clipb_clean)

    elif clipa_movement == MiscConstants.SQUEEZE and clipb_movement == MiscConstants.EXPAND:

        def _squeeze_expand(n: int) -> vs.VideoNode:
            scale = Fraction(n, frames_ - 1)

            if scale == 0:
                return clipa_t_zone
            elif scale == 1:
                return clipb_t_zone

            if direction in [Direction.LEFT, Direction.RIGHT]:
                w_inc = math.floor(scale * clipa.width)
                w_dec = clipa.width - w_inc

                if w_inc == 0:
                    return clipa_t_zone

                if direction == Direction.LEFT:
                    return core.std.StackHorizontal(
                        [clipa_t_zone.resize.Spline36(width=w_dec), clipb_t_zone.resize.Spline36(width=w_inc)]
                    )
                elif direction == Direction.RIGHT:
                    return core.std.StackHorizontal(
                        [clipb_t_zone.resize.Spline36(width=w_inc), clipa_t_zone.resize.Spline36(width=w_dec)]
                    )

            elif direction in [Direction.UP, Direction.DOWN]:
                h_inc = math.floor(scale * clipa.width)
                h_dec = clipa.width - h_inc

                if h_inc == 0:
                    return clipa_t_zone

                if direction == Direction.UP:
                    return core.std.StackVertical(
                        [clipa_t_zone.resize.Spline36(width=h_dec), clipb_t_zone.resize.Spline36(width=h_inc)]
                    )
                elif direction == Direction.RIGHT:
                    return core.std.StackVertical(
                        [clipb_t_zone.resize.Spline36(width=h_inc), clipa_t_zone.resize.Spline36(width=h_dec)]
                    )

        squeeze_expanded = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _squeeze_expand)

        return _return_combo(clipa_clean, squeeze_expanded, clipb_clean)


def push(clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT):
    """Second clip pushes first clip off of the screen.

    The first clip moves off of the screen moving towards the given `direction`.

    Alias for :func:`linear_boundary` with ``clipa_movement=SLIDE`` and ``clipb_movement=SLIDE``.
    """
    return linear_boundary(clipa, clipb, MiscConstants.SLIDE, MiscConstants.SLIDE, frames=frames, direction=direction)


def slide_expand(
    clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT
):
    """First clip slides out of view, while second clip expands into view from nothing.

    `clipa` slides off of the screen towards `direction`.
    `clipb` expands into view from the opposite side of the given direction.

    Alias for :func:`linear_boundary` with ``clipa_movement=SLIDE`` and ``clipb_movement=EXPAND``.
    """
    return linear_boundary(clipa, clipb, MiscConstants.SLIDE, MiscConstants.EXPAND, frames=frames, direction=direction)


def squeeze_slide(
    clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT
):
    """First clip squeezes into nothing, while second clip slides into view.

    `clipa` gets compressed off of the screen towards `direction`.
    `clipb` slides into view from the opposite side of the given direction.

    Alias for :func:`linear_boundary` with ``clipa_movement=SQUEEZE`` and ``clipb_movement=SLIDE``.
    """
    return linear_boundary(clipa, clipb, MiscConstants.SQUEEZE, MiscConstants.SLIDE, frames=frames, direction=direction)


def squeeze_expand(
    clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT
):
    """First clip squeezes into nothing, while second clip expands into view from nothing.

    `clipa` gets compressed off of the screen towards `direction`.
    `clipb` expands into view from the opposite side of the given direction.

    Alias for :func:`linear_boundary` with ``clipa_movement=SQUEEZE`` and ``clipb_movement=EXPAND``.
    """
    return linear_boundary(
        clipa, clipb, MiscConstants.SQUEEZE, MiscConstants.EXPAND, frames=frames, direction=direction
    )


def cover(
    clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT
) -> vs.VideoNode:
    """Second clip slides in and covers the first clip which stays in place.

    `clipb` slides into frame towards `direction` covering `clipa`.
    """
    if direction not in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        raise ValueError("cover: give a proper direction")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, cover, clipa, clipb)
    clipa_clean, clipb_clean, clipa_t_zone, clipb_t_zone = _transition_clips(clipa, clipb, frames_)

    def _cover(n: int) -> vs.VideoNode:
        progress = Fraction(n, frames_ - 1)
        w = math.floor(progress * clipa.width)
        h = math.floor(progress * clipa.height)

        if progress == 0:
            return clipa_t_zone
        elif progress == 1:
            return clipb_t_zone

        if w == 0 or h == 0:
            return clipa_t_zone

        if direction == Direction.LEFT:
            cropped_a = clipa_t_zone.std.Crop(right=w)
            stack = core.std.StackHorizontal([cropped_a, clipb_t_zone])
            return stack.resize.Spline36(width=clipa.width, src_width=clipa.width)
        elif direction == Direction.RIGHT:
            cropped_a = clipa_t_zone.std.Crop(left=w)
            stack = core.std.StackHorizontal([clipb_t_zone, cropped_a])
            return stack.resize.Spline36(width=clipa.width, src_left=clipa.width - w, src_width=clipa.width)
        elif direction == Direction.UP:
            cropped_a = clipa_t_zone.std.Crop(bottom=h)
            stack = core.std.StackVertical([cropped_a, clipb_t_zone])
            return stack.resize.Spline36(height=clipa.height, src_height=clipa.height)
        elif direction == Direction.DOWN:
            cropped_a = clipa_t_zone.std.Crop(top=h)
            stack = core.std.StackVertical([clipb_t_zone, cropped_a])
            return stack.resize.Spline36(height=clipa.height, src_top=clipa.height - h, src_height=clipa.height)

    covered = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _cover)

    return _return_combo(clipa_clean, covered, clipb_clean)


def reveal(
    clipa: vs.VideoNode, clipb: vs.VideoNode, frames: Optional[int] = None, direction: Direction = Direction.LEFT
) -> vs.VideoNode:
    """First clip slides out of view exposing second clip that stays in place.

    `clipa` slides out of frame towards `direction` revealing `clipb`.
    """
    if direction not in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
        raise ValueError("reveal: give a proper direction")
    frames_ = frames or min(clipa.num_frames, clipb.num_frames)
    if TYPE_CHECKING:
        assert isinstance(frames_, int)
    _check_clips(frames_, reveal, clipa, clipb)
    clipa_clean, clipb_clean, clipa_t_zone, clipb_t_zone = _transition_clips(clipa, clipb, frames_)

    def _reveal(n: int) -> vs.VideoNode:
        progress = 1 - Fraction(n, frames_ - 1)
        w = math.floor(progress * clipa.width)
        h = math.floor(progress * clipa.height)

        if progress == 1:
            return clipa_t_zone
        elif progress == 0:
            return clipb_t_zone

        if w == 0 or h == 0:
            return clipb_t_zone

        if direction == Direction.LEFT:
            cropped_b = clipb_t_zone.std.Crop(left=w)
            stack = core.std.StackHorizontal([clipa_t_zone, cropped_b])
            return stack.resize.Spline36(width=clipa.width, src_width=clipa.width, src_left=clipa.width - w)
        elif direction == Direction.RIGHT:
            cropped_b = clipb_t_zone.std.Crop(right=w)
            stack = core.std.StackHorizontal([cropped_b, clipa_t_zone])
            return stack.resize.Spline36(width=clipa.width, src_width=clipa.width)
        elif direction == Direction.UP:
            cropped_b = clipb_t_zone.std.Crop(top=h)
            stack = core.std.StackVertical([clipa_t_zone, cropped_b])
            return stack.resize.Spline36(height=clipa.height, src_height=clipa.height, src_top=clipa.height - h)
        elif direction == Direction.DOWN:
            cropped_b = clipb_t_zone.std.Crop(bottom=h)
            stack = core.std.StackVertical([cropped_b, clipa_t_zone])
            return stack.resize.Spline36(height=clipa.height, src_height=clipa.height)

    covered = core.std.FrameEval(core.std.BlankClip(clipa, length=frames_), _reveal)

    return _return_combo(clipa_clean, covered, clipb_clean)
