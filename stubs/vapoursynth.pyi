# Stop pep8 from complaining (hopefully)
# NOQA

# Ignore Flake Warnings
# flake8: noqa

# Ignore coverage
# (No coverage)

# From https://gist.github.com/pylover/7870c235867cf22817ac5b096defb768
# noinspection PyPep8
# noinspection PyPep8Naming
# noinspection PyTypeChecker
# noinspection PyAbstractClass
# noinspection PyArgumentEqualDefault
# noinspection PyArgumentList
# noinspection PyAssignmentToLoopOrWithParameter
# noinspection PyAttributeOutsideInit
# noinspection PyAugmentAssignment
# noinspection PyBroadException
# noinspection PyByteLiteral
# noinspection PyCallByClass
# noinspection PyChainedComparsons
# noinspection PyClassHasNoInit
# noinspection PyClassicStyleClass
# noinspection PyComparisonWithNone
# noinspection PyCompatibility
# noinspection PyDecorator
# noinspection PyDefaultArgument
# noinspection PyDictCreation
# noinspection PyDictDuplicateKeys
# noinspection PyDocstringTypes
# noinspection PyExceptClausesOrder
# noinspection PyExceptionInheritance
# noinspection PyFromFutureImport
# noinspection PyGlobalUndefined
# noinspection PyIncorrectDocstring
# noinspection PyInitNewSignature
# noinspection PyInterpreter
# noinspection PyListCreation
# noinspection PyMandatoryEncoding
# noinspection PyMethodFirstArgAssignment
# noinspection PyMethodMayBeStatic
# noinspection PyMethodOverriding
# noinspection PyMethodParameters
# noinspection PyMissingConstructor
# noinspection PyMissingOrEmptyDocstring
# noinspection PyNestedDecorators
# noinspection PynonAsciiChar
# noinspection PyNoneFunctionAssignment
# noinspection PyOldStyleClasses
# noinspection PyPackageRequirements
# noinspection PyPropertyAccess
# noinspection PyPropertyDefinition
# noinspection PyProtectedMember
# noinspection PyRaisingNewStyleClass
# noinspection PyRedeclaration
# noinspection PyRedundantParentheses
# noinspection PySetFunctionToLiteral
# noinspection PySimplifyBooleanCheck
# noinspection PySingleQuotedDocstring
# noinspection PyStatementEffect
# noinspection PyStringException
# noinspection PyStringFormat
# noinspection PySuperArguments
# noinspection PyTrailingSemicolon
# noinspection PyTupleAssignmentBalance
# noinspection PyTupleItemAssignment
# noinspection PyUnboundLocalVariable
# noinspection PyUnnecessaryBackslash
# noinspection PyUnreachableCode
# noinspection PyUnresolvedReferences
# noinspection PyUnusedLocal
# noinspection ReturnValueFromInit

import ctypes
import fractions
import types
import typing

T = typing.TypeVar("T")
SingleAndSequence = typing.Union[T, typing.Sequence[T]]

###
# ENUMS AND CONSTANTS
class ColorFamily(int):
    name: str
    value: int

    GRAY: typing.ClassVar['ColorFamily']
    RGB: typing.ClassVar['ColorFamily']
    YUV: typing.ClassVar['ColorFamily']
    YCOCG: typing.ClassVar['ColorFamily']
    COMPAT: typing.ClassVar['ColorFamily']

GRAY: ColorFamily
RGB: ColorFamily
YUV: ColorFamily
YCOCG: ColorFamily
COMPAT: ColorFamily


class SampleType(int):
    name: str
    value: int

    INTEGER: typing.ClassVar['SampleType']
    FLOAT: typing.ClassVar['SampleType']


INTEGER: SampleType
FLOAT: SampleType


class PresetFormat(int):
    name: str
    value: int

    NONE: typing.ClassVar['PresetFormat']

    GRAY8: typing.ClassVar['PresetFormat']
    GRAY16: typing.ClassVar['PresetFormat']

    GRAYH: typing.ClassVar['PresetFormat']
    GRAYS: typing.ClassVar['PresetFormat']

    YUV420P8: typing.ClassVar['PresetFormat']
    YUV422P8: typing.ClassVar['PresetFormat']
    YUV444P8: typing.ClassVar['PresetFormat']
    YUV410P8: typing.ClassVar['PresetFormat']
    YUV411P8: typing.ClassVar['PresetFormat']
    YUV440P8: typing.ClassVar['PresetFormat']

    YUV420P9: typing.ClassVar['PresetFormat']
    YUV422P9: typing.ClassVar['PresetFormat']
    YUV444P9: typing.ClassVar['PresetFormat']

    YUV420P10: typing.ClassVar['PresetFormat']
    YUV422P10: typing.ClassVar['PresetFormat']
    YUV444P10: typing.ClassVar['PresetFormat']

    YUV420P12: typing.ClassVar['PresetFormat']
    YUV422P12: typing.ClassVar['PresetFormat']
    YUV444P12: typing.ClassVar['PresetFormat']

    YUV420P14: typing.ClassVar['PresetFormat']
    YUV422P14: typing.ClassVar['PresetFormat']
    YUV444P14: typing.ClassVar['PresetFormat']

    YUV420P16: typing.ClassVar['PresetFormat']
    YUV422P16: typing.ClassVar['PresetFormat']
    YUV444P16: typing.ClassVar['PresetFormat']

    YUV444PH: typing.ClassVar['PresetFormat']
    YUV444PS: typing.ClassVar['PresetFormat']

    RGB24: typing.ClassVar['PresetFormat']
    RGB27: typing.ClassVar['PresetFormat']
    RGB30: typing.ClassVar['PresetFormat']
    RGB48: typing.ClassVar['PresetFormat']

    RGBH: typing.ClassVar['PresetFormat']
    RGBS: typing.ClassVar['PresetFormat']

    COMPATBGR32: typing.ClassVar['PresetFormat']
    COMPATYUY2: typing.ClassVar['PresetFormat']


NONE: PresetFormat

GRAY8: PresetFormat
GRAY16: PresetFormat

GRAYH: PresetFormat
GRAYS: PresetFormat

YUV420P8: PresetFormat
YUV422P8: PresetFormat
YUV444P8: PresetFormat
YUV410P8: PresetFormat
YUV411P8: PresetFormat
YUV440P8: PresetFormat

YUV420P9: PresetFormat
YUV422P9: PresetFormat
YUV444P9: PresetFormat

YUV420P10: PresetFormat
YUV422P10: PresetFormat
YUV444P10: PresetFormat

YUV420P12: PresetFormat
YUV422P12: PresetFormat
YUV444P12: PresetFormat

YUV420P14: PresetFormat
YUV422P14: PresetFormat
YUV444P14: PresetFormat

YUV420P16: PresetFormat
YUV422P16: PresetFormat
YUV444P16: PresetFormat

YUV444PH: PresetFormat
YUV444PS: PresetFormat

RGB24: PresetFormat
RGB27: PresetFormat
RGB30: PresetFormat
RGB48: PresetFormat

RGBH: PresetFormat
RGBS: PresetFormat

COMPATBGR32: PresetFormat
COMPATYUY2: PresetFormat


###
# VapourSynth Environment SubSystem

class EnvironmentData:
    """
    Contains the data VapourSynth stores for a specific environment.
    """


class Environment:
    alive: bool
    single: bool
    env_id: int
    active: bool

    def copy(self) -> Environment: ...
    def use(self) -> typing.ContextManager[None]: ...

    def __enter__(self) -> Environment: ...
    def __exit__(self, ty: typing.Type[BaseException], tv: BaseException, tb: types.TracebackType) -> None: ...

class EnvironmentPolicyAPI:
    def wrap_environment(self, environment_data: EnvironmentData) -> Environment: ...
    def create_environment(self) -> EnvironmentData: ...
    def unregister_policy(self) -> None: ...

class EnvironmentPolicy:
    def on_policy_registered(self, special_api: EnvironmentPolicyAPI) -> None: ...
    def on_policy_cleared(self) -> None: ...
    def get_current_environment(self) -> typing.Optional[EnvironmentData]: ...
    def set_environment(self, environment: typing.Optional[EnvironmentData]) -> None: ...
    def is_active(self, environment: EnvironmentData) -> bool: ...


_using_vsscript: bool


def register_policy(policy: EnvironmentPolicy) -> None: ...
def has_policy() -> bool: ...

def vpy_current_environment() -> Environment: ...
def get_current_environment() -> Environment: ...


class AlphaOutputTuple(typing.NamedTuple):
    clip: 'VideoNode'
    alpha: 'VideoNode'

Func = typing.Callable[..., typing.Any]

class Error(Exception): ...

def set_message_handler(handler_func: typing.Callable[[int, str], None]) -> None: ...
def clear_output(index: int = 0) -> None: ...
def clear_outputs() -> None: ...
def get_outputs() -> typing.Mapping[int, typing.Union['VideoNode', AlphaOutputTuple]]: ...
def get_output(index: int = 0) -> typing.Union['VideoNode', AlphaOutputTuple]: ...


class Format:
    id: int
    name: str
    color_family: ColorFamily
    sample_type: SampleType
    bits_per_sample: int
    bytes_per_sample: int
    subsampling_w: int
    subsampling_h: int
    num_planes: int

    def _as_dict(self) -> typing.Dict[str, typing.Any]: ...
    def replace(self, *,
                color_family: typing.Optional[ColorFamily] = None,
                sample_type: typing.Optional[SampleType] = None,
                bits_per_sample: typing.Optional[int] = None,
                subsampling_w: typing.Optional[int] = None,
                subsampling_h: typing.Optional[int] = None
                ) -> 'Format': ...


_VideoPropsValue = typing.Union[
    SingleAndSequence[int],
    SingleAndSequence[float],
    SingleAndSequence[str],
    SingleAndSequence['VideoNode'],
    SingleAndSequence['VideoFrame'],
    SingleAndSequence[typing.Callable[..., typing.Any]]
]

class VideoProps(typing.MutableMapping[str, _VideoPropsValue]):
    def __getattr__(self, name: str) -> _VideoPropsValue: ...
    def __setattr__(self, name: str, value: _VideoPropsValue) -> None: ...

    # mypy lo vult.
    # In all seriousness, why do I need to manually define them in a typestub?
    def __delitem__(self, name: str) -> None: ...
    def __setitem__(self, name: str, value: _VideoPropsValue) -> None: ...
    def __getitem__(self, name: str) -> _VideoPropsValue: ...
    def __iter__(self) -> typing.Iterator[str]: ...
    def __len__(self) -> int: ...

class VideoPlane:
    width: int
    height: int


class VideoFrame:
    props: VideoProps
    height: int
    width: int
    format: Format
    readonly: bool

    def copy(self) -> 'VideoFrame': ...

    def get_read_ptr(self, plane: int) -> ctypes.c_void_p: ...
    def get_read_array(self, plane: int) -> typing.Optional[memoryview]: ...
    def get_write_ptr(self, plane: int) -> ctypes.c_void_p: ...
    def get_write_array(self, plane: int) -> typing.Optional[memoryview]: ...

    def get_stride(self, plane: int) -> int: ...
    def planes(self) -> typing.Iterator['VideoPlane']: ...


class _Future(typing.Generic[T]):
    def set_result(self, value: T) -> None: ...
    def set_exception(self, exception: BaseException) -> None: ...
    def result(self) -> T: ...
    def exception(self) -> typing.Optional[typing.NoReturn]: ...


class Plugin:
    namespace: str

    def get_functions(self) -> typing.Dict[str, str]: ...
    def list_functions(self) -> str: ...


