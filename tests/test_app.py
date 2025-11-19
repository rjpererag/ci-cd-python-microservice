import pytest
from src.app import calculate_average_price, greeting

def test_greeting_success():
    assert greeting(name="Tutor") == "Hello, Tutor!"

def test_calculate_average_success():
    prices = [10.5, 20.5, 30.0]
    assert calculate_average_price(prices=prices) == pytest.approx(20.333333, abs=1e-6)

def test_calculate_average_empty():
    assert calculate_average_price(prices=[]) == 0.0

def test_calculate_average_forbidden_price():
    prices = [10.0, 13.0, 20.0]
    with pytest.raises(ValueError, match="forbidden value"):
        calculate_average_price(prices)