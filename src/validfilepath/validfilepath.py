import argparse
import os

def valid_filepath_input(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(
            f"File not found: {path}"
        )
    return path

def valid_filepath_output(path):
    dir_name, file_name = os.path.split(path)
    if not dir_name:
        dir_name = '.'
    # make sure parent directory exists
    if not os.path.exists(dir_name):
        raise argparse.ArgumentTypeError(
            f'File {path} cannot be created ' + \
            'as its parent directory does not exist: {dir_name}'
        )
    # make sure parent directory is writable
    if not os.access(dir_name, os.W_OK):
        raise argparse.ArgumentTypeError(
            f'Parent directory is not writable: {dir_name}'
        )
    # make sure path is not directory
    if os.path.isdir(path):
        raise argparse.ArgumentTypeError(
            f'Path is directory: {path}'
        )
    # if a file exists, make sure it is writable
    if os.path.exists(path):
        if not os.access(path, os.W_OK):
            raise argparse.ArgumentTypeError(
                f'File exists and cannot be written: {path}'
            )
    return path
