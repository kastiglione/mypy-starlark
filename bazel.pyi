from typing import Any, Callable, List, Dict, Optional, Union, TypeVar, Generic, Sequence


def load(
    label: str,
    *args: str,
    **kwargs: str,
) -> None: ...


T = TypeVar("T")


class File:
    basename: str
    dirname: str
    extension: str
    is_source: bool
    owner: Label
    path: str
    root: root
    short_path: str


class root:
    path: str


class depset(Generic[T]):
    def __init__(
        self,
        items: Sequence[T] = [],
        order: str = "default",
        *,
        direct: Sequence[T] = [],
        transitive: Sequence[depset[T]] = [],
    ) -> None: ...

    def to_list(self) -> List[T]: ...


class Args:
    pass


class Actions:
    @staticmethod
    def args() -> Args: ...

    @staticmethod
    def declare_directory(
        filename: str,
        *,
        sibling: Optional[File] = None,
    ) -> File: ...

    @staticmethod
    def declare_file(
        filename: str,
        *,
        sibling: Optional[File] = None,
    ) -> File: ...

    @staticmethod
    def do_nothing(
        mnemonic: str,
        inputs: Union[Sequence[File], depset[File]],
    ) -> None: ...

    @staticmethod
    def expand_template(
        template: File,
        output: File,
        substitutions: Dict[str, str],
        is_executable: bool = False,
    ) -> None: ...

    @staticmethod
    def run(
        outputs: Sequence[File],
        inputs: Union[Sequence[File], depset[File]] = [],
        executable: Union[File, str] = "",
        tools: Union[Sequence[File], depset[File]] = [],
        arguments: Union[Sequence[str], Args] = [],
        mnemonic: str = "",
        progress_message: str = "",
        use_default_shell_env: bool = False,
        env: Dict[str, str] = {},
        execution_requirements: Dict[str, str] = {},
    ) -> None: ...

    @staticmethod
    def run_shell(
        outputs: Sequence[File],
        inputs: Union[Sequence[File], depset[File]] = [],
        tools: Union[Sequence[File], depset[File]] = [],
        arguments: Union[Sequence[str], Args] = [],
        mnemonic: str = "",
        command: Sequence[str],
        progress_message: str = "",
        use_default_shell_env: bool = False,
        env: Dict[str, str] = {},
        execution_requirements: Dict[str, str] = {},
    ) -> None: ...

    @staticmethod
    def write(
        output: File,
        content: Union[str, Args],
        is_executable: bool = False,
    ) -> None: ...


class Ctx:
    actions = Actions

    bin_dir: root
    genfiles_dir: root
    build_file_path: str
    disabled_features: List[str]
    features: List[str]
    label: Label
    workspace_name: str
    var: Dict[str, str]

    def runfiles(
        files: Sequence[File] = [],
        transitive_files: depset[File] = depset([]),
        collect_data: bool = False,
        collect_default: bool = False,
    ) -> runfiles: ...


class Target:
    label: Label
    files: depset[File]


class Provider:
    pass


class DefaultInfo(Provider):
    def __init__(
        self,
        files: depset[File],
        runfiles: Optional[runfiles] = None,
        data_runfiles: Optional[runfiles] = None,
        default_runfiles: Optional[runfiles] = None,
        executable: Optional[File] = None,
    ) -> None: ...

    files: depset[File]
    data_runfiles: runfiles
    default_runfiles: runfiles


class runfiles:
    empty_filenames: depset[str]
    files: depset[File]

    def merge(self, other: runfiles) -> runfiles: ...


class SwiftInfo(Provider):
    pass


class Rule:
    pass


def fail(msg: str, attr: Optional[str] = None) -> None: ...


def provider(
    doc: str = "",
    *,
    fields: Union[Sequence[str], Dict[str, str]] = [],
) -> Provider: ...


def select(x: Dict[str, Any], no_match_error: str = "") -> Any: ...


def rule(
    implementation: Callable[[Any], List[Provider]],
    test: bool = False,
    attrs: Dict[str, Attribute] = {},
    outputs: Dict[str, str] = {},
    executable: bool = False,
    output_to_genfiles: bool = False,
    fragments: List[str] = [],
    host_fragments: List[str] = [],
    _skylark_testable: bool = False,
    toolchains: List[str] = [],
    doc: str = "",
    *,
    provides: Sequence[Provider] = [],
    execution_platform_constraints_allowed: bool = False,
    exec_compatible_with: Sequence[str] = [],
    cfg: Optional[str] = None,
) -> Rule: ...


def workspace(name: str) -> None: ...


class Label:
    def __init__(label_string: str) -> None: ...

    name: str
    package: str
    workspace_name: str
    workspace_root: str

    def relative(relName: str) -> Label: ...


class Attribute:
    pass


class attr:
    @staticmethod
    def bool(
        default: bool = False,
        doc: str = "",
        mandatory: bool = False,
    ) -> Attribute: ...

    @staticmethod
    def int(
        default: int = 0,
        doc: str = "",
        mandatory: bool = False,
        values: Sequence[int] = [],
    ) -> Attribute: ...

    @staticmethod
    def int_list(
        mandatory: bool = False,
        non_empty: bool = False,
        allow_empty: bool = True,
        *,
        default: Sequence[int] = [],
        doc: str = "",
    ) -> Attribute: ...

    @staticmethod
    def bool(
            default: bool = False,
    ) -> Attribute: ...

    @staticmethod
    def label(
        default: Union[Label, str] = "",
        doc: str = "",
        executable: bool = False,
        allow_files: Union[bool, Sequence[str]] = bool,
        allow_single_file: Union[bool, Sequence[str]] = bool,
        mandatory: bool = False,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = [],
        cfg: str = "target",
    ) -> Attribute: ...

    @staticmethod
    def label_keyed_string_dict(
        allow_empty: bool = True,
        default: Dict[Label, str] = {},
        doc: str = "",
        allow_files: Union[bool, Sequence[str]] = bool,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = [],
        mandatory: bool = False,
        cfg: str = "target",
    ) -> Attribute: ...

    @staticmethod
    def label_list(
        allow_empty: bool = True,
        default: Sequence[Union[Label, str]] = []
        doc: str = "",
        allow_files: Union[bool, Sequence[str]] = bool,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = [],
        mandatory: bool = False,
        cfg: str = "target",
    ) -> Attribute: ...

    @staticmethod
    def output(
        doc: str = "",
        mandatory: bool = False,
    ) -> Attribute: ...

    @staticmethod
    def output_list(
        allow_empty: bool = True,
        doc: str = "",
        mandatory: bool = False,
    ) -> Attribute: ...

    @staticmethod
    def string(
        default: str = "",
        doc: str = "",
        mandatory: bool = False,
        values: Sequence[str] = [],
    ) -> Attribute: ...

    @staticmethod
    def string_dict(
        allow_empty: bool = True,
        default: Dict[str, str] = {},
        doc: str = "",
        mandatory: bool = False,
    ) -> Attribute: ...

    @staticmethod
    def string_list(
        mandatory: bool = False,
        allow_empty: bool = True,
        default: Sequence[str] = [],
        doc: str = "",
    ) -> Attribute: ...

    @staticmethod
    def string_list_dict(
        allow_empty: bool = True,
        default: Dict[str, List[str]] = {},
        doc: str = "",
        mandatory: bool = False,
    ) -> Attribute: ...


class native:
    @staticmethod
    def glob(patterns: List[str]) -> List[str]: ...


class apple_common:
    multi_arch_split: str
    platform_type: PlatformType


class PlatformType:
    ios: Any
