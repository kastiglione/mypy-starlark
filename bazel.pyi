from typing import Any, Callable, List, Dict, Union, TypeVar, Generic, Sequence


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
        items: Sequence[T] = ...,
        order: str = ...,
        *,
        direct: Sequence[T] = ...,
        transitive: Sequence[depset[T]] = ...,
    ) -> None: ...

    def to_list(self) -> List[T]: ...


# https://docs.bazel.build/versions/master/skylark/lib/Args.html
class Args:
    def add(
        arg_name_or_value: Union[str, T],
        value: T,
        *,
        format: str = ...,
    ) -> Args: ...

    def add_all(
        arg_name_or_values: Union[str, Sequence[T], depset[T]],
        values: Union[Sequence[T], depset[T]],
        *,
        map_each: Callable[[T], Union[None, str, Sequence[str]]] = ...,
        format_each: str = ...,
        before_each: str = ...,
        omit_if_empty: bool = ...,
        uniquify: bool = ...,
        expand_directories: bool = ...,
        terminate_with: str = ...,
    ) -> Args: ...

    def add_joined(
        arg_name_or_values: Union[str, Sequence[T], depset[T]],
        values: Union[Sequence[T], depset[T]] = ...,
        *,
        join_with: str = ...,
        map_each: Callable[[T], Union[None, str, Sequence[str]]] = ...,
        format_each: str = ...,
        format_joined: str = ...,
        omit_if_empty: bool = ...,
        uniquify: bool = ...,
        expand_directories: bool = ...,
    ) -> Args: ...

    def set_param_file_format(format: str) -> Args: ...

    def use_param_file(
        param_file_arg: str,
        *,
        use_always: bool = ...,
    ) -> Args: ...


class Actions:
    @staticmethod
    def args() -> Args: ...

    @staticmethod
    def declare_directory(
        filename: str,
        *,
        sibling: File = ...,
    ) -> File: ...

    @staticmethod
    def declare_file(
        filename: str,
        *,
        sibling: File = ...,
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
        is_executable: bool = ...,
    ) -> None: ...

    @staticmethod
    def run(
        outputs: Sequence[File],
        inputs: Union[Sequence[File], depset[File]] = ...,
        executable: Union[File, str] = ...,
        tools: Union[Sequence[File], depset[File]] = ...,
        arguments: Union[Sequence[str], Args] = ...,
        mnemonic: str = ...,
        progress_message: str = ...,
        use_default_shell_env: bool = ...,
        env: Dict[str, str] = ...,
        execution_requirements: Dict[str, str] = ...,
    ) -> None: ...

    @staticmethod
    def run_shell(
        outputs: Sequence[File],
        inputs: Union[Sequence[File], depset[File]] = ...,
        tools: Union[Sequence[File], depset[File]] = ...,
        arguments: Union[Sequence[str], Args] = ...,
        mnemonic: str = ...,
        command: Sequence[str],
        progress_message: str = ...,
        use_default_shell_env: bool = ...,
        env: Dict[str, str] = ...,
        execution_requirements: Dict[str, str] = ...,
    ) -> None: ...

    @staticmethod
    def write(
        output: File,
        content: Union[str, Args],
        is_executable: bool = ...,
    ) -> None: ...


# https://docs.bazel.build/versions/master/skylark/lib/ctx.html
Attr = TypeVar("Attr")

