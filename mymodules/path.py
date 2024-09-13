import inspect
import os
from pathlib import Path


def to_abs_path(fpath: str) -> str:
    dirpath = get_caller_path()
    return os.path.normpath(Path(dirpath) / fpath)


def get_caller_path() -> str:
    """関数呼び出しをたどり大元のディレクトリのパスを返す

    Returns
    -------
    str
        _description_
    """
    caller_frame = inspect.stack()[-1]
    caller_module = inspect.getmodule(caller_frame[0])

    caller_module_path = Path(caller_module.__file__).resolve()
    return caller_module_path.parent
