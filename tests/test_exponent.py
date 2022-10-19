from src.calculator import exponent
import pytest


def test_exponent_positive():
    result = exponent(4, 2)
    assert result == 16


def test_exponent_negative():
    result = exponent(4, -2)
    assert result == 1/16


def test_exponent_string():
    with pytest.raises(TypeError):
        exponent("string", 4)