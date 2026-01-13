import pytest
import app.main as main


def test_negative_ages() -> None:
    assert main.get_human_age(-1, -10) == [0, 0]
    assert main.get_human_age(-15, 24) == [0, 2]


def test_should_raise_type_error_for_strings() -> None:
    with pytest.raises(TypeError):
        main.get_human_age("15", 20)

    with pytest.raises(TypeError):
        main.get_human_age(20, "20")


def test_should_raise_type_error_for_floats() -> None:
    with pytest.raises(TypeError):
        main.get_human_age(15.5, 20)

    with pytest.raises(TypeError):
        main.get_human_age(20, 24.0)
