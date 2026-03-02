"""Tests for utils module - the instructor deletes this file to show coverage drop."""

import pytest
from src.utils import format_result, validate_input, calculate_percentage, round_to_decimal


def test_format_result():
    assert format_result("+", 2, 3, 5) == "2 + 3 = 5"
    assert format_result("*", 4, 5, 20) == "4 * 5 = 20"


def test_validate_input():
    assert validate_input(5) is True
    assert validate_input(3.14) is True
    with pytest.raises(TypeError):
        validate_input("not a number")


def test_calculate_percentage():
    assert calculate_percentage(50, 200) == 25.0
    assert calculate_percentage(1, 3) == pytest.approx(33.333, rel=1e-2)
    with pytest.raises(ValueError):
        calculate_percentage(5, 0)


def test_round_to_decimal():
    assert round_to_decimal(3.14159, 2) == 3.14
    assert round_to_decimal(3.14159, 4) == 3.1416
    assert round_to_decimal(3.5, 0) == 4
