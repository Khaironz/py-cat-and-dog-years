import pytest
import app.main as main
from typing import List


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),

        (27, 0, [2, 0]),
        (28, 0, [3, 0]),
        (0, 28, [0, 2]),
        (0, 29, [0, 3]),

        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: List[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_return_type() -> None:
    result: List[int] = main.get_human_age(
        20,
        20
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
