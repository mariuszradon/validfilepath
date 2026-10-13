from .validfilepath import valid_filepath_input
from .validfilepath import valid_filepath_output

__all__ = [
    "valid_path_input_file",
    "valid_path_output_file",
]

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("validfilepath")
except PackageNotFoundError:
    __version__ = "unknown"
