from unittest.mock import patch
from weather import describe_weather

def test_hot_weather():
    with patch('weather.get_temperature', return_value=30):
        assert result == "Hot"

def test_freezing_weather():
    with patch('weather.get_temperature', return_value=-5):
        assert result == "Freeze"