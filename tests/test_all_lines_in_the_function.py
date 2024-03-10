import pathlib

from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


def py_files() -> Tuple[pathlib.Path]:
    return tuple(proj_folder.glob("*.py"))


@pytest.mark.parametrize("py_file", py_files())
def test_function_only_in_py_file(py_file:pathlib.Path):
    with open(py_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line_strip = line.strip()
        if line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
            continue
        if line.startswith('def ') and line_strip.endswith(':'):
            continue
        assert line.startswith(' ') or line == ''
