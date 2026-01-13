import pytest
import app.main as main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -10, [0, 0]),
        (-15, 24, [0, 2]),
    ],
)
def test_negative_ages(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 20),
        (20, "20"),
        (15.5, 20),
        (20, 24.0),
    ],
)
def test_invalid_types_raise_type_error(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
