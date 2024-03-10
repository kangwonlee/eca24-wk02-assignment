import math
import pathlib
import random
import sys
from typing import Tuple

import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import wk02


random.seed()


@pytest.fixture
def prime_below_100() -> Tuple[int]:
    # https://thirdspacelearning.com/us/blog/what-is-a-prime-number/
    return (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


@pytest.fixture
def area(prime_below_100:Tuple[int]) -> int:
    while True:
        a = random.randint(50, 100)
        if a not in prime_below_100:
            return a


@pytest.fixture
def w_h(area:int) -> Tuple[int]:
    max_w = int(math.sqrt(area))
    for w in range(max_w, 1, -1):
        if area % w == 0:
            return (w, area // w)


@pytest.fixture
def result(w_h:Tuple[int]) -> int:
    return wk02.wk02(*w_h)


def test_wk02(result:int, w_h:Tuple[int], area:int):
    assert result == area, f"result={result}, (w, h)={w_h}, area={area}"