class _Plugin_vinverse_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Vinverse(self, clip: "VideoNode", sstr: typing.Union[float, None] = None, amnt: typing.Union[int, None] = None, scl: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_nnedi3_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, clip: "VideoNode", field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, int16_prescreener: typing.Union[int, None] = None, int16_predictor: typing.Union[int, None] = None, exp: typing.Union[int, None] = None, show_mask: typing.Union[int, None] = None, combed_only: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_rdvs_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DupBlocks(self, input: "VideoNode", gmthreshold: typing.Union[int, None] = None, mthreshold: typing.Union[int, None] = None, noise: typing.Union[int, None] = None, noisy: typing.Union[int, None] = None, dist: typing.Union[int, None] = None, tolerance: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, pthreshold: typing.Union[int, None] = None, cthreshold: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...
    def RestoreMotionBlocks(self, input: "VideoNode", restore: "VideoNode", neighbour: typing.Union["VideoNode", None] = None, neighbour2: typing.Union["VideoNode", None] = None, alternative: typing.Union["VideoNode", None] = None, gmthreshold: typing.Union[int, None] = None, mthreshold: typing.Union[int, None] = None, noise: typing.Union[int, None] = None, noisy: typing.Union[int, None] = None, dist: typing.Union[int, None] = None, tolerance: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, pthreshold: typing.Union[int, None] = None, cthreshold: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCSelect(self, input: "VideoNode", sceneBegin: "VideoNode", sceneEnd: "VideoNode", globalMotion: "VideoNode", dfactor: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_focus_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalSoften(self, clip: "VideoNode", radius: typing.Union[int, None] = None, luma_threshold: typing.Union[int, None] = None, chroma_threshold: typing.Union[int, None] = None, scenechange: typing.Union[int, None] = None, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_grain_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Add(self, clip: "VideoNode", var: typing.Union[float, None] = None, uvar: typing.Union[float, None] = None, hcorr: typing.Union[float, None] = None, vcorr: typing.Union[float, None] = None, seed: typing.Union[int, None] = None, constant: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_ctmf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def CTMF(self, clip: "VideoNode", radius: typing.Union[int, None] = None, memsize: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_dctf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DCTFilter(self, clip: "VideoNode", factors: typing.Sequence[float], planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_deblock_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Deblock(self, clip: "VideoNode", quant: typing.Union[int, None] = None, aoffset: typing.Union[int, None] = None, boffset: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_dfttest_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DFTTest(self, clip: "VideoNode", ftype: typing.Union[int, None] = None, sigma: typing.Union[float, None] = None, sigma2: typing.Union[float, None] = None, pmin: typing.Union[float, None] = None, pmax: typing.Union[float, None] = None, sbsize: typing.Union[int, None] = None, smode: typing.Union[int, None] = None, sosize: typing.Union[int, None] = None, tbsize: typing.Union[int, None] = None, tmode: typing.Union[int, None] = None, tosize: typing.Union[int, None] = None, swin: typing.Union[int, None] = None, twin: typing.Union[int, None] = None, sbeta: typing.Union[float, None] = None, tbeta: typing.Union[float, None] = None, zmean: typing.Union[int, None] = None, f0beta: typing.Union[float, None] = None, nlocation: typing.Union[typing.Sequence[int], None] = None, alpha: typing.Union[float, None] = None, slocation: typing.Union[typing.Sequence[float], None] = None, ssx: typing.Union[typing.Sequence[float], None] = None, ssy: typing.Union[typing.Sequence[float], None] = None, sst: typing.Union[typing.Sequence[float], None] = None, ssystem: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_eedi2_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def EEDI2(self, clip: "VideoNode", field: int, mthresh: typing.Union[int, None] = None, lthresh: typing.Union[int, None] = None, vthresh: typing.Union[int, None] = None, estr: typing.Union[int, None] = None, dstr: typing.Union[int, None] = None, maxd: typing.Union[int, None] = None, map: typing.Union[int, None] = None, nt: typing.Union[int, None] = None, pp: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_mpls_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, bd_path: typing.Union[str, bytes, bytearray], playlist: int, angle: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_morpho_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BottomHat(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Close(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Dilate(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Erode(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Open(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def TopHat(self, clip: "VideoNode", size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tdm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def IsCombed(self, clip: "VideoNode", cthresh: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, mi: typing.Union[int, None] = None, metric: typing.Union[int, None] = None) -> "VideoNode": ...
    def TDeintMod(self, clip: "VideoNode", order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, length: typing.Union[int, None] = None, mtype: typing.Union[int, None] = None, ttype: typing.Union[int, None] = None, mtql: typing.Union[int, None] = None, mthl: typing.Union[int, None] = None, mtqc: typing.Union[int, None] = None, mthc: typing.Union[int, None] = None, nt: typing.Union[int, None] = None, minthresh: typing.Union[int, None] = None, maxthresh: typing.Union[int, None] = None, cstr: typing.Union[int, None] = None, athresh: typing.Union[int, None] = None, metric: typing.Union[int, None] = None, expand: typing.Union[int, None] = None, link: typing.Union[int, None] = None, show: typing.Union[int, None] = None, edeint: typing.Union["VideoNode", None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_ttmpsm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TTempSmooth(self, clip: "VideoNode", maxr: typing.Union[int, None] = None, thresh: typing.Union[typing.Sequence[int], None] = None, mdiff: typing.Union[typing.Sequence[int], None] = None, strength: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None, fp: typing.Union[int, None] = None, pfclip: typing.Union["VideoNode", None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vd_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VagueDenoiser(self, clip: "VideoNode", threshold: typing.Union[float, None] = None, method: typing.Union[int, None] = None, nsteps: typing.Union[int, None] = None, percent: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vmaf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VMAF(self, reference: "VideoNode", distorted: "VideoNode", model: typing.Union[int, None] = None, log_path: typing.Union[str, bytes, bytearray, None] = None, log_fmt: typing.Union[int, None] = None, ssim: typing.Union[int, None] = None, ms_ssim: typing.Union[int, None] = None, pool: typing.Union[int, None] = None, ci: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_w3fdif_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def W3FDIF(self, clip: "VideoNode", order: int, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_yadifmod_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Yadifmod(self, clip: "VideoNode", edeint: "VideoNode", order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_noisegen_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Generate(self, clip: "VideoNode", str: typing.Union[float, None] = None, limit: typing.Union[float, None] = None, type: typing.Union[int, None] = None, mean: typing.Union[float, None] = None, var: typing.Union[float, None] = None, dyn: typing.Union[int, None] = None, full: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_rf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Replace(self, clip: "VideoNode", clips: typing.Sequence["VideoNode"], intervals: typing.Sequence[typing.Union[str, bytes, bytearray]]) -> "VideoNode": ...


class _Plugin_sangnom_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SangNom(self, clip: "VideoNode", order: typing.Union[int, None] = None, dh: typing.Union[int, None] = None, aa: typing.Union[typing.Sequence[int], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_warp_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ABlur(self, clip: "VideoNode", blur: typing.Union[int, None] = None, type: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def ASobel(self, clip: "VideoNode", thresh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def AWarp(self, clip: "VideoNode", mask: "VideoNode", depth: typing.Union[typing.Sequence[int], None] = None, chroma: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def AWarpSharp2(self, clip: "VideoNode", thresh: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, type: typing.Union[int, None] = None, depth: typing.Union[typing.Sequence[int], None] = None, chroma: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_sub_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ImageFile(self, clip: "VideoNode", file: typing.Union[str, bytes, bytearray], id: typing.Union[int, None] = None, palette: typing.Union[typing.Sequence[int], None] = None, gray: typing.Union[int, None] = None, info: typing.Union[int, None] = None, flatten: typing.Union[int, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Subtitle(self, clip: "VideoNode", text: typing.Union[str, bytes, bytearray], start: typing.Union[int, None] = None, end: typing.Union[int, None] = None, debuglevel: typing.Union[int, None] = None, fontdir: typing.Union[str, bytes, bytearray, None] = None, linespacing: typing.Union[float, None] = None, margins: typing.Union[typing.Sequence[int], None] = None, sar: typing.Union[float, None] = None, style: typing.Union[str, bytes, bytearray, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def TextFile(self, clip: "VideoNode", file: typing.Union[str, bytes, bytearray], charset: typing.Union[str, bytes, bytearray, None] = None, scale: typing.Union[float, None] = None, debuglevel: typing.Union[int, None] = None, fontdir: typing.Union[str, bytes, bytearray, None] = None, linespacing: typing.Union[float, None] = None, margins: typing.Union[typing.Sequence[int], None] = None, sar: typing.Union[float, None] = None, style: typing.Union[str, bytes, bytearray, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_flux_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothST(self, clip: "VideoNode", temporal_threshold: typing.Union[int, None] = None, spatial_threshold: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def SmoothT(self, clip: "VideoNode", temporal_threshold: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_hist_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Classic(self, clip: "VideoNode") -> "VideoNode": ...
    def Color(self, clip: "VideoNode") -> "VideoNode": ...
    def Color2(self, clip: "VideoNode") -> "VideoNode": ...
    def Levels(self, clip: "VideoNode", factor: typing.Union[float, None] = None) -> "VideoNode": ...
    def Luma(self, clip: "VideoNode") -> "VideoNode": ...


class _Plugin_median_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Median(self, clips: typing.Sequence["VideoNode"], sync: typing.Union[int, None] = None, samples: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MedianBlend(self, clips: typing.Sequence["VideoNode"], low: typing.Union[int, None] = None, high: typing.Union[int, None] = None, closest: typing.Union[int, None] = None, sync: typing.Union[int, None] = None, samples: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def TemporalMedian(self, clip: "VideoNode", radius: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_msmoosh_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSharpen(self, clip: "VideoNode", threshold: typing.Union[float, None] = None, strength: typing.Union[float, None] = None, mask: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MSmooth(self, clip: "VideoNode", threshold: typing.Union[float, None] = None, strength: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_mvsf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Analyse(self, super: "VideoNode", blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[float, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[float, None] = None, badrange: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def Analyze(self, super: "VideoNode", blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[float, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[float, None] = None, badrange: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def BlockFPS(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Compensate(self, clip: "VideoNode", super: "VideoNode", vectors: "VideoNode", scbehavior: typing.Union[int, None] = None, thsad: typing.Union[float, None] = None, fields: typing.Union[int, None] = None, time: typing.Union[float, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain1(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain10(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain11(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain12(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain13(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain14(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain15(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain16(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain17(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain18(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain19(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain2(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain20(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain21(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain22(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain23(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", mvbw23: "VideoNode", mvfw23: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain24(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", mvbw23: "VideoNode", mvfw23: "VideoNode", mvbw24: "VideoNode", mvfw24: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain3(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain4(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain5(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain6(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain7(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain8(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain9(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Finest(self, super: "VideoNode") -> "VideoNode": ...
    def Flow(self, clip: "VideoNode", super: "VideoNode", vectors: "VideoNode", time: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowBlur(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", blur: typing.Union[float, None] = None, prec: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def FlowFPS(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def FlowInter(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", time: typing.Union[float, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Mask(self, clip: "VideoNode", vectors: "VideoNode", ml: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, kind: typing.Union[int, None] = None, time: typing.Union[float, None] = None, ysc: typing.Union[float, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Recalculate(self, super: "VideoNode", vectors: "VideoNode", thsad: typing.Union[float, None] = None, smooth: typing.Union[int, None] = None, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCDetection(self, clip: "VideoNode", vectors: "VideoNode", thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Super(self, clip: "VideoNode", hpad: typing.Union[int, None] = None, vpad: typing.Union[int, None] = None, pel: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, sharp: typing.Union[int, None] = None, rfilter: typing.Union[int, None] = None, pelclip: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_mv_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Analyse(self, super: "VideoNode", blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[int, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[int, None] = None, badrange: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def BlockFPS(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Compensate(self, clip: "VideoNode", super: "VideoNode", vectors: "VideoNode", scbehavior: typing.Union[int, None] = None, thsad: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, time: typing.Union[float, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain1(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain2(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain3(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanAnalyse(self, clip: "VideoNode", vectors: "VideoNode", mask: typing.Union["VideoNode", None] = None, zoom: typing.Union[int, None] = None, rot: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, error: typing.Union[float, None] = None, info: typing.Union[int, None] = None, wrong: typing.Union[float, None] = None, zerow: typing.Union[float, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanCompensate(self, clip: "VideoNode", data: "VideoNode", offset: typing.Union[float, None] = None, subpixel: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, matchfields: typing.Union[int, None] = None, mirror: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, info: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanEstimate(self, clip: "VideoNode", trust: typing.Union[float, None] = None, winx: typing.Union[int, None] = None, winy: typing.Union[int, None] = None, wleft: typing.Union[int, None] = None, wtop: typing.Union[int, None] = None, dxmax: typing.Union[int, None] = None, dymax: typing.Union[int, None] = None, zoommax: typing.Union[float, None] = None, stab: typing.Union[float, None] = None, pixaspect: typing.Union[float, None] = None, info: typing.Union[int, None] = None, show: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanStabilise(self, clip: "VideoNode", data: "VideoNode", cutoff: typing.Union[float, None] = None, damping: typing.Union[float, None] = None, initzoom: typing.Union[float, None] = None, addzoom: typing.Union[int, None] = None, prev: typing.Union[int, None] = None, next: typing.Union[int, None] = None, mirror: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, dxmax: typing.Union[float, None] = None, dymax: typing.Union[float, None] = None, zoommax: typing.Union[float, None] = None, rotmax: typing.Union[float, None] = None, subpixel: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, fitlast: typing.Union[int, None] = None, tzoom: typing.Union[float, None] = None, info: typing.Union[int, None] = None, method: typing.Union[int, None] = None, fields: typing.Union[int, None] = None) -> "VideoNode": ...
    def Finest(self, super: "VideoNode", opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Flow(self, clip: "VideoNode", super: "VideoNode", vectors: "VideoNode", time: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowBlur(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", blur: typing.Union[float, None] = None, prec: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowFPS(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowInter(self, clip: "VideoNode", super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", time: typing.Union[float, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Mask(self, clip: "VideoNode", vectors: "VideoNode", ml: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, kind: typing.Union[int, None] = None, time: typing.Union[float, None] = None, ysc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Recalculate(self, super: "VideoNode", vectors: "VideoNode", thsad: typing.Union[int, None] = None, smooth: typing.Union[int, None] = None, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, lambda_: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCDetection(self, clip: "VideoNode", vectors: "VideoNode", thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None) -> "VideoNode": ...
    def Super(self, clip: "VideoNode", hpad: typing.Union[int, None] = None, vpad: typing.Union[int, None] = None, pel: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, sharp: typing.Union[int, None] = None, rfilter: typing.Union[int, None] = None, pelclip: typing.Union["VideoNode", None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_scxvid_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Scxvid(self, clip: "VideoNode", log: typing.Union[str, bytes, bytearray, None] = None, use_slices: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_smoothuv_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothUV(self, clip: "VideoNode", radius: typing.Union[int, None] = None, threshold: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_ssiq_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SSIQ(self, clip: "VideoNode", diameter: typing.Union[int, None] = None, strength: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tbilateral_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TBilateral(self, clip: "VideoNode", ppclip: typing.Union["VideoNode", None] = None, diameter: typing.Union[typing.Sequence[int], None] = None, sdev: typing.Union[typing.Sequence[float], None] = None, idev: typing.Union[typing.Sequence[float], None] = None, cs: typing.Union[typing.Sequence[float], None] = None, d2: typing.Union[int, None] = None, kerns: typing.Union[int, None] = None, kerni: typing.Union[int, None] = None, restype: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_remap_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def RemapFrames(self, baseclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, sourceclip: typing.Union["VideoNode", None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def RemapFramesSimple(self, clip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Remf(self, baseclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, sourceclip: typing.Union["VideoNode", None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def Remfs(self, clip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def ReplaceFramesSimple(self, baseclip: "VideoNode", sourceclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def Rfs(self, baseclip: "VideoNode", sourceclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tcomb_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TComb(self, clip: "VideoNode", mode: typing.Union[int, None] = None, fthreshl: typing.Union[int, None] = None, fthreshc: typing.Union[int, None] = None, othreshl: typing.Union[int, None] = None, othreshc: typing.Union[int, None] = None, map: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_tedgemask_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TEdgeMask(self, clip: "VideoNode", threshold: typing.Union[typing.Sequence[float], None] = None, type: typing.Union[int, None] = None, link: typing.Union[int, None] = None, scale: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tmedian_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalMedian(self, clip: "VideoNode", radius: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vscope_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Scope(self, clip: "VideoNode", mode: typing.Union[str, bytes, bytearray, None] = None, tickmarks: typing.Union[int, None] = None, side: typing.Union[str, bytes, bytearray, None] = None, bottom: typing.Union[str, bytes, bytearray, None] = None, corner: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_wwxd_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def WWXD(self, clip: "VideoNode") -> "VideoNode": ...


class _Plugin_svp2_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothFps(self, clip: "VideoNode", super: "VideoNode", sdata: int, vectors: "VideoNode", vdata: int, opt: typing.Union[str, bytes, bytearray], src: typing.Union["VideoNode", None] = None, fps: typing.Union[float, None] = None) -> "VideoNode": ...
    def SmoothFps_NVOF(self, clip: "VideoNode", opt: typing.Union[str, bytes, bytearray], nvof_src: typing.Union["VideoNode", None] = None, src: typing.Union["VideoNode", None] = None, fps: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_surfaceblur_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def surfaceblur(self, input: "VideoNode", threshold: typing.Union[float, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_bm3d_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Basic(self, input: "VideoNode", ref: typing.Union["VideoNode", None] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, hard_thr: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def Final(self, input: "VideoNode", ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def OPP2RGB(self, input: "VideoNode", sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def RGB2OPP(self, input: "VideoNode", sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def VAggregate(self, input: "VideoNode", radius: typing.Union[int, None] = None, sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def VBasic(self, input: "VideoNode", ref: typing.Union["VideoNode", None] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, radius: typing.Union[int, None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, ps_num: typing.Union[int, None] = None, ps_range: typing.Union[int, None] = None, ps_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, hard_thr: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def VFinal(self, input: "VideoNode", ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, radius: typing.Union[int, None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, ps_num: typing.Union[int, None] = None, ps_range: typing.Union[int, None] = None, ps_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_eedi3_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def eedi3(self, clip: "VideoNode", field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, alpha: typing.Union[float, None] = None, beta: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, nrad: typing.Union[int, None] = None, mdis: typing.Union[int, None] = None, hp: typing.Union[int, None] = None, ucubic: typing.Union[int, None] = None, cost3: typing.Union[int, None] = None, vcheck: typing.Union[int, None] = None, vthresh0: typing.Union[float, None] = None, vthresh1: typing.Union[float, None] = None, vthresh2: typing.Union[float, None] = None, sclip: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_ffms2_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def GetLogLevel(self) -> "VideoNode": ...
    def Index(self, source: typing.Union[str, bytes, bytearray], cachefile: typing.Union[str, bytes, bytearray, None] = None, indextracks: typing.Union[typing.Sequence[int], None] = None, errorhandling: typing.Union[int, None] = None, overwrite: typing.Union[int, None] = None) -> "VideoNode": ...
    def SetLogLevel(self, level: int) -> "VideoNode": ...
    def Source(self, source: typing.Union[str, bytes, bytearray], track: typing.Union[int, None] = None, cache: typing.Union[int, None] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, threads: typing.Union[int, None] = None, timecodes: typing.Union[str, bytes, bytearray, None] = None, seekmode: typing.Union[int, None] = None, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, resizer: typing.Union[str, bytes, bytearray, None] = None, format: typing.Union[int, None] = None, alpha: typing.Union[int, None] = None) -> "VideoNode": ...
    def Version(self) -> "VideoNode": ...


class _Plugin_vfrtocfr_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VFRToCFR(self, clip: "VideoNode", timecodes: typing.Union[str, bytes, bytearray], fpsnum: int, fpsden: int, drop: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_hqdn3d_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Hqdn3d(self, clip: "VideoNode", lum_spac: typing.Union[float, None] = None, chrom_spac: typing.Union[float, None] = None, lum_tmp: typing.Union[float, None] = None, chrom_tmp: typing.Union[float, None] = None, restart_lap: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_imwri_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, filename: typing.Sequence[typing.Union[str, bytes, bytearray]], firstnum: typing.Union[int, None] = None, mismatch: typing.Union[int, None] = None, alpha: typing.Union[int, None] = None, float_output: typing.Union[int, None] = None) -> "VideoNode": ...
    def Write(self, clip: "VideoNode", imgformat: typing.Union[str, bytes, bytearray], filename: typing.Union[str, bytes, bytearray], firstnum: typing.Union[int, None] = None, quality: typing.Union[int, None] = None, dither: typing.Union[int, None] = None, compression_type: typing.Union[str, bytes, bytearray, None] = None, overwrite: typing.Union[int, None] = None, alpha: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_misc_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AverageFrames(self, clips: typing.Sequence["VideoNode"], weights: typing.Sequence[float], scale: typing.Union[float, None] = None, scenechange: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Hysteresis(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def SCDetect(self, clip: "VideoNode", threshold: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_rgvs_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, clip: "VideoNode", previous: typing.Union["VideoNode", None] = None, next: typing.Union["VideoNode", None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, clip: "VideoNode", mode: typing.Sequence[int]) -> "VideoNode": ...
    def Repair(self, clip: "VideoNode", repairclip: "VideoNode", mode: typing.Sequence[int]) -> "VideoNode": ...
    def VerticalCleaner(self, clip: "VideoNode", mode: typing.Sequence[int]) -> "VideoNode": ...


class _Plugin_resize_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bicubic(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Bilinear(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Lanczos(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Point(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline16(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline36(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline64(self, clip: "VideoNode", width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_retinex_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSRCP(self, input: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, chroma_protect: typing.Union[float, None] = None) -> "VideoNode": ...
    def MSRCR(self, input: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, restore: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_std_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AddBorders(self, clip: "VideoNode", left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, color: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def AssumeFPS(self, clip: "VideoNode", src: typing.Union["VideoNode", None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None) -> "VideoNode": ...
    def Binarize(self, clip: "VideoNode", threshold: typing.Union[typing.Sequence[float], None] = None, v0: typing.Union[typing.Sequence[float], None] = None, v1: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def BlankClip(self, clip: typing.Union["VideoNode", None] = None, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, length: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, color: typing.Union[typing.Sequence[float], None] = None, keep: typing.Union[int, None] = None) -> "VideoNode": ...
    def BoxBlur(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, hradius: typing.Union[int, None] = None, hpasses: typing.Union[int, None] = None, vradius: typing.Union[int, None] = None, vpasses: typing.Union[int, None] = None) -> "VideoNode": ...
    def Cache(self, clip: "VideoNode", size: typing.Union[int, None] = None, fixed: typing.Union[int, None] = None, make_linear: typing.Union[int, None] = None) -> "VideoNode": ...
    def ClipToProp(self, clip: "VideoNode", mclip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Convolution(self, clip: "VideoNode", matrix: typing.Sequence[float], bias: typing.Union[float, None] = None, divisor: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, saturate: typing.Union[int, None] = None, mode: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Crop(self, clip: "VideoNode", left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None) -> "VideoNode": ...
    def CropAbs(self, clip: "VideoNode", width: int, height: int, left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, x: typing.Union[int, None] = None, y: typing.Union[int, None] = None) -> "VideoNode": ...
    def CropRel(self, clip: "VideoNode", left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None) -> "VideoNode": ...
    def Deflate(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None) -> "VideoNode": ...
    def DeleteFrames(self, clip: "VideoNode", frames: typing.Sequence[int]) -> "VideoNode": ...
    def DoubleWeave(self, clip: "VideoNode", tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DuplicateFrames(self, clip: "VideoNode", frames: typing.Sequence[int]) -> "VideoNode": ...
    def Expr(self, clips: typing.Sequence["VideoNode"], expr: typing.Sequence[typing.Union[str, bytes, bytearray]], format: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlipHorizontal(self, clip: "VideoNode") -> "VideoNode": ...
    def FlipVertical(self, clip: "VideoNode") -> "VideoNode": ...
    def FrameEval(self, clip: "VideoNode", eval: typing.Callable[..., typing.Any], prop_src: typing.Union[typing.Sequence["VideoNode"], None] = None) -> "VideoNode": ...
    def FreezeFrames(self, clip: "VideoNode", first: typing.Sequence[int], last: typing.Sequence[int], replacement: typing.Sequence[int]) -> "VideoNode": ...
    def Inflate(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None) -> "VideoNode": ...
    def Interleave(self, clips: typing.Sequence["VideoNode"], extend: typing.Union[int, None] = None, mismatch: typing.Union[int, None] = None, modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def Invert(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Levels(self, clip: "VideoNode", min_in: typing.Union[typing.Sequence[float], None] = None, max_in: typing.Union[typing.Sequence[float], None] = None, gamma: typing.Union[typing.Sequence[float], None] = None, min_out: typing.Union[typing.Sequence[float], None] = None, max_out: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Limiter(self, clip: "VideoNode", min: typing.Union[typing.Sequence[float], None] = None, max: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def LoadPlugin(self, path: typing.Union[str, bytes, bytearray], altsearchpath: typing.Union[int, None] = None, forcens: typing.Union[str, bytes, bytearray, None] = None, forceid: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Loop(self, clip: "VideoNode", times: typing.Union[int, None] = None) -> "VideoNode": ...
    def Lut(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, lut: typing.Union[typing.Sequence[int], None] = None, lutf: typing.Union[typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Union[int, None] = None, floatout: typing.Union[int, None] = None) -> "VideoNode": ...
    def Lut2(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, lut: typing.Union[typing.Sequence[int], None] = None, lutf: typing.Union[typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Union[int, None] = None, floatout: typing.Union[int, None] = None) -> "VideoNode": ...
    def MakeDiff(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MaskedMerge(self, clipa: "VideoNode", clipb: "VideoNode", mask: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, first_plane: typing.Union[int, None] = None, premultiplied: typing.Union[int, None] = None) -> "VideoNode": ...
    def Maximum(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None, coordinates: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Median(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Merge(self, clipa: "VideoNode", clipb: "VideoNode", weight: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def MergeDiff(self, clipa: "VideoNode", clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Minimum(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None, coordinates: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ModifyFrame(self, clip: "VideoNode", clips: typing.Sequence["VideoNode"], selector: typing.Callable[..., typing.Any]) -> "VideoNode": ...
    def PEMVerifier(self, clip: "VideoNode", upper: typing.Union[typing.Sequence[float], None] = None, lower: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def PlaneStats(self, clipa: "VideoNode", clipb: typing.Union["VideoNode", None] = None, plane: typing.Union[int, None] = None, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def PreMultiply(self, clip: "VideoNode", alpha: "VideoNode") -> "VideoNode": ...
    def Prewitt(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, scale: typing.Union[float, None] = None) -> "VideoNode": ...
    def PropToClip(self, clip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Reverse(self, clip: "VideoNode") -> "VideoNode": ...
    def SelectEvery(self, clip: "VideoNode", cycle: int, offsets: typing.Sequence[int], modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def SeparateFields(self, clip: "VideoNode", tff: typing.Union[int, None] = None, modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def SetFieldBased(self, clip: "VideoNode", value: int) -> "VideoNode": ...
    def SetFrameProp(self, clip: "VideoNode", prop: typing.Union[str, bytes, bytearray], delete: typing.Union[int, None] = None, intval: typing.Union[typing.Sequence[int], None] = None, floatval: typing.Union[typing.Sequence[float], None] = None, data: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None) -> "VideoNode": ...
    def SetMaxCPU(self, cpu: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def ShufflePlanes(self, clips: typing.Sequence["VideoNode"], planes: typing.Sequence[int], colorfamily: int) -> "VideoNode": ...
    def Sobel(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, scale: typing.Union[float, None] = None) -> "VideoNode": ...
    def Splice(self, clips: typing.Sequence["VideoNode"], mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def StackHorizontal(self, clips: typing.Sequence["VideoNode"]) -> "VideoNode": ...
    def StackVertical(self, clips: typing.Sequence["VideoNode"]) -> "VideoNode": ...
    def Transpose(self, clip: "VideoNode") -> "VideoNode": ...
    def Trim(self, clip: "VideoNode", first: typing.Union[int, None] = None, last: typing.Union[int, None] = None, length: typing.Union[int, None] = None) -> "VideoNode": ...
    def Turn180(self, clip: "VideoNode") -> "VideoNode": ...


class _Plugin_text_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ClipInfo(self, clip: "VideoNode", alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def CoreInfo(self, clip: typing.Union["VideoNode", None] = None, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def FrameNum(self, clip: "VideoNode", alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def FrameProps(self, clip: "VideoNode", props: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def Text(self, clip: "VideoNode", text: typing.Union[str, bytes, bytearray], alignment: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_timecube_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Cube(self, clip: "VideoNode", cube: typing.Union[str, bytes, bytearray], format: typing.Union[int, None] = None, range: typing.Union[int, None] = None, cpu: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tla_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TempLinearApproximate(self, clip: "VideoNode", radius: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, gamma: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_focus2_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalSoften2(self, clip: "VideoNode", radius: typing.Union[int, None] = None, luma_threshold: typing.Union[int, None] = None, chroma_threshold: typing.Union[int, None] = None, scenechange: typing.Union[int, None] = None, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_fmtc_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def bitdepth(self, clip: "VideoNode", csp: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, ampo: typing.Union[float, None] = None, ampn: typing.Union[float, None] = None, dyn: typing.Union[int, None] = None, staticnoise: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None, patsize: typing.Union[int, None] = None) -> "VideoNode": ...
    def histluma(self, clip: "VideoNode", full: typing.Union[int, None] = None, amp: typing.Union[int, None] = None) -> "VideoNode": ...
    def matrix(self, clip: "VideoNode", mat: typing.Union[str, bytes, bytearray, None] = None, mats: typing.Union[str, bytes, bytearray, None] = None, matd: typing.Union[str, bytes, bytearray, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, coef: typing.Union[typing.Sequence[float], None] = None, csp: typing.Union[int, None] = None, col_fam: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, singleout: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def matrix2020cl(self, clip: "VideoNode", full: typing.Union[int, None] = None, csp: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def nativetostack16(self, clip: "VideoNode") -> "VideoNode": ...
    def primaries(self, clip: "VideoNode", rs: typing.Union[typing.Sequence[float], None] = None, gs: typing.Union[typing.Sequence[float], None] = None, bs: typing.Union[typing.Sequence[float], None] = None, ws: typing.Union[typing.Sequence[float], None] = None, rd: typing.Union[typing.Sequence[float], None] = None, gd: typing.Union[typing.Sequence[float], None] = None, bd: typing.Union[typing.Sequence[float], None] = None, wd: typing.Union[typing.Sequence[float], None] = None, prims: typing.Union[str, bytes, bytearray, None] = None, primd: typing.Union[str, bytes, bytearray, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def resample(self, clip: "VideoNode", w: typing.Union[int, None] = None, h: typing.Union[int, None] = None, sx: typing.Union[typing.Sequence[float], None] = None, sy: typing.Union[typing.Sequence[float], None] = None, sw: typing.Union[typing.Sequence[float], None] = None, sh: typing.Union[typing.Sequence[float], None] = None, scale: typing.Union[float, None] = None, scaleh: typing.Union[float, None] = None, scalev: typing.Union[float, None] = None, kernel: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelh: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelv: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, impulse: typing.Union[typing.Sequence[float], None] = None, impulseh: typing.Union[typing.Sequence[float], None] = None, impulsev: typing.Union[typing.Sequence[float], None] = None, taps: typing.Union[typing.Sequence[int], None] = None, tapsh: typing.Union[typing.Sequence[int], None] = None, tapsv: typing.Union[typing.Sequence[int], None] = None, a1: typing.Union[typing.Sequence[float], None] = None, a2: typing.Union[typing.Sequence[float], None] = None, a3: typing.Union[typing.Sequence[float], None] = None, kovrspl: typing.Union[typing.Sequence[int], None] = None, fh: typing.Union[typing.Sequence[float], None] = None, fv: typing.Union[typing.Sequence[float], None] = None, cnorm: typing.Union[typing.Sequence[int], None] = None, totalh: typing.Union[typing.Sequence[float], None] = None, totalv: typing.Union[typing.Sequence[float], None] = None, invks: typing.Union[typing.Sequence[int], None] = None, invksh: typing.Union[typing.Sequence[int], None] = None, invksv: typing.Union[typing.Sequence[int], None] = None, invkstaps: typing.Union[typing.Sequence[int], None] = None, invkstapsh: typing.Union[typing.Sequence[int], None] = None, invkstapsv: typing.Union[typing.Sequence[int], None] = None, csp: typing.Union[int, None] = None, css: typing.Union[str, bytes, bytearray, None] = None, planes: typing.Union[typing.Sequence[float], None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, center: typing.Union[typing.Sequence[int], None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None, cplaces: typing.Union[str, bytes, bytearray, None] = None, cplaced: typing.Union[str, bytes, bytearray, None] = None, interlaced: typing.Union[int, None] = None, interlacedd: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, tffd: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def stack16tonative(self, clip: "VideoNode") -> "VideoNode": ...
    def transfer(self, clip: "VideoNode", transs: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, transd: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, cont: typing.Union[float, None] = None, gcor: typing.Union[float, None] = None, bits: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None, blacklvl: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_deintconf_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def IsCombedTIVTC(self, clip: "VideoNode", cthresh: typing.Union[int, None] = None, MI: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, metric: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def PlaneDifferenceFromPrevious(self, clip: "VideoNode", plane: int, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_trans_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Accord(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, twin: typing.Union[int, None] = None, open: typing.Union[int, None] = None) -> "VideoNode": ...
    def Bubbles(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, static: typing.Union[int, None] = None) -> "VideoNode": ...
    def Central(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, nturns: typing.Union[int, None] = None, emerge: typing.Union[int, None] = None, resize: typing.Union[int, None] = None) -> "VideoNode": ...
    def Crumple(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, crumple: typing.Union[int, None] = None, emerge: typing.Union[int, None] = None) -> "VideoNode": ...
    def Disco(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, emerge: typing.Union[int, None] = None, rad: typing.Union[int, None] = None, nturns: typing.Union[int, None] = None) -> "VideoNode": ...
    def Door(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, open: typing.Union[int, None] = None, vert: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlipPage(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, left: typing.Union[int, None] = None) -> "VideoNode": ...
    def Funnel(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Paint(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None) -> "VideoNode": ...
    def Push(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Ripple(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, origin: typing.Union[int, None] = None, amp: typing.Union[int, None] = None, wlength: typing.Union[int, None] = None, merge: typing.Union[int, None] = None) -> "VideoNode": ...
    def Roll(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, rollin: typing.Union[int, None] = None) -> "VideoNode": ...
    def Scratch(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None) -> "VideoNode": ...
    def Shuffle(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Slide(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, slidein: typing.Union[int, None] = None) -> "VideoNode": ...
    def Sprite(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Swing(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, open: typing.Union[int, None] = None, ndoors: typing.Union[int, None] = None, corner: typing.Union[int, None] = None) -> "VideoNode": ...
    def Swirl(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, qr: typing.Union[int, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def VenitianBlinds(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None, slatwidth: typing.Union[int, None] = None, open: typing.Union[int, None] = None) -> "VideoNode": ...
    def Weave(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None, slatwidth: typing.Union[int, None] = None) -> "VideoNode": ...
    def Wipe(self, clip: "VideoNode", clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_vcmod_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Amplitude(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Fan(self, clip: "VideoNode", span: typing.Union[int, None] = None, edge: typing.Union[int, None] = None, plus: typing.Union[int, None] = None, minus: typing.Union[int, None] = None, uv: typing.Union[int, None] = None) -> "VideoNode": ...
    def GBlur(self, clip: "VideoNode", ksize: typing.Union[int, None] = None, sd: typing.Union[float, None] = None) -> "VideoNode": ...
    def Histogram(self, clip: "VideoNode", clipm: typing.Union["VideoNode", None] = None, type: typing.Union[int, None] = None, table: typing.Union[typing.Sequence[int], None] = None, mf: typing.Union[int, None] = None, window: typing.Union[int, None] = None, limit: typing.Union[int, None] = None) -> "VideoNode": ...
    def MBlur(self, clip: "VideoNode", type: typing.Union[int, None] = None, x: typing.Union[int, None] = None, y: typing.Union[int, None] = None) -> "VideoNode": ...
    def Median(self, clip: "VideoNode", maxgrid: typing.Union[int, None] = None, plane: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Neural(self, clip: "VideoNode", txt: typing.Union[str, bytes, bytearray, None] = None, fname: typing.Union[str, bytes, bytearray, None] = None, tclip: typing.Union["VideoNode", None] = None, xpts: typing.Union[int, None] = None, ypts: typing.Union[int, None] = None, tlx: typing.Union[int, None] = None, tty: typing.Union[int, None] = None, trx: typing.Union[int, None] = None, tby: typing.Union[int, None] = None, iter: typing.Union[int, None] = None, bestof: typing.Union[int, None] = None, wset: typing.Union[int, None] = None, rgb: typing.Union[int, None] = None) -> "VideoNode": ...
    def SaltPepper(self, clip: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, tol: typing.Union[int, None] = None, avg: typing.Union[int, None] = None) -> "VideoNode": ...
    def Variance(self, clip: "VideoNode", lx: int, wd: int, ty: int, ht: int, fn: typing.Union[int, None] = None, uv: typing.Union[int, None] = None, xgrid: typing.Union[int, None] = None, ygrid: typing.Union[int, None] = None) -> "VideoNode": ...
    def Veed(self, clip: "VideoNode", str: typing.Union[int, None] = None, rad: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, plimit: typing.Union[typing.Sequence[int], None] = None, mlimit: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vcmove_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DeBarrel(self, clip: "VideoNode", a: float, b: float, c: float, vhr: typing.Union[float, None] = None, pin: typing.Union[int, None] = None, yind: typing.Union[int, None] = None, ypin: typing.Union[int, None] = None, ya: typing.Union[float, None] = None, yb: typing.Union[float, None] = None, yc: typing.Union[float, None] = None, test: typing.Union[int, None] = None) -> "VideoNode": ...
    def Quad2Rect(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Rect2Quad(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Rotate(self, clip: "VideoNode", bkg: "VideoNode", angle: float, dinc: typing.Union[float, None] = None, lx: typing.Union[int, None] = None, wd: typing.Union[int, None] = None, ty: typing.Union[int, None] = None, ht: typing.Union[int, None] = None, axx: typing.Union[int, None] = None, axy: typing.Union[int, None] = None, intq: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_bilateral_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bilateral(self, input: "VideoNode", ref: typing.Union["VideoNode", None] = None, sigmaS: typing.Union[typing.Sequence[float], None] = None, sigmaR: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None, algorithm: typing.Union[typing.Sequence[int], None] = None, PBFICnum: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Gaussian(self, input: "VideoNode", sigma: typing.Union[typing.Sequence[float], None] = None, sigmaV: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...


class _Plugin_adg_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Mask(self, clip: "VideoNode", luma_scaling: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_f3kdb_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Deband(self, clip: "VideoNode", range: typing.Union[int, None] = None, y: typing.Union[int, None] = None, cb: typing.Union[int, None] = None, cr: typing.Union[int, None] = None, grainy: typing.Union[int, None] = None, grainc: typing.Union[int, None] = None, sample_mode: typing.Union[int, None] = None, seed: typing.Union[int, None] = None, blur_first: typing.Union[int, None] = None, dynamic_grain: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, dither_algo: typing.Union[int, None] = None, keep_tv_range: typing.Union[int, None] = None, output_depth: typing.Union[int, None] = None, random_algo_ref: typing.Union[int, None] = None, random_algo_grain: typing.Union[int, None] = None, random_param_ref: typing.Union[float, None] = None, random_param_grain: typing.Union[float, None] = None, preset: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_vivtc_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VDecimate(self, clip: "VideoNode", cycle: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, dupthresh: typing.Union[float, None] = None, scthresh: typing.Union[float, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, clip2: typing.Union["VideoNode", None] = None, ovr: typing.Union[str, bytes, bytearray, None] = None, dryrun: typing.Union[int, None] = None) -> "VideoNode": ...
    def VFM(self, clip: "VideoNode", order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, mchroma: typing.Union[int, None] = None, cthresh: typing.Union[int, None] = None, mi: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, y0: typing.Union[int, None] = None, y1: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None, micmatch: typing.Union[int, None] = None, micout: typing.Union[int, None] = None, clip2: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_tc2cfr_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def readtcv1(self, clip: "VideoNode", timecode: typing.Union[str, bytes, bytearray], fpsNum: int, fpsDen: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_raws_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Source(self, source: typing.Union[str, bytes, bytearray], width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, sarnum: typing.Union[int, None] = None, sarden: typing.Union[int, None] = None, src_fmt: typing.Union[str, bytes, bytearray, None] = None, off_header: typing.Union[int, None] = None, off_frame: typing.Union[int, None] = None, rowbytes_align: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_fft3dfilter_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def FFT3DFilter(self, clip: "VideoNode", sigma: typing.Union[float, None] = None, beta: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, bw: typing.Union[int, None] = None, bh: typing.Union[int, None] = None, bt: typing.Union[int, None] = None, ow: typing.Union[int, None] = None, oh: typing.Union[int, None] = None, kratio: typing.Union[float, None] = None, sharpen: typing.Union[float, None] = None, scutoff: typing.Union[float, None] = None, svr: typing.Union[float, None] = None, smin: typing.Union[float, None] = None, smax: typing.Union[float, None] = None, measure: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None, wintype: typing.Union[int, None] = None, pframe: typing.Union[int, None] = None, px: typing.Union[int, None] = None, py: typing.Union[int, None] = None, pshow: typing.Union[int, None] = None, pcutoff: typing.Union[float, None] = None, pfactor: typing.Union[float, None] = None, sigma2: typing.Union[float, None] = None, sigma3: typing.Union[float, None] = None, sigma4: typing.Union[float, None] = None, degrid: typing.Union[float, None] = None, dehalo: typing.Union[float, None] = None, hr: typing.Union[float, None] = None, ht: typing.Union[float, None] = None, ncpu: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_lsmas_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def LWLibavSource(self, source: typing.Union[str, bytes, bytearray], stream_index: typing.Union[int, None] = None, cache: typing.Union[int, None] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, threads: typing.Union[int, None] = None, seek_mode: typing.Union[int, None] = None, seek_threshold: typing.Union[int, None] = None, dr: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, variable: typing.Union[int, None] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, prefer_hw: typing.Union[int, None] = None, repeat: typing.Union[int, None] = None, dominance: typing.Union[int, None] = None, ff_loglevel: typing.Union[int, None] = None) -> "VideoNode": ...
    def LibavSMASHSource(self, source: typing.Union[str, bytes, bytearray], track: typing.Union[int, None] = None, threads: typing.Union[int, None] = None, seek_mode: typing.Union[int, None] = None, seek_threshold: typing.Union[int, None] = None, dr: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, variable: typing.Union[int, None] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, prefer_hw: typing.Union[int, None] = None, ff_loglevel: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_reduceflicker_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ReduceFlicker(self, clip: "VideoNode", strength: typing.Union[int, None] = None, aggressive: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tnlm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TNLMeans(self, clip: "VideoNode", ax: typing.Union[int, None] = None, ay: typing.Union[int, None] = None, az: typing.Union[int, None] = None, sx: typing.Union[int, None] = None, sy: typing.Union[int, None] = None, bx: typing.Union[int, None] = None, by: typing.Union[int, None] = None, a: typing.Union[float, None] = None, h: typing.Union[float, None] = None, ssd: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_descale_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Debicubic(self, src: "VideoNode", width: int, height: int, b: typing.Union[float, None] = None, c: typing.Union[float, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Debilinear(self, src: "VideoNode", width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Delanczos(self, src: "VideoNode", width: int, height: int, taps: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline16(self, src: "VideoNode", width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline36(self, src: "VideoNode", width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline64(self, src: "VideoNode", width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_edgefixer_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Continuity(self, clip: "VideoNode", left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, right: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...
    def Reference(self, clip: "VideoNode", ref: "VideoNode", left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, right: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_znedi3_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, clip: "VideoNode", field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, int16_prescreener: typing.Union[int, None] = None, int16_predictor: typing.Union[int, None] = None, exp: typing.Union[int, None] = None, show_mask: typing.Union[int, None] = None, x_nnedi3_weights_bin: typing.Union[str, bytes, bytearray, None] = None, x_cpu: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_scd_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ApplyLog(self, clip: "VideoNode", log: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def Detect(self, clip: "VideoNode", thresh: typing.Union[int, None] = None, interval_h: typing.Union[int, None] = None, interval_v: typing.Union[int, None] = None, log: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_knlm_Unbound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def KNLMeansCL(self, clip: "VideoNode", d: typing.Union[int, None] = None, a: typing.Union[int, None] = None, s: typing.Union[int, None] = None, h: typing.Union[float, None] = None, channels: typing.Union[str, bytes, bytearray, None] = None, wmode: typing.Union[int, None] = None, wref: typing.Union[float, None] = None, rclip: typing.Union["VideoNode", None] = None, device_type: typing.Union[str, bytes, bytearray, None] = None, device_id: typing.Union[int, None] = None, ocl_x: typing.Union[int, None] = None, ocl_y: typing.Union[int, None] = None, ocl_r: typing.Union[int, None] = None, info: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_vinverse_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Vinverse(self, sstr: typing.Union[float, None] = None, amnt: typing.Union[int, None] = None, scl: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_nnedi3_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, int16_prescreener: typing.Union[int, None] = None, int16_predictor: typing.Union[int, None] = None, exp: typing.Union[int, None] = None, show_mask: typing.Union[int, None] = None, combed_only: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_rdvs_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DupBlocks(self, gmthreshold: typing.Union[int, None] = None, mthreshold: typing.Union[int, None] = None, noise: typing.Union[int, None] = None, noisy: typing.Union[int, None] = None, dist: typing.Union[int, None] = None, tolerance: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, pthreshold: typing.Union[int, None] = None, cthreshold: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...
    def RestoreMotionBlocks(self, restore: "VideoNode", neighbour: typing.Union["VideoNode", None] = None, neighbour2: typing.Union["VideoNode", None] = None, alternative: typing.Union["VideoNode", None] = None, gmthreshold: typing.Union[int, None] = None, mthreshold: typing.Union[int, None] = None, noise: typing.Union[int, None] = None, noisy: typing.Union[int, None] = None, dist: typing.Union[int, None] = None, tolerance: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, pthreshold: typing.Union[int, None] = None, cthreshold: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCSelect(self, sceneBegin: "VideoNode", sceneEnd: "VideoNode", globalMotion: "VideoNode", dfactor: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_focus_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalSoften(self, radius: typing.Union[int, None] = None, luma_threshold: typing.Union[int, None] = None, chroma_threshold: typing.Union[int, None] = None, scenechange: typing.Union[int, None] = None, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_grain_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Add(self, var: typing.Union[float, None] = None, uvar: typing.Union[float, None] = None, hcorr: typing.Union[float, None] = None, vcorr: typing.Union[float, None] = None, seed: typing.Union[int, None] = None, constant: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_ctmf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def CTMF(self, radius: typing.Union[int, None] = None, memsize: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_dctf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DCTFilter(self, factors: typing.Sequence[float], planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_deblock_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Deblock(self, quant: typing.Union[int, None] = None, aoffset: typing.Union[int, None] = None, boffset: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_dfttest_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DFTTest(self, ftype: typing.Union[int, None] = None, sigma: typing.Union[float, None] = None, sigma2: typing.Union[float, None] = None, pmin: typing.Union[float, None] = None, pmax: typing.Union[float, None] = None, sbsize: typing.Union[int, None] = None, smode: typing.Union[int, None] = None, sosize: typing.Union[int, None] = None, tbsize: typing.Union[int, None] = None, tmode: typing.Union[int, None] = None, tosize: typing.Union[int, None] = None, swin: typing.Union[int, None] = None, twin: typing.Union[int, None] = None, sbeta: typing.Union[float, None] = None, tbeta: typing.Union[float, None] = None, zmean: typing.Union[int, None] = None, f0beta: typing.Union[float, None] = None, nlocation: typing.Union[typing.Sequence[int], None] = None, alpha: typing.Union[float, None] = None, slocation: typing.Union[typing.Sequence[float], None] = None, ssx: typing.Union[typing.Sequence[float], None] = None, ssy: typing.Union[typing.Sequence[float], None] = None, sst: typing.Union[typing.Sequence[float], None] = None, ssystem: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_eedi2_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def EEDI2(self, field: int, mthresh: typing.Union[int, None] = None, lthresh: typing.Union[int, None] = None, vthresh: typing.Union[int, None] = None, estr: typing.Union[int, None] = None, dstr: typing.Union[int, None] = None, maxd: typing.Union[int, None] = None, map: typing.Union[int, None] = None, nt: typing.Union[int, None] = None, pp: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_mpls_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, playlist: int, angle: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_morpho_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BottomHat(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Close(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Dilate(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Erode(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def Open(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...
    def TopHat(self, size: typing.Union[int, None] = None, shape: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tdm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def IsCombed(self, cthresh: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, mi: typing.Union[int, None] = None, metric: typing.Union[int, None] = None) -> "VideoNode": ...
    def TDeintMod(self, order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, length: typing.Union[int, None] = None, mtype: typing.Union[int, None] = None, ttype: typing.Union[int, None] = None, mtql: typing.Union[int, None] = None, mthl: typing.Union[int, None] = None, mtqc: typing.Union[int, None] = None, mthc: typing.Union[int, None] = None, nt: typing.Union[int, None] = None, minthresh: typing.Union[int, None] = None, maxthresh: typing.Union[int, None] = None, cstr: typing.Union[int, None] = None, athresh: typing.Union[int, None] = None, metric: typing.Union[int, None] = None, expand: typing.Union[int, None] = None, link: typing.Union[int, None] = None, show: typing.Union[int, None] = None, edeint: typing.Union["VideoNode", None] = None, opt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_ttmpsm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TTempSmooth(self, maxr: typing.Union[int, None] = None, thresh: typing.Union[typing.Sequence[int], None] = None, mdiff: typing.Union[typing.Sequence[int], None] = None, strength: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None, fp: typing.Union[int, None] = None, pfclip: typing.Union["VideoNode", None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vd_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VagueDenoiser(self, threshold: typing.Union[float, None] = None, method: typing.Union[int, None] = None, nsteps: typing.Union[int, None] = None, percent: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vmaf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VMAF(self, distorted: "VideoNode", model: typing.Union[int, None] = None, log_path: typing.Union[str, bytes, bytearray, None] = None, log_fmt: typing.Union[int, None] = None, ssim: typing.Union[int, None] = None, ms_ssim: typing.Union[int, None] = None, pool: typing.Union[int, None] = None, ci: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_w3fdif_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def W3FDIF(self, order: int, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_yadifmod_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Yadifmod(self, edeint: "VideoNode", order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_noisegen_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Generate(self, str: typing.Union[float, None] = None, limit: typing.Union[float, None] = None, type: typing.Union[int, None] = None, mean: typing.Union[float, None] = None, var: typing.Union[float, None] = None, dyn: typing.Union[int, None] = None, full: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_rf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Replace(self, clips: typing.Sequence["VideoNode"], intervals: typing.Sequence[typing.Union[str, bytes, bytearray]]) -> "VideoNode": ...


class _Plugin_sangnom_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SangNom(self, order: typing.Union[int, None] = None, dh: typing.Union[int, None] = None, aa: typing.Union[typing.Sequence[int], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_warp_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ABlur(self, blur: typing.Union[int, None] = None, type: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def ASobel(self, thresh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def AWarp(self, mask: "VideoNode", depth: typing.Union[typing.Sequence[int], None] = None, chroma: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def AWarpSharp2(self, thresh: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, type: typing.Union[int, None] = None, depth: typing.Union[typing.Sequence[int], None] = None, chroma: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_sub_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ImageFile(self, file: typing.Union[str, bytes, bytearray], id: typing.Union[int, None] = None, palette: typing.Union[typing.Sequence[int], None] = None, gray: typing.Union[int, None] = None, info: typing.Union[int, None] = None, flatten: typing.Union[int, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Subtitle(self, text: typing.Union[str, bytes, bytearray], start: typing.Union[int, None] = None, end: typing.Union[int, None] = None, debuglevel: typing.Union[int, None] = None, fontdir: typing.Union[str, bytes, bytearray, None] = None, linespacing: typing.Union[float, None] = None, margins: typing.Union[typing.Sequence[int], None] = None, sar: typing.Union[float, None] = None, style: typing.Union[str, bytes, bytearray, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def TextFile(self, file: typing.Union[str, bytes, bytearray], charset: typing.Union[str, bytes, bytearray, None] = None, scale: typing.Union[float, None] = None, debuglevel: typing.Union[int, None] = None, fontdir: typing.Union[str, bytes, bytearray, None] = None, linespacing: typing.Union[float, None] = None, margins: typing.Union[typing.Sequence[int], None] = None, sar: typing.Union[float, None] = None, style: typing.Union[str, bytes, bytearray, None] = None, blend: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_flux_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothST(self, temporal_threshold: typing.Union[int, None] = None, spatial_threshold: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def SmoothT(self, temporal_threshold: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_hist_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Classic(self) -> "VideoNode": ...
    def Color(self) -> "VideoNode": ...
    def Color2(self) -> "VideoNode": ...
    def Levels(self, factor: typing.Union[float, None] = None) -> "VideoNode": ...
    def Luma(self) -> "VideoNode": ...


class _Plugin_median_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Median(self, sync: typing.Union[int, None] = None, samples: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MedianBlend(self, low: typing.Union[int, None] = None, high: typing.Union[int, None] = None, closest: typing.Union[int, None] = None, sync: typing.Union[int, None] = None, samples: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def TemporalMedian(self, radius: typing.Union[int, None] = None, debug: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_msmoosh_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSharpen(self, threshold: typing.Union[float, None] = None, strength: typing.Union[float, None] = None, mask: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MSmooth(self, threshold: typing.Union[float, None] = None, strength: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_mvsf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Analyse(self, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[float, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[float, None] = None, badrange: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def Analyze(self, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[float, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[float, None] = None, badrange: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def BlockFPS(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Compensate(self, super: "VideoNode", vectors: "VideoNode", scbehavior: typing.Union[int, None] = None, thsad: typing.Union[float, None] = None, fields: typing.Union[int, None] = None, time: typing.Union[float, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain1(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain10(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain11(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain12(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain13(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain14(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain15(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain16(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain17(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain18(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain19(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain2(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain20(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain21(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain22(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain23(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", mvbw23: "VideoNode", mvfw23: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain24(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", mvbw10: "VideoNode", mvfw10: "VideoNode", mvbw11: "VideoNode", mvfw11: "VideoNode", mvbw12: "VideoNode", mvfw12: "VideoNode", mvbw13: "VideoNode", mvfw13: "VideoNode", mvbw14: "VideoNode", mvfw14: "VideoNode", mvbw15: "VideoNode", mvfw15: "VideoNode", mvbw16: "VideoNode", mvfw16: "VideoNode", mvbw17: "VideoNode", mvfw17: "VideoNode", mvbw18: "VideoNode", mvfw18: "VideoNode", mvbw19: "VideoNode", mvfw19: "VideoNode", mvbw20: "VideoNode", mvfw20: "VideoNode", mvbw21: "VideoNode", mvfw21: "VideoNode", mvbw22: "VideoNode", mvfw22: "VideoNode", mvbw23: "VideoNode", mvfw23: "VideoNode", mvbw24: "VideoNode", mvfw24: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain3(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain4(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain5(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain6(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain7(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain8(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Degrain9(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", mvbw4: "VideoNode", mvfw4: "VideoNode", mvbw5: "VideoNode", mvfw5: "VideoNode", mvbw6: "VideoNode", mvfw6: "VideoNode", mvbw7: "VideoNode", mvfw7: "VideoNode", mvbw8: "VideoNode", mvfw8: "VideoNode", mvbw9: "VideoNode", mvfw9: "VideoNode", thsad: typing.Union[typing.Sequence[float], None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[typing.Sequence[float], None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Finest(self) -> "VideoNode": ...
    def Flow(self, super: "VideoNode", vectors: "VideoNode", time: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowBlur(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", blur: typing.Union[float, None] = None, prec: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def FlowFPS(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def FlowInter(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", time: typing.Union[float, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Mask(self, vectors: "VideoNode", ml: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, kind: typing.Union[int, None] = None, time: typing.Union[float, None] = None, ysc: typing.Union[float, None] = None, thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Recalculate(self, vectors: "VideoNode", thsad: typing.Union[float, None] = None, smooth: typing.Union[int, None] = None, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, lambda_: typing.Union[float, None] = None, chroma: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCDetection(self, vectors: "VideoNode", thscd1: typing.Union[float, None] = None, thscd2: typing.Union[float, None] = None) -> "VideoNode": ...
    def Super(self, hpad: typing.Union[int, None] = None, vpad: typing.Union[int, None] = None, pel: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, sharp: typing.Union[int, None] = None, rfilter: typing.Union[int, None] = None, pelclip: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_mv_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Analyse(self, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, pelsearch: typing.Union[int, None] = None, isb: typing.Union[int, None] = None, lambda_: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, delta: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, lsad: typing.Union[int, None] = None, plevel: typing.Union[int, None] = None, global_: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, pzero: typing.Union[int, None] = None, pglobal: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, badsad: typing.Union[int, None] = None, badrange: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, trymany: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, search_coarse: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def BlockFPS(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Compensate(self, super: "VideoNode", vectors: "VideoNode", scbehavior: typing.Union[int, None] = None, thsad: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, time: typing.Union[float, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain1(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain2(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Degrain3(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", mvbw2: "VideoNode", mvfw2: "VideoNode", mvbw3: "VideoNode", mvfw3: "VideoNode", thsad: typing.Union[int, None] = None, thsadc: typing.Union[int, None] = None, plane: typing.Union[int, None] = None, limit: typing.Union[int, None] = None, limitc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanAnalyse(self, vectors: "VideoNode", mask: typing.Union["VideoNode", None] = None, zoom: typing.Union[int, None] = None, rot: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, error: typing.Union[float, None] = None, info: typing.Union[int, None] = None, wrong: typing.Union[float, None] = None, zerow: typing.Union[float, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanCompensate(self, data: "VideoNode", offset: typing.Union[float, None] = None, subpixel: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, matchfields: typing.Union[int, None] = None, mirror: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, info: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanEstimate(self, trust: typing.Union[float, None] = None, winx: typing.Union[int, None] = None, winy: typing.Union[int, None] = None, wleft: typing.Union[int, None] = None, wtop: typing.Union[int, None] = None, dxmax: typing.Union[int, None] = None, dymax: typing.Union[int, None] = None, zoommax: typing.Union[float, None] = None, stab: typing.Union[float, None] = None, pixaspect: typing.Union[float, None] = None, info: typing.Union[int, None] = None, show: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DepanStabilise(self, data: "VideoNode", cutoff: typing.Union[float, None] = None, damping: typing.Union[float, None] = None, initzoom: typing.Union[float, None] = None, addzoom: typing.Union[int, None] = None, prev: typing.Union[int, None] = None, next: typing.Union[int, None] = None, mirror: typing.Union[int, None] = None, blur: typing.Union[int, None] = None, dxmax: typing.Union[float, None] = None, dymax: typing.Union[float, None] = None, zoommax: typing.Union[float, None] = None, rotmax: typing.Union[float, None] = None, subpixel: typing.Union[int, None] = None, pixaspect: typing.Union[float, None] = None, fitlast: typing.Union[int, None] = None, tzoom: typing.Union[float, None] = None, info: typing.Union[int, None] = None, method: typing.Union[int, None] = None, fields: typing.Union[int, None] = None) -> "VideoNode": ...
    def Finest(self, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Flow(self, super: "VideoNode", vectors: "VideoNode", time: typing.Union[float, None] = None, mode: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowBlur(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", blur: typing.Union[float, None] = None, prec: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowFPS(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", num: typing.Union[int, None] = None, den: typing.Union[int, None] = None, mask: typing.Union[int, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlowInter(self, super: "VideoNode", mvbw: "VideoNode", mvfw: "VideoNode", time: typing.Union[float, None] = None, ml: typing.Union[float, None] = None, blend: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Mask(self, vectors: "VideoNode", ml: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, kind: typing.Union[int, None] = None, time: typing.Union[float, None] = None, ysc: typing.Union[int, None] = None, thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def Recalculate(self, vectors: "VideoNode", thsad: typing.Union[int, None] = None, smooth: typing.Union[int, None] = None, blksize: typing.Union[int, None] = None, blksizev: typing.Union[int, None] = None, search: typing.Union[int, None] = None, searchparam: typing.Union[int, None] = None, lambda_: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, truemotion: typing.Union[int, None] = None, pnew: typing.Union[int, None] = None, overlap: typing.Union[int, None] = None, overlapv: typing.Union[int, None] = None, divide: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, meander: typing.Union[int, None] = None, fields: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, dct: typing.Union[int, None] = None) -> "VideoNode": ...
    def SCDetection(self, vectors: "VideoNode", thscd1: typing.Union[int, None] = None, thscd2: typing.Union[int, None] = None) -> "VideoNode": ...
    def Super(self, hpad: typing.Union[int, None] = None, vpad: typing.Union[int, None] = None, pel: typing.Union[int, None] = None, levels: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, sharp: typing.Union[int, None] = None, rfilter: typing.Union[int, None] = None, pelclip: typing.Union["VideoNode", None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_scxvid_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Scxvid(self, log: typing.Union[str, bytes, bytearray, None] = None, use_slices: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_smoothuv_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothUV(self, radius: typing.Union[int, None] = None, threshold: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_ssiq_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SSIQ(self, diameter: typing.Union[int, None] = None, strength: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tbilateral_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TBilateral(self, ppclip: typing.Union["VideoNode", None] = None, diameter: typing.Union[typing.Sequence[int], None] = None, sdev: typing.Union[typing.Sequence[float], None] = None, idev: typing.Union[typing.Sequence[float], None] = None, cs: typing.Union[typing.Sequence[float], None] = None, d2: typing.Union[int, None] = None, kerns: typing.Union[int, None] = None, kerni: typing.Union[int, None] = None, restype: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_remap_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def RemapFrames(self, filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, sourceclip: typing.Union["VideoNode", None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def RemapFramesSimple(self, filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Remf(self, filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, sourceclip: typing.Union["VideoNode", None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def Remfs(self, filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def ReplaceFramesSimple(self, sourceclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def Rfs(self, sourceclip: "VideoNode", filename: typing.Union[str, bytes, bytearray, None] = None, mappings: typing.Union[str, bytes, bytearray, None] = None, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tcomb_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TComb(self, mode: typing.Union[int, None] = None, fthreshl: typing.Union[int, None] = None, fthreshc: typing.Union[int, None] = None, othreshl: typing.Union[int, None] = None, othreshc: typing.Union[int, None] = None, map: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_tedgemask_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TEdgeMask(self, threshold: typing.Union[typing.Sequence[float], None] = None, type: typing.Union[int, None] = None, link: typing.Union[int, None] = None, scale: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tmedian_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalMedian(self, radius: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vscope_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Scope(self, mode: typing.Union[str, bytes, bytearray, None] = None, tickmarks: typing.Union[int, None] = None, side: typing.Union[str, bytes, bytearray, None] = None, bottom: typing.Union[str, bytes, bytearray, None] = None, corner: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_wwxd_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def WWXD(self) -> "VideoNode": ...


class _Plugin_svp2_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def SmoothFps(self, super: "VideoNode", sdata: int, vectors: "VideoNode", vdata: int, opt: typing.Union[str, bytes, bytearray], src: typing.Union["VideoNode", None] = None, fps: typing.Union[float, None] = None) -> "VideoNode": ...
    def SmoothFps_NVOF(self, opt: typing.Union[str, bytes, bytearray], nvof_src: typing.Union["VideoNode", None] = None, src: typing.Union["VideoNode", None] = None, fps: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_surfaceblur_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def surfaceblur(self, threshold: typing.Union[float, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_bm3d_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Basic(self, ref: typing.Union["VideoNode", None] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, hard_thr: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def Final(self, ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def OPP2RGB(self, sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def RGB2OPP(self, sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def VAggregate(self, radius: typing.Union[int, None] = None, sample: typing.Union[int, None] = None) -> "VideoNode": ...
    def VBasic(self, ref: typing.Union["VideoNode", None] = None, profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, radius: typing.Union[int, None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, ps_num: typing.Union[int, None] = None, ps_range: typing.Union[int, None] = None, ps_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, hard_thr: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...
    def VFinal(self, ref: "VideoNode", profile: typing.Union[str, bytes, bytearray, None] = None, sigma: typing.Union[typing.Sequence[float], None] = None, radius: typing.Union[int, None] = None, block_size: typing.Union[int, None] = None, block_step: typing.Union[int, None] = None, group_size: typing.Union[int, None] = None, bm_range: typing.Union[int, None] = None, bm_step: typing.Union[int, None] = None, ps_num: typing.Union[int, None] = None, ps_range: typing.Union[int, None] = None, ps_step: typing.Union[int, None] = None, th_mse: typing.Union[float, None] = None, matrix: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_eedi3_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def eedi3(self, field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, alpha: typing.Union[float, None] = None, beta: typing.Union[float, None] = None, gamma: typing.Union[float, None] = None, nrad: typing.Union[int, None] = None, mdis: typing.Union[int, None] = None, hp: typing.Union[int, None] = None, ucubic: typing.Union[int, None] = None, cost3: typing.Union[int, None] = None, vcheck: typing.Union[int, None] = None, vthresh0: typing.Union[float, None] = None, vthresh1: typing.Union[float, None] = None, vthresh2: typing.Union[float, None] = None, sclip: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_ffms2_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def GetLogLevel(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Index(self, cachefile: typing.Union[str, bytes, bytearray, None] = None, indextracks: typing.Union[typing.Sequence[int], None] = None, errorhandling: typing.Union[int, None] = None, overwrite: typing.Union[int, None] = None) -> "VideoNode": ...
    def SetLogLevel(self) -> "VideoNode": ...
    def Source(self, track: typing.Union[int, None] = None, cache: typing.Union[int, None] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, threads: typing.Union[int, None] = None, timecodes: typing.Union[str, bytes, bytearray, None] = None, seekmode: typing.Union[int, None] = None, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, resizer: typing.Union[str, bytes, bytearray, None] = None, format: typing.Union[int, None] = None, alpha: typing.Union[int, None] = None) -> "VideoNode": ...
    def Version(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...


class _Plugin_vfrtocfr_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VFRToCFR(self, timecodes: typing.Union[str, bytes, bytearray], fpsnum: int, fpsden: int, drop: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_hqdn3d_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Hqdn3d(self, lum_spac: typing.Union[float, None] = None, chrom_spac: typing.Union[float, None] = None, lum_tmp: typing.Union[float, None] = None, chrom_tmp: typing.Union[float, None] = None, restart_lap: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_imwri_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Read(self, firstnum: typing.Union[int, None] = None, mismatch: typing.Union[int, None] = None, alpha: typing.Union[int, None] = None, float_output: typing.Union[int, None] = None) -> "VideoNode": ...
    def Write(self, imgformat: typing.Union[str, bytes, bytearray], filename: typing.Union[str, bytes, bytearray], firstnum: typing.Union[int, None] = None, quality: typing.Union[int, None] = None, dither: typing.Union[int, None] = None, compression_type: typing.Union[str, bytes, bytearray, None] = None, overwrite: typing.Union[int, None] = None, alpha: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_misc_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AverageFrames(self, weights: typing.Sequence[float], scale: typing.Union[float, None] = None, scenechange: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Hysteresis(self, clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def SCDetect(self, threshold: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_rgvs_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def BackwardClense(self, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Clense(self, previous: typing.Union["VideoNode", None] = None, next: typing.Union["VideoNode", None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ForwardClense(self, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def RemoveGrain(self, mode: typing.Sequence[int]) -> "VideoNode": ...
    def Repair(self, repairclip: "VideoNode", mode: typing.Sequence[int]) -> "VideoNode": ...
    def VerticalCleaner(self, mode: typing.Sequence[int]) -> "VideoNode": ...


class _Plugin_resize_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bicubic(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Bilinear(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Lanczos(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Point(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline16(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline36(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...
    def Spline64(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, matrix: typing.Union[int, None] = None, matrix_s: typing.Union[str, bytes, bytearray, None] = None, transfer: typing.Union[int, None] = None, transfer_s: typing.Union[str, bytes, bytearray, None] = None, primaries: typing.Union[int, None] = None, primaries_s: typing.Union[str, bytes, bytearray, None] = None, range: typing.Union[int, None] = None, range_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc: typing.Union[int, None] = None, chromaloc_s: typing.Union[str, bytes, bytearray, None] = None, matrix_in: typing.Union[int, None] = None, matrix_in_s: typing.Union[str, bytes, bytearray, None] = None, transfer_in: typing.Union[int, None] = None, transfer_in_s: typing.Union[str, bytes, bytearray, None] = None, primaries_in: typing.Union[int, None] = None, primaries_in_s: typing.Union[str, bytes, bytearray, None] = None, range_in: typing.Union[int, None] = None, range_in_s: typing.Union[str, bytes, bytearray, None] = None, chromaloc_in: typing.Union[int, None] = None, chromaloc_in_s: typing.Union[str, bytes, bytearray, None] = None, filter_param_a: typing.Union[float, None] = None, filter_param_b: typing.Union[float, None] = None, resample_filter_uv: typing.Union[str, bytes, bytearray, None] = None, filter_param_a_uv: typing.Union[float, None] = None, filter_param_b_uv: typing.Union[float, None] = None, dither_type: typing.Union[str, bytes, bytearray, None] = None, cpu_type: typing.Union[str, bytes, bytearray, None] = None, prefer_props: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None, nominal_luminance: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_retinex_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def MSRCP(self, sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, chroma_protect: typing.Union[float, None] = None) -> "VideoNode": ...
    def MSRCR(self, sigma: typing.Union[typing.Sequence[float], None] = None, lower_thr: typing.Union[float, None] = None, upper_thr: typing.Union[float, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, restore: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_std_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def AddBorders(self, left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, color: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def AssumeFPS(self, src: typing.Union["VideoNode", None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None) -> "VideoNode": ...
    def Binarize(self, threshold: typing.Union[typing.Sequence[float], None] = None, v0: typing.Union[typing.Sequence[float], None] = None, v1: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def BlankClip(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, format: typing.Union[int, None] = None, length: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, color: typing.Union[typing.Sequence[float], None] = None, keep: typing.Union[int, None] = None) -> "VideoNode": ...
    def BoxBlur(self, planes: typing.Union[typing.Sequence[int], None] = None, hradius: typing.Union[int, None] = None, hpasses: typing.Union[int, None] = None, vradius: typing.Union[int, None] = None, vpasses: typing.Union[int, None] = None) -> "VideoNode": ...
    def Cache(self, size: typing.Union[int, None] = None, fixed: typing.Union[int, None] = None, make_linear: typing.Union[int, None] = None) -> "VideoNode": ...
    def ClipToProp(self, mclip: "VideoNode", prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Convolution(self, matrix: typing.Sequence[float], bias: typing.Union[float, None] = None, divisor: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, saturate: typing.Union[int, None] = None, mode: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Crop(self, left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None) -> "VideoNode": ...
    def CropAbs(self, width: int, height: int, left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, x: typing.Union[int, None] = None, y: typing.Union[int, None] = None) -> "VideoNode": ...
    def CropRel(self, left: typing.Union[int, None] = None, right: typing.Union[int, None] = None, top: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None) -> "VideoNode": ...
    def Deflate(self, planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None) -> "VideoNode": ...
    def DeleteFrames(self, frames: typing.Sequence[int]) -> "VideoNode": ...
    def DoubleWeave(self, tff: typing.Union[int, None] = None) -> "VideoNode": ...
    def DuplicateFrames(self, frames: typing.Sequence[int]) -> "VideoNode": ...
    def Expr(self, expr: typing.Sequence[typing.Union[str, bytes, bytearray]], format: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlipHorizontal(self) -> "VideoNode": ...
    def FlipVertical(self) -> "VideoNode": ...
    def FrameEval(self, eval: typing.Callable[..., typing.Any], prop_src: typing.Union[typing.Sequence["VideoNode"], None] = None) -> "VideoNode": ...
    def FreezeFrames(self, first: typing.Sequence[int], last: typing.Sequence[int], replacement: typing.Sequence[int]) -> "VideoNode": ...
    def Inflate(self, planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None) -> "VideoNode": ...
    def Interleave(self, extend: typing.Union[int, None] = None, mismatch: typing.Union[int, None] = None, modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def Invert(self, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Levels(self, min_in: typing.Union[typing.Sequence[float], None] = None, max_in: typing.Union[typing.Sequence[float], None] = None, gamma: typing.Union[typing.Sequence[float], None] = None, min_out: typing.Union[typing.Sequence[float], None] = None, max_out: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Limiter(self, min: typing.Union[typing.Sequence[float], None] = None, max: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def LoadPlugin(self, altsearchpath: typing.Union[int, None] = None, forcens: typing.Union[str, bytes, bytearray, None] = None, forceid: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Loop(self, times: typing.Union[int, None] = None) -> "VideoNode": ...
    def Lut(self, planes: typing.Union[typing.Sequence[int], None] = None, lut: typing.Union[typing.Sequence[int], None] = None, lutf: typing.Union[typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Union[int, None] = None, floatout: typing.Union[int, None] = None) -> "VideoNode": ...
    def Lut2(self, clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, lut: typing.Union[typing.Sequence[int], None] = None, lutf: typing.Union[typing.Sequence[float], None] = None, function: typing.Optional[typing.Callable[..., typing.Any]] = None, bits: typing.Union[int, None] = None, floatout: typing.Union[int, None] = None) -> "VideoNode": ...
    def MakeDiff(self, clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def MaskedMerge(self, clipb: "VideoNode", mask: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None, first_plane: typing.Union[int, None] = None, premultiplied: typing.Union[int, None] = None) -> "VideoNode": ...
    def Maximum(self, planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None, coordinates: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Median(self, planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Merge(self, clipb: "VideoNode", weight: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def MergeDiff(self, clipb: "VideoNode", planes: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Minimum(self, planes: typing.Union[typing.Sequence[int], None] = None, threshold: typing.Union[float, None] = None, coordinates: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def ModifyFrame(self, clips: typing.Sequence["VideoNode"], selector: typing.Callable[..., typing.Any]) -> "VideoNode": ...
    def PEMVerifier(self, upper: typing.Union[typing.Sequence[float], None] = None, lower: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...
    def PlaneStats(self, clipb: typing.Union["VideoNode", None] = None, plane: typing.Union[int, None] = None, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def PreMultiply(self, alpha: "VideoNode") -> "VideoNode": ...
    def Prewitt(self, planes: typing.Union[typing.Sequence[int], None] = None, scale: typing.Union[float, None] = None) -> "VideoNode": ...
    def PropToClip(self, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...
    def Reverse(self) -> "VideoNode": ...
    def SelectEvery(self, cycle: int, offsets: typing.Sequence[int], modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def SeparateFields(self, tff: typing.Union[int, None] = None, modify_duration: typing.Union[int, None] = None) -> "VideoNode": ...
    def SetFieldBased(self, value: int) -> "VideoNode": ...
    def SetFrameProp(self, prop: typing.Union[str, bytes, bytearray], delete: typing.Union[int, None] = None, intval: typing.Union[typing.Sequence[int], None] = None, floatval: typing.Union[typing.Sequence[float], None] = None, data: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None) -> "VideoNode": ...
    def SetMaxCPU(self) -> "VideoNode": ...
    def ShufflePlanes(self, planes: typing.Sequence[int], colorfamily: int) -> "VideoNode": ...
    def Sobel(self, planes: typing.Union[typing.Sequence[int], None] = None, scale: typing.Union[float, None] = None) -> "VideoNode": ...
    def Splice(self, mismatch: typing.Union[int, None] = None) -> "VideoNode": ...
    def StackHorizontal(self) -> "VideoNode": ...
    def StackVertical(self) -> "VideoNode": ...
    def Transpose(self) -> "VideoNode": ...
    def Trim(self, first: typing.Union[int, None] = None, last: typing.Union[int, None] = None, length: typing.Union[int, None] = None) -> "VideoNode": ...
    def Turn180(self) -> "VideoNode": ...


class _Plugin_text_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ClipInfo(self, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def CoreInfo(self, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def FrameNum(self, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def FrameProps(self, props: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, alignment: typing.Union[int, None] = None) -> "VideoNode": ...
    def Text(self, text: typing.Union[str, bytes, bytearray], alignment: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_timecube_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Cube(self, cube: typing.Union[str, bytes, bytearray], format: typing.Union[int, None] = None, range: typing.Union[int, None] = None, cpu: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tla_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TempLinearApproximate(self, radius: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, gamma: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_focus2_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TemporalSoften2(self, radius: typing.Union[int, None] = None, luma_threshold: typing.Union[int, None] = None, chroma_threshold: typing.Union[int, None] = None, scenechange: typing.Union[int, None] = None, mode: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_fmtc_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def bitdepth(self, csp: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, dmode: typing.Union[int, None] = None, ampo: typing.Union[float, None] = None, ampn: typing.Union[float, None] = None, dyn: typing.Union[int, None] = None, staticnoise: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None, patsize: typing.Union[int, None] = None) -> "VideoNode": ...
    def histluma(self, full: typing.Union[int, None] = None, amp: typing.Union[int, None] = None) -> "VideoNode": ...
    def matrix(self, mat: typing.Union[str, bytes, bytearray, None] = None, mats: typing.Union[str, bytes, bytearray, None] = None, matd: typing.Union[str, bytes, bytearray, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, coef: typing.Union[typing.Sequence[float], None] = None, csp: typing.Union[int, None] = None, col_fam: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, singleout: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def matrix2020cl(self, full: typing.Union[int, None] = None, csp: typing.Union[int, None] = None, bits: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def nativetostack16(self) -> "VideoNode": ...
    def primaries(self, rs: typing.Union[typing.Sequence[float], None] = None, gs: typing.Union[typing.Sequence[float], None] = None, bs: typing.Union[typing.Sequence[float], None] = None, ws: typing.Union[typing.Sequence[float], None] = None, rd: typing.Union[typing.Sequence[float], None] = None, gd: typing.Union[typing.Sequence[float], None] = None, bd: typing.Union[typing.Sequence[float], None] = None, wd: typing.Union[typing.Sequence[float], None] = None, prims: typing.Union[str, bytes, bytearray, None] = None, primd: typing.Union[str, bytes, bytearray, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def resample(self, w: typing.Union[int, None] = None, h: typing.Union[int, None] = None, sx: typing.Union[typing.Sequence[float], None] = None, sy: typing.Union[typing.Sequence[float], None] = None, sw: typing.Union[typing.Sequence[float], None] = None, sh: typing.Union[typing.Sequence[float], None] = None, scale: typing.Union[float, None] = None, scaleh: typing.Union[float, None] = None, scalev: typing.Union[float, None] = None, kernel: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelh: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, kernelv: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, impulse: typing.Union[typing.Sequence[float], None] = None, impulseh: typing.Union[typing.Sequence[float], None] = None, impulsev: typing.Union[typing.Sequence[float], None] = None, taps: typing.Union[typing.Sequence[int], None] = None, tapsh: typing.Union[typing.Sequence[int], None] = None, tapsv: typing.Union[typing.Sequence[int], None] = None, a1: typing.Union[typing.Sequence[float], None] = None, a2: typing.Union[typing.Sequence[float], None] = None, a3: typing.Union[typing.Sequence[float], None] = None, kovrspl: typing.Union[typing.Sequence[int], None] = None, fh: typing.Union[typing.Sequence[float], None] = None, fv: typing.Union[typing.Sequence[float], None] = None, cnorm: typing.Union[typing.Sequence[int], None] = None, totalh: typing.Union[typing.Sequence[float], None] = None, totalv: typing.Union[typing.Sequence[float], None] = None, invks: typing.Union[typing.Sequence[int], None] = None, invksh: typing.Union[typing.Sequence[int], None] = None, invksv: typing.Union[typing.Sequence[int], None] = None, invkstaps: typing.Union[typing.Sequence[int], None] = None, invkstapsh: typing.Union[typing.Sequence[int], None] = None, invkstapsv: typing.Union[typing.Sequence[int], None] = None, csp: typing.Union[int, None] = None, css: typing.Union[str, bytes, bytearray, None] = None, planes: typing.Union[typing.Sequence[float], None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, center: typing.Union[typing.Sequence[int], None] = None, cplace: typing.Union[str, bytes, bytearray, None] = None, cplaces: typing.Union[str, bytes, bytearray, None] = None, cplaced: typing.Union[str, bytes, bytearray, None] = None, interlaced: typing.Union[int, None] = None, interlacedd: typing.Union[int, None] = None, tff: typing.Union[int, None] = None, tffd: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None) -> "VideoNode": ...
    def stack16tonative(self) -> "VideoNode": ...
    def transfer(self, transs: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, transd: typing.Union[typing.Sequence[typing.Union[str, bytes, bytearray]], None] = None, cont: typing.Union[float, None] = None, gcor: typing.Union[float, None] = None, bits: typing.Union[int, None] = None, flt: typing.Union[int, None] = None, fulls: typing.Union[int, None] = None, fulld: typing.Union[int, None] = None, cpuopt: typing.Union[int, None] = None, blacklvl: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_deintconf_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def IsCombedTIVTC(self, cthresh: typing.Union[int, None] = None, MI: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, metric: typing.Union[int, None] = None, opt: typing.Union[int, None] = None) -> "VideoNode": ...
    def PlaneDifferenceFromPrevious(self, plane: int, prop: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_trans_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Accord(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, twin: typing.Union[int, None] = None, open: typing.Union[int, None] = None) -> "VideoNode": ...
    def Bubbles(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, static: typing.Union[int, None] = None) -> "VideoNode": ...
    def Central(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, nturns: typing.Union[int, None] = None, emerge: typing.Union[int, None] = None, resize: typing.Union[int, None] = None) -> "VideoNode": ...
    def Crumple(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, crumple: typing.Union[int, None] = None, emerge: typing.Union[int, None] = None) -> "VideoNode": ...
    def Disco(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, emerge: typing.Union[int, None] = None, rad: typing.Union[int, None] = None, nturns: typing.Union[int, None] = None) -> "VideoNode": ...
    def Door(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, open: typing.Union[int, None] = None, vert: typing.Union[int, None] = None) -> "VideoNode": ...
    def FlipPage(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, left: typing.Union[int, None] = None) -> "VideoNode": ...
    def Funnel(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Paint(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None) -> "VideoNode": ...
    def Push(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Ripple(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, origin: typing.Union[int, None] = None, amp: typing.Union[int, None] = None, wlength: typing.Union[int, None] = None, merge: typing.Union[int, None] = None) -> "VideoNode": ...
    def Roll(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, rollin: typing.Union[int, None] = None) -> "VideoNode": ...
    def Scratch(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None) -> "VideoNode": ...
    def Shuffle(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Slide(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, slidein: typing.Union[int, None] = None) -> "VideoNode": ...
    def Sprite(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def Swing(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None, open: typing.Union[int, None] = None, ndoors: typing.Union[int, None] = None, corner: typing.Union[int, None] = None) -> "VideoNode": ...
    def Swirl(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, qr: typing.Union[int, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...
    def VenitianBlinds(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None, slatwidth: typing.Union[int, None] = None, open: typing.Union[int, None] = None) -> "VideoNode": ...
    def Weave(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, style: typing.Union[int, None] = None, slatwidth: typing.Union[int, None] = None) -> "VideoNode": ...
    def Wipe(self, clipb: "VideoNode", overlap: typing.Union[float, None] = None, dir: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_vcmod_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Amplitude(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Fan(self, span: typing.Union[int, None] = None, edge: typing.Union[int, None] = None, plus: typing.Union[int, None] = None, minus: typing.Union[int, None] = None, uv: typing.Union[int, None] = None) -> "VideoNode": ...
    def GBlur(self, ksize: typing.Union[int, None] = None, sd: typing.Union[float, None] = None) -> "VideoNode": ...
    def Histogram(self, clipm: typing.Union["VideoNode", None] = None, type: typing.Union[int, None] = None, table: typing.Union[typing.Sequence[int], None] = None, mf: typing.Union[int, None] = None, window: typing.Union[int, None] = None, limit: typing.Union[int, None] = None) -> "VideoNode": ...
    def MBlur(self, type: typing.Union[int, None] = None, x: typing.Union[int, None] = None, y: typing.Union[int, None] = None) -> "VideoNode": ...
    def Median(self, maxgrid: typing.Union[int, None] = None, plane: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Neural(self, txt: typing.Union[str, bytes, bytearray, None] = None, fname: typing.Union[str, bytes, bytearray, None] = None, tclip: typing.Union["VideoNode", None] = None, xpts: typing.Union[int, None] = None, ypts: typing.Union[int, None] = None, tlx: typing.Union[int, None] = None, tty: typing.Union[int, None] = None, trx: typing.Union[int, None] = None, tby: typing.Union[int, None] = None, iter: typing.Union[int, None] = None, bestof: typing.Union[int, None] = None, wset: typing.Union[int, None] = None, rgb: typing.Union[int, None] = None) -> "VideoNode": ...
    def SaltPepper(self, planes: typing.Union[typing.Sequence[int], None] = None, tol: typing.Union[int, None] = None, avg: typing.Union[int, None] = None) -> "VideoNode": ...
    def Variance(self, lx: int, wd: int, ty: int, ht: int, fn: typing.Union[int, None] = None, uv: typing.Union[int, None] = None, xgrid: typing.Union[int, None] = None, ygrid: typing.Union[int, None] = None) -> "VideoNode": ...
    def Veed(self, str: typing.Union[int, None] = None, rad: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, plimit: typing.Union[typing.Sequence[int], None] = None, mlimit: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...


class _Plugin_vcmove_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def DeBarrel(self, a: float, b: float, c: float, vhr: typing.Union[float, None] = None, pin: typing.Union[int, None] = None, yind: typing.Union[int, None] = None, ypin: typing.Union[int, None] = None, ya: typing.Union[float, None] = None, yb: typing.Union[float, None] = None, yc: typing.Union[float, None] = None, test: typing.Union[int, None] = None) -> "VideoNode": ...
    def Quad2Rect(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Rect2Quad(self, *args, **kwargs) -> typing.Union[None, "VideoNode"]: ...
    def Rotate(self, bkg: "VideoNode", angle: float, dinc: typing.Union[float, None] = None, lx: typing.Union[int, None] = None, wd: typing.Union[int, None] = None, ty: typing.Union[int, None] = None, ht: typing.Union[int, None] = None, axx: typing.Union[int, None] = None, axy: typing.Union[int, None] = None, intq: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_bilateral_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Bilateral(self, ref: typing.Union["VideoNode", None] = None, sigmaS: typing.Union[typing.Sequence[float], None] = None, sigmaR: typing.Union[typing.Sequence[float], None] = None, planes: typing.Union[typing.Sequence[int], None] = None, algorithm: typing.Union[typing.Sequence[int], None] = None, PBFICnum: typing.Union[typing.Sequence[int], None] = None) -> "VideoNode": ...
    def Gaussian(self, sigma: typing.Union[typing.Sequence[float], None] = None, sigmaV: typing.Union[typing.Sequence[float], None] = None) -> "VideoNode": ...


class _Plugin_adg_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Mask(self, luma_scaling: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_f3kdb_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Deband(self, range: typing.Union[int, None] = None, y: typing.Union[int, None] = None, cb: typing.Union[int, None] = None, cr: typing.Union[int, None] = None, grainy: typing.Union[int, None] = None, grainc: typing.Union[int, None] = None, sample_mode: typing.Union[int, None] = None, seed: typing.Union[int, None] = None, blur_first: typing.Union[int, None] = None, dynamic_grain: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, dither_algo: typing.Union[int, None] = None, keep_tv_range: typing.Union[int, None] = None, output_depth: typing.Union[int, None] = None, random_algo_ref: typing.Union[int, None] = None, random_algo_grain: typing.Union[int, None] = None, random_param_ref: typing.Union[float, None] = None, random_param_grain: typing.Union[float, None] = None, preset: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_vivtc_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def VDecimate(self, cycle: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, dupthresh: typing.Union[float, None] = None, scthresh: typing.Union[float, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, clip2: typing.Union["VideoNode", None] = None, ovr: typing.Union[str, bytes, bytearray, None] = None, dryrun: typing.Union[int, None] = None) -> "VideoNode": ...
    def VFM(self, order: int, field: typing.Union[int, None] = None, mode: typing.Union[int, None] = None, mchroma: typing.Union[int, None] = None, cthresh: typing.Union[int, None] = None, mi: typing.Union[int, None] = None, chroma: typing.Union[int, None] = None, blockx: typing.Union[int, None] = None, blocky: typing.Union[int, None] = None, y0: typing.Union[int, None] = None, y1: typing.Union[int, None] = None, scthresh: typing.Union[float, None] = None, micmatch: typing.Union[int, None] = None, micout: typing.Union[int, None] = None, clip2: typing.Union["VideoNode", None] = None) -> "VideoNode": ...


class _Plugin_tc2cfr_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def readtcv1(self, timecode: typing.Union[str, bytes, bytearray], fpsNum: int, fpsDen: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_raws_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Source(self, width: typing.Union[int, None] = None, height: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, sarnum: typing.Union[int, None] = None, sarden: typing.Union[int, None] = None, src_fmt: typing.Union[str, bytes, bytearray, None] = None, off_header: typing.Union[int, None] = None, off_frame: typing.Union[int, None] = None, rowbytes_align: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_fft3dfilter_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def FFT3DFilter(self, sigma: typing.Union[float, None] = None, beta: typing.Union[float, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, bw: typing.Union[int, None] = None, bh: typing.Union[int, None] = None, bt: typing.Union[int, None] = None, ow: typing.Union[int, None] = None, oh: typing.Union[int, None] = None, kratio: typing.Union[float, None] = None, sharpen: typing.Union[float, None] = None, scutoff: typing.Union[float, None] = None, svr: typing.Union[float, None] = None, smin: typing.Union[float, None] = None, smax: typing.Union[float, None] = None, measure: typing.Union[int, None] = None, interlaced: typing.Union[int, None] = None, wintype: typing.Union[int, None] = None, pframe: typing.Union[int, None] = None, px: typing.Union[int, None] = None, py: typing.Union[int, None] = None, pshow: typing.Union[int, None] = None, pcutoff: typing.Union[float, None] = None, pfactor: typing.Union[float, None] = None, sigma2: typing.Union[float, None] = None, sigma3: typing.Union[float, None] = None, sigma4: typing.Union[float, None] = None, degrid: typing.Union[float, None] = None, dehalo: typing.Union[float, None] = None, hr: typing.Union[float, None] = None, ht: typing.Union[float, None] = None, ncpu: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_lsmas_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def LWLibavSource(self, stream_index: typing.Union[int, None] = None, cache: typing.Union[int, None] = None, cachefile: typing.Union[str, bytes, bytearray, None] = None, threads: typing.Union[int, None] = None, seek_mode: typing.Union[int, None] = None, seek_threshold: typing.Union[int, None] = None, dr: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, variable: typing.Union[int, None] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, prefer_hw: typing.Union[int, None] = None, repeat: typing.Union[int, None] = None, dominance: typing.Union[int, None] = None, ff_loglevel: typing.Union[int, None] = None) -> "VideoNode": ...
    def LibavSMASHSource(self, track: typing.Union[int, None] = None, threads: typing.Union[int, None] = None, seek_mode: typing.Union[int, None] = None, seek_threshold: typing.Union[int, None] = None, dr: typing.Union[int, None] = None, fpsnum: typing.Union[int, None] = None, fpsden: typing.Union[int, None] = None, variable: typing.Union[int, None] = None, format: typing.Union[str, bytes, bytearray, None] = None, decoder: typing.Union[str, bytes, bytearray, None] = None, prefer_hw: typing.Union[int, None] = None, ff_loglevel: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_reduceflicker_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ReduceFlicker(self, strength: typing.Union[int, None] = None, aggressive: typing.Union[int, None] = None, grey: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_tnlm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def TNLMeans(self, ax: typing.Union[int, None] = None, ay: typing.Union[int, None] = None, az: typing.Union[int, None] = None, sx: typing.Union[int, None] = None, sy: typing.Union[int, None] = None, bx: typing.Union[int, None] = None, by: typing.Union[int, None] = None, a: typing.Union[float, None] = None, h: typing.Union[float, None] = None, ssd: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_descale_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Debicubic(self, width: int, height: int, b: typing.Union[float, None] = None, c: typing.Union[float, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Debilinear(self, width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Delanczos(self, width: int, height: int, taps: typing.Union[int, None] = None, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline16(self, width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline36(self, width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...
    def Despline64(self, width: int, height: int, src_left: typing.Union[float, None] = None, src_top: typing.Union[float, None] = None, src_width: typing.Union[float, None] = None, src_height: typing.Union[float, None] = None) -> "VideoNode": ...


class _Plugin_edgefixer_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def Continuity(self, left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, right: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...
    def Reference(self, ref: "VideoNode", left: typing.Union[int, None] = None, top: typing.Union[int, None] = None, right: typing.Union[int, None] = None, bottom: typing.Union[int, None] = None, radius: typing.Union[int, None] = None) -> "VideoNode": ...


class _Plugin_znedi3_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def nnedi3(self, field: int, dh: typing.Union[int, None] = None, planes: typing.Union[typing.Sequence[int], None] = None, nsize: typing.Union[int, None] = None, nns: typing.Union[int, None] = None, qual: typing.Union[int, None] = None, etype: typing.Union[int, None] = None, pscrn: typing.Union[int, None] = None, opt: typing.Union[int, None] = None, int16_prescreener: typing.Union[int, None] = None, int16_predictor: typing.Union[int, None] = None, exp: typing.Union[int, None] = None, show_mask: typing.Union[int, None] = None, x_nnedi3_weights_bin: typing.Union[str, bytes, bytearray, None] = None, x_cpu: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_scd_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def ApplyLog(self, log: typing.Union[str, bytes, bytearray]) -> "VideoNode": ...
    def Detect(self, thresh: typing.Union[int, None] = None, interval_h: typing.Union[int, None] = None, interval_v: typing.Union[int, None] = None, log: typing.Union[str, bytes, bytearray, None] = None) -> "VideoNode": ...


class _Plugin_knlm_Bound(Plugin):
    """
    This class implements the module definitions for the corresponding VapourSynth plugin.
    This class cannot be imported.
    """
    def KNLMeansCL(self, d: typing.Union[int, None] = None, a: typing.Union[int, None] = None, s: typing.Union[int, None] = None, h: typing.Union[float, None] = None, channels: typing.Union[str, bytes, bytearray, None] = None, wmode: typing.Union[int, None] = None, wref: typing.Union[float, None] = None, rclip: typing.Union["VideoNode", None] = None, device_type: typing.Union[str, bytes, bytearray, None] = None, device_id: typing.Union[int, None] = None, ocl_x: typing.Union[int, None] = None, ocl_y: typing.Union[int, None] = None, ocl_r: typing.Union[int, None] = None, info: typing.Union[int, None] = None) -> "VideoNode": ...




class VideoNode:
    @property
    def vinverse(self) -> _Plugin_vinverse_Bound:
        """
        A simple filter to remove residual combing.
        """
    @property
    def nnedi3(self) -> _Plugin_nnedi3_Bound:
        """
        Neural network edge directed interpolation (3rd gen.), v12
        """
    @property
    def rdvs(self) -> _Plugin_rdvs_Bound:
        """
        RemoveDirt VapourSynth Port
        """
    @property
    def focus(self) -> _Plugin_focus_Bound:
        """
        VapourSynth TemporalSoften Filter
        """
    @property
    def grain(self) -> _Plugin_grain_Bound:
        """
        Add some correlated color gaussian noise
        """
    @property
    def ctmf(self) -> _Plugin_ctmf_Bound:
        """
        Constant Time Median Filtering
        """
    @property
    def dctf(self) -> _Plugin_dctf_Bound:
        """
        DCT/IDCT Frequency Suppressor
        """
    @property
    def deblock(self) -> _Plugin_deblock_Bound:
        """
        It does a deblocking of the picture, using the deblocking filter of h264
        """
    @property
    def dfttest(self) -> _Plugin_dfttest_Bound:
        """
        2D/3D frequency domain denoiser
        """
    @property
    def eedi2(self) -> _Plugin_eedi2_Bound:
        """
        EEDI2
        """
    @property
    def mpls(self) -> _Plugin_mpls_Bound:
        """
        Get m2ts clip id from a playlist and return a dict
        """
    @property
    def morpho(self) -> _Plugin_morpho_Bound:
        """
        Simple morphological filters.
        """
    @property
    def tdm(self) -> _Plugin_tdm_Bound:
        """
        A bi-directionally motion adaptive deinterlacer
        """
    @property
    def ttmpsm(self) -> _Plugin_ttmpsm_Bound:
        """
        A basic, motion adaptive, temporal smoothing filter
        """
    @property
    def vd(self) -> _Plugin_vd_Bound:
        """
        A wavelet based denoiser
        """
    @property
    def vmaf(self) -> _Plugin_vmaf_Bound:
        """
        Video Multi-Method Assessment Fusion
        """
    @property
    def w3fdif(self) -> _Plugin_w3fdif_Bound:
        """
        Weston 3 Field Deinterlacing Filter
        """
    @property
    def yadifmod(self) -> _Plugin_yadifmod_Bound:
        """
        Modification of Fizick's yadif avisynth filter
        """
    @property
    def noisegen(self) -> _Plugin_noisegen_Bound:
        """
        VapourSynth Noise Generator
        """
    @property
    def rf(self) -> _Plugin_rf_Bound:
        """
        VapourSynth Replace Frames Tool
        """
    @property
    def sangnom(self) -> _Plugin_sangnom_Bound:
        """
        VapourSynth Single Field Deinterlacer
        """
    @property
    def warp(self) -> _Plugin_warp_Bound:
        """
        Sharpen images by warping
        """
    @property
    def sub(self) -> _Plugin_sub_Bound:
        """
        A subtitling filter based on libass and ffmpeg.
        """
    @property
    def flux(self) -> _Plugin_flux_Bound:
        """
        FluxSmooth plugin for VapourSynth
        """
    @property
    def hist(self) -> _Plugin_hist_Bound:
        """
        VapourSynth Histogram Plugin
        """
    @property
    def median(self) -> _Plugin_median_Bound:
        """
        Median of clips
        """
    @property
    def msmoosh(self) -> _Plugin_msmoosh_Bound:
        """
        MSmooth and MSharpen
        """
    @property
    def mvsf(self) -> _Plugin_mvsf_Bound:
        """
        MVTools Single Precision
        """
    @property
    def mv(self) -> _Plugin_mv_Bound:
        """
        MVTools v23
        """
    @property
    def scxvid(self) -> _Plugin_scxvid_Bound:
        """
        VapourSynth Scxvid Plugin
        """
    @property
    def smoothuv(self) -> _Plugin_smoothuv_Bound:
        """
        SmoothUV is a spatial derainbow filter
        """
    @property
    def ssiq(self) -> _Plugin_ssiq_Bound:
        """
        SSIQ plugin for VapourSynth
        """
    @property
    def tbilateral(self) -> _Plugin_tbilateral_Bound:
        """
        Bilateral spatial denoising filter
        """
    @property
    def remap(self) -> _Plugin_remap_Bound:
        """
        Remaps frame indices based on a file/string
        """
    @property
    def tcomb(self) -> _Plugin_tcomb_Bound:
        """
        Dotcrawl and rainbow remover
        """
    @property
    def tedgemask(self) -> _Plugin_tedgemask_Bound:
        """
        Edge detection plugin
        """
    @property
    def tmedian(self) -> _Plugin_tmedian_Bound:
        """
        Calculates temporal median
        """
    @property
    def vscope(self) -> _Plugin_vscope_Bound:
        """
        Videoscope plugin for VapourSynth
        """
    @property
    def wwxd(self) -> _Plugin_wwxd_Bound:
        """
        Scene change detection approximately like Xvid's
        """
    @property
    def svp2(self) -> _Plugin_svp2_Bound:
        """
        SVPFlow2
        """
    @property
    def surfaceblur(self) -> _Plugin_surfaceblur_Bound:
        """
        surface blur
        """
    @property
    def bm3d(self) -> _Plugin_bm3d_Bound:
        """
        Implementation of BM3D denoising filter for VapourSynth.
        """
    @property
    def eedi3(self) -> _Plugin_eedi3_Bound:
        """
        EEDI3
        """
    @property
    def ffms2(self) -> _Plugin_ffms2_Bound:
        """
        FFmpegSource 2 for VapourSynth
        """
    @property
    def vfrtocfr(self) -> _Plugin_vfrtocfr_Bound:
        """
        VFR to CFR Video Converter
        """
    @property
    def hqdn3d(self) -> _Plugin_hqdn3d_Bound:
        """
        HQDn3D port as used in avisynth/mplayer
        """
    @property
    def imwri(self) -> _Plugin_imwri_Bound:
        """
        VapourSynth ImageMagick 7 HDRI Writer/Reader
        """
    @property
    def misc(self) -> _Plugin_misc_Bound:
        """
        Miscellaneous filters
        """
    @property
    def rgvs(self) -> _Plugin_rgvs_Bound:
        """
        RemoveGrain VapourSynth Port
        """
    @property
    def resize(self) -> _Plugin_resize_Bound:
        """
        VapourSynth Resize
        """
    @property
    def retinex(self) -> _Plugin_retinex_Bound:
        """
        Implementation of Retinex algorithm for VapourSynth.
        """
    @property
    def std(self) -> _Plugin_std_Bound:
        """
        VapourSynth Core Functions
        """
    @property
    def text(self) -> _Plugin_text_Bound:
        """
        VapourSynth Text
        """
    @property
    def timecube(self) -> _Plugin_timecube_Bound:
        """
        TimeCube 4D
        """
    @property
    def tla(self) -> _Plugin_tla_Bound:
        """
        VapourSynth Temporal Linear Approximation plugin
        """
    @property
    def focus2(self) -> _Plugin_focus2_Bound:
        """
        VapourSynth TemporalSoften Filter v1
        """
    @property
    def fmtc(self) -> _Plugin_fmtc_Bound:
        """
        Format converter, r22
        """
    @property
    def deintconf(self) -> _Plugin_deintconf_Bound:
        """
        auto deinterlace external filters
        """
    @property
    def trans(self) -> _Plugin_trans_Bound:
        """
        VapourSynth transition plugin
        """
    @property
    def vcmod(self) -> _Plugin_vcmod_Bound:
        """
        VapourSynth Pixel Amplitude modification
        """
    @property
    def vcmove(self) -> _Plugin_vcmove_Bound:
        """
        VapourSynth pixel repositioning Plugin
        """
    @property
    def bilateral(self) -> _Plugin_bilateral_Bound:
        """
        Bilateral filter and Gaussian filter for VapourSynth.
        """
    @property
    def adg(self) -> _Plugin_adg_Bound:
        """
        Adaptive grain
        """
    @property
    def f3kdb(self) -> _Plugin_f3kdb_Bound:
        """
        flash3kyuu_deband
        """
    @property
    def vivtc(self) -> _Plugin_vivtc_Bound:
        """
        VFM
        """
    @property
    def tc2cfr(self) -> _Plugin_tc2cfr_Bound:
        """
        timecode to cfr convert
        """
    @property
    def raws(self) -> _Plugin_raws_Bound:
        """
        Raw-format file Reader for VapourSynth 0.3.5
        """
    @property
    def fft3dfilter(self) -> _Plugin_fft3dfilter_Bound:
        """
        FFT3DFilter
        """
    @property
    def lsmas(self) -> _Plugin_lsmas_Bound:
        """
        LSMASHSource for VapourSynth
        """
    @property
    def reduceflicker(self) -> _Plugin_reduceflicker_Bound:
        """
        ReduceFlicker rev2-8766391
        """
    @property
    def tnlm(self) -> _Plugin_tnlm_Bound:
        """
        TNLMeans rev39-22a40af
        """
    @property
    def descale(self) -> _Plugin_descale_Bound:
        """
        Undo linear interpolation
        """
    @property
    def edgefixer(self) -> _Plugin_edgefixer_Bound:
        """
        ultraman
        """
    @property
    def znedi3(self) -> _Plugin_znedi3_Bound:
        """
        Neural network edge directed interpolation (3rd gen.)
        """
    @property
    def scd(self) -> _Plugin_scd_Bound:
        """
        Scene change detect filter for VapourSynth v0.2.0
        """
    @property
    def knlm(self) -> _Plugin_knlm_Bound:
        """
        KNLMeansCL for VapourSynth
        """

    format: typing.Optional[Format]

    fps: fractions.Fraction
    fps_den: int
    fps_num: int

    height: int
    width: int

    num_frames: int
    flags: int

    def get_frame(self, n: int) -> VideoFrame: ...
    def get_frame_async_raw(self, n: int, cb: _Future[VideoFrame], future_wrapper: typing.Optional[typing.Callable[..., None]]=None) -> _Future[VideoFrame]: ...
    def get_frame_async(self, n: int) -> _Future[VideoFrame]: ...

    def set_output(self, index: int=0, alpha: typing.Optional['VideoNode']=None) -> None: ...
    def output(self, fileobj: typing.BinaryIO, y4m: bool = False, progress_update: typing.Optional[typing.Callable[[int], int]]=None, prefetch: int = 0) -> None: ...

    def frames(self) -> typing.Iterator[VideoFrame]: ...

    def __add__(self, other: 'VideoNode') -> 'VideoNode': ...
    def __mul__(self, other: int) -> 'VideoNode': ...
    def __getitem__(self, other: typing.Union[int, slice]) -> 'VideoNode': ...
    def __len__(self) -> int: ...


class _PluginMeta(typing.TypedDict):
    namespace: str
    identifier: str
    name: str
    functions: typing.Dict[str, str]


class Core:
    @property
    def vinverse(self) -> _Plugin_vinverse_Unbound:
        """
        A simple filter to remove residual combing.
        """
    @property
    def nnedi3(self) -> _Plugin_nnedi3_Unbound:
        """
        Neural network edge directed interpolation (3rd gen.), v12
        """
    @property
    def rdvs(self) -> _Plugin_rdvs_Unbound:
        """
        RemoveDirt VapourSynth Port
        """
    @property
    def focus(self) -> _Plugin_focus_Unbound:
        """
        VapourSynth TemporalSoften Filter
        """
    @property
    def grain(self) -> _Plugin_grain_Unbound:
        """
        Add some correlated color gaussian noise
        """
    @property
    def ctmf(self) -> _Plugin_ctmf_Unbound:
        """
        Constant Time Median Filtering
        """
    @property
    def dctf(self) -> _Plugin_dctf_Unbound:
        """
        DCT/IDCT Frequency Suppressor
        """
    @property
    def deblock(self) -> _Plugin_deblock_Unbound:
        """
        It does a deblocking of the picture, using the deblocking filter of h264
        """
    @property
    def dfttest(self) -> _Plugin_dfttest_Unbound:
        """
        2D/3D frequency domain denoiser
        """
    @property
    def eedi2(self) -> _Plugin_eedi2_Unbound:
        """
        EEDI2
        """
    @property
    def mpls(self) -> _Plugin_mpls_Unbound:
        """
        Get m2ts clip id from a playlist and return a dict
        """
    @property
    def morpho(self) -> _Plugin_morpho_Unbound:
        """
        Simple morphological filters.
        """
    @property
    def tdm(self) -> _Plugin_tdm_Unbound:
        """
        A bi-directionally motion adaptive deinterlacer
        """
    @property
    def ttmpsm(self) -> _Plugin_ttmpsm_Unbound:
        """
        A basic, motion adaptive, temporal smoothing filter
        """
    @property
    def vd(self) -> _Plugin_vd_Unbound:
        """
        A wavelet based denoiser
        """
    @property
    def vmaf(self) -> _Plugin_vmaf_Unbound:
        """
        Video Multi-Method Assessment Fusion
        """
    @property
    def w3fdif(self) -> _Plugin_w3fdif_Unbound:
        """
        Weston 3 Field Deinterlacing Filter
        """
    @property
    def yadifmod(self) -> _Plugin_yadifmod_Unbound:
        """
        Modification of Fizick's yadif avisynth filter
        """
    @property
    def noisegen(self) -> _Plugin_noisegen_Unbound:
        """
        VapourSynth Noise Generator
        """
    @property
    def rf(self) -> _Plugin_rf_Unbound:
        """
        VapourSynth Replace Frames Tool
        """
    @property
    def sangnom(self) -> _Plugin_sangnom_Unbound:
        """
        VapourSynth Single Field Deinterlacer
        """
    @property
    def warp(self) -> _Plugin_warp_Unbound:
        """
        Sharpen images by warping
        """
    @property
    def sub(self) -> _Plugin_sub_Unbound:
        """
        A subtitling filter based on libass and ffmpeg.
        """
    @property
    def flux(self) -> _Plugin_flux_Unbound:
        """
        FluxSmooth plugin for VapourSynth
        """
    @property
    def hist(self) -> _Plugin_hist_Unbound:
        """
        VapourSynth Histogram Plugin
        """
    @property
    def median(self) -> _Plugin_median_Unbound:
        """
        Median of clips
        """
    @property
    def msmoosh(self) -> _Plugin_msmoosh_Unbound:
        """
        MSmooth and MSharpen
        """
    @property
    def mvsf(self) -> _Plugin_mvsf_Unbound:
        """
        MVTools Single Precision
        """
    @property
    def mv(self) -> _Plugin_mv_Unbound:
        """
        MVTools v23
        """
    @property
    def scxvid(self) -> _Plugin_scxvid_Unbound:
        """
        VapourSynth Scxvid Plugin
        """
    @property
    def smoothuv(self) -> _Plugin_smoothuv_Unbound:
        """
        SmoothUV is a spatial derainbow filter
        """
    @property
    def ssiq(self) -> _Plugin_ssiq_Unbound:
        """
        SSIQ plugin for VapourSynth
        """
    @property
    def tbilateral(self) -> _Plugin_tbilateral_Unbound:
        """
        Bilateral spatial denoising filter
        """
    @property
    def remap(self) -> _Plugin_remap_Unbound:
        """
        Remaps frame indices based on a file/string
        """
    @property
    def tcomb(self) -> _Plugin_tcomb_Unbound:
        """
        Dotcrawl and rainbow remover
        """
    @property
    def tedgemask(self) -> _Plugin_tedgemask_Unbound:
        """
        Edge detection plugin
        """
    @property
    def tmedian(self) -> _Plugin_tmedian_Unbound:
        """
        Calculates temporal median
        """
    @property
    def vscope(self) -> _Plugin_vscope_Unbound:
        """
        Videoscope plugin for VapourSynth
        """
    @property
    def wwxd(self) -> _Plugin_wwxd_Unbound:
        """
        Scene change detection approximately like Xvid's
        """
    @property
    def svp2(self) -> _Plugin_svp2_Unbound:
        """
        SVPFlow2
        """
    @property
    def surfaceblur(self) -> _Plugin_surfaceblur_Unbound:
        """
        surface blur
        """
    @property
    def bm3d(self) -> _Plugin_bm3d_Unbound:
        """
        Implementation of BM3D denoising filter for VapourSynth.
        """
    @property
    def eedi3(self) -> _Plugin_eedi3_Unbound:
        """
        EEDI3
        """
    @property
    def ffms2(self) -> _Plugin_ffms2_Unbound:
        """
        FFmpegSource 2 for VapourSynth
        """
    @property
    def vfrtocfr(self) -> _Plugin_vfrtocfr_Unbound:
        """
        VFR to CFR Video Converter
        """
    @property
    def hqdn3d(self) -> _Plugin_hqdn3d_Unbound:
        """
        HQDn3D port as used in avisynth/mplayer
        """
    @property
    def imwri(self) -> _Plugin_imwri_Unbound:
        """
        VapourSynth ImageMagick 7 HDRI Writer/Reader
        """
    @property
    def misc(self) -> _Plugin_misc_Unbound:
        """
        Miscellaneous filters
        """
    @property
    def rgvs(self) -> _Plugin_rgvs_Unbound:
        """
        RemoveGrain VapourSynth Port
        """
    @property
    def resize(self) -> _Plugin_resize_Unbound:
        """
        VapourSynth Resize
        """
    @property
    def retinex(self) -> _Plugin_retinex_Unbound:
        """
        Implementation of Retinex algorithm for VapourSynth.
        """
    @property
    def std(self) -> _Plugin_std_Unbound:
        """
        VapourSynth Core Functions
        """
    @property
    def text(self) -> _Plugin_text_Unbound:
        """
        VapourSynth Text
        """
    @property
    def timecube(self) -> _Plugin_timecube_Unbound:
        """
        TimeCube 4D
        """
    @property
    def tla(self) -> _Plugin_tla_Unbound:
        """
        VapourSynth Temporal Linear Approximation plugin
        """
    @property
    def focus2(self) -> _Plugin_focus2_Unbound:
        """
        VapourSynth TemporalSoften Filter v1
        """
    @property
    def fmtc(self) -> _Plugin_fmtc_Unbound:
        """
        Format converter, r22
        """
    @property
    def deintconf(self) -> _Plugin_deintconf_Unbound:
        """
        auto deinterlace external filters
        """
    @property
    def trans(self) -> _Plugin_trans_Unbound:
        """
        VapourSynth transition plugin
        """
    @property
    def vcmod(self) -> _Plugin_vcmod_Unbound:
        """
        VapourSynth Pixel Amplitude modification
        """
    @property
    def vcmove(self) -> _Plugin_vcmove_Unbound:
        """
        VapourSynth pixel repositioning Plugin
        """
    @property
    def bilateral(self) -> _Plugin_bilateral_Unbound:
        """
        Bilateral filter and Gaussian filter for VapourSynth.
        """
    @property
    def adg(self) -> _Plugin_adg_Unbound:
        """
        Adaptive grain
        """
    @property
    def f3kdb(self) -> _Plugin_f3kdb_Unbound:
        """
        flash3kyuu_deband
        """
    @property
    def vivtc(self) -> _Plugin_vivtc_Unbound:
        """
        VFM
        """
    @property
    def tc2cfr(self) -> _Plugin_tc2cfr_Unbound:
        """
        timecode to cfr convert
        """
    @property
    def raws(self) -> _Plugin_raws_Unbound:
        """
        Raw-format file Reader for VapourSynth 0.3.5
        """
    @property
    def fft3dfilter(self) -> _Plugin_fft3dfilter_Unbound:
        """
        FFT3DFilter
        """
    @property
    def lsmas(self) -> _Plugin_lsmas_Unbound:
        """
        LSMASHSource for VapourSynth
        """
    @property
    def reduceflicker(self) -> _Plugin_reduceflicker_Unbound:
        """
        ReduceFlicker rev2-8766391
        """
    @property
    def tnlm(self) -> _Plugin_tnlm_Unbound:
        """
        TNLMeans rev39-22a40af
        """
    @property
    def descale(self) -> _Plugin_descale_Unbound:
        """
        Undo linear interpolation
        """
    @property
    def edgefixer(self) -> _Plugin_edgefixer_Unbound:
        """
        ultraman
        """
    @property
    def znedi3(self) -> _Plugin_znedi3_Unbound:
        """
        Neural network edge directed interpolation (3rd gen.)
        """
    @property
    def scd(self) -> _Plugin_scd_Unbound:
        """
        Scene change detect filter for VapourSynth v0.2.0
        """
    @property
    def knlm(self) -> _Plugin_knlm_Unbound:
        """
        KNLMeansCL for VapourSynth
        """

    num_threads: int
    max_cache_size: int
    add_cache: bool

    def set_max_cache_size(self, mb: int) -> int: ...
    def get_plugins(self) -> typing.Dict[str, _PluginMeta]: ...
    def list_functions(self) -> str: ...

    def register_format(self, color_family: ColorFamily, sample_type: SampleType, bits_per_sample: int, subsampling_w: int, subsampling_h: int) -> Format: ...
    def get_format(self, id: typing.Union[Format, int, PresetFormat]) -> Format: ...

    def version(self) -> str: ...
    def version_number(self) -> int: ...


def get_core(threads: typing.Optional[int]=None, add_cache: typing.Optional[bool]=None) -> Core: ...


class _CoreProxy(Core):
    core: Core


core: _CoreProxy
