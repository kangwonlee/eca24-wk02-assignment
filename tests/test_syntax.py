import ast
import os
import pathlib

from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()

proj_folder = pathlib.Path(
    os.getenv(
        'STUDENT_CODE_FOLDER',
        test_folder.parent.absolute()
    )
)


def py_files() -> Tuple[pathlib.Path]:
    return tuple(proj_folder.glob("*.py"))


@pytest.mark.parametrize("py_file", py_files())
def test_syntax(py_file:pathlib.Path):
    
    code = py_file.read_text(encoding="utf-8")
    
    try:
        ast.parse(code)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in file: {py_file}\n{e}")