class Ctx(Generic[Attr]):
    actions: Actions

    attr: Attr

    bin_dir: root
    genfiles_dir: root
    build_file_path: str
    disabled_features: List[str]
    features: List[str]
    label: Label
    workspace_name: str
    var: Dict[str, str]

    def runfiles(
        files: Sequence[File] = ...,
        transitive_files: depset[File] = ...,
        collect_data: bool = ...,
        collect_default: bool = ...,
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
        runfiles: runfiles = ...,
        data_runfiles: runfiles = ...,
        default_runfiles: runfiles = ...,
        executable: File = ...,
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


def fail(msg: str, attr: str = ...) -> None: ...


def provider(
    doc: str = ...,
    *,
    fields: Union[Sequence[str], Dict[str, str]] = ...,
) -> Provider: ...


def select(x: Dict[str, Any], no_match_error: str = ...) -> Any: ...


def rule(
    implementation: Callable[[Any], List[Provider]],
    test: bool = ...,
    attrs: Dict[str, Attribute] = ...,
    outputs: Dict[str, str] = ...,
    executable: bool = ...,
    output_to_genfiles: bool = ...,
    fragments: List[str] = ...,
    host_fragments: List[str] = ...,
    _skylark_testable: bool = ...,
    toolchains: List[str] = ...,
    doc: str = ...,
    *,
    provides: Sequence[Provider] = ...,
    execution_platform_constraints_allowed: bool = ...,
    exec_compatible_with: Sequence[str] = ...,
    cfg: str = ...,
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
        default: bool = ...,
        doc: str = ...,
        mandatory: bool = ...,
    ) -> Attribute: ...

    @staticmethod
    def int(
        default: int = ...,
        doc: str = ...,
        mandatory: bool = ...,
        values: Sequence[int] = ...,
    ) -> Attribute: ...

    @staticmethod
    def int_list(
        mandatory: bool = ...,
        non_empty: bool = ...,
        allow_empty: bool = ...,
        *,
        default: Sequence[int] = ...,
        doc: str = ...,
    ) -> Attribute: ...

    @staticmethod
    def bool(
            default: bool = ...,
    ) -> Attribute: ...

    @staticmethod
    def label(
        default: Union[Label, str] = ...,
        doc: str = ...,
        executable: bool = ...,
        allow_files: Union[bool, Sequence[str]] = ...,
        allow_single_file: Union[bool, Sequence[str]] = ...,
        mandatory: bool = ...,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = ...,
        cfg: str = ...,
    ) -> Attribute: ...

    @staticmethod
    def label_keyed_string_dict(
        allow_empty: bool = ...,
        default: Dict[Label, str] = ...,
        doc: str = ...,
        allow_files: Union[bool, Sequence[str]] = ...,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = ...,
        mandatory: bool = ...,
        cfg: str = ...,
    ) -> Attribute: ...

    @staticmethod
    def label_list(
        allow_empty: bool = ...,
        default: Sequence[Union[Label, str]] = ...,
        doc: str = ...,
        allow_files: Union[bool, Sequence[str]] = ...,
        providers: Union[Sequence[Sequence[Provider]], Sequence[Provider]] = ...,
        mandatory: bool = ...,
        cfg: str = ...,
    ) -> Attribute: ...

    @staticmethod
    def output(
        doc: str = ...,
        mandatory: bool = ...,
    ) -> Attribute: ...

    @staticmethod
    def output_list(
        allow_empty: bool = ...,
        doc: str = ...,
        mandatory: bool = ...,
    ) -> Attribute: ...

    @staticmethod
    def string(
        default: str = ...,
        doc: str = ...,
        mandatory: bool = ...,
        values: Sequence[str] = ...,
    ) -> Attribute: ...

    @staticmethod
    def string_dict(
        allow_empty: bool = ...,
        default: Dict[str, str] = ...,
        doc: str = ...,
        mandatory: bool = ...,
    ) -> Attribute: ...

    @staticmethod
    def string_list(
        mandatory: bool = ...,
        allow_empty: bool = ...,
        default: Sequence[str] = ...,
        doc: str = ...,
    ) -> Attribute: ...

    @staticmethod
    def string_list_dict(
        allow_empty: bool = ...,
        default: Dict[str, List[str]] = ...,
        doc: str = ...,
        mandatory: bool = ...,
    ) -> Attribute: ...


class native:
    @staticmethod
    def glob(patterns: List[str]) -> List[str]: ...


class apple_common:
    multi_arch_split: str
    platform_type: PlatformType


class PlatformType:
    ios: Any
