from weather import describe_weather

def test_weather_description():
    result = describe_weather(10)
    assert result in ["Freeze", "Cold", "Pleasant", "Hot"] 