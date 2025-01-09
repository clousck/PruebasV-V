from TemperatureConverter import TemperatureConverter
import pytest

@pytest.fixture
def converter():
    return TemperatureConverter()

def test_convert_celsius_to_fahrenheit(converter):
    assert converter.convert_temperature(0, "C", "F") == 32

def test_convert_celsius_to_kelvin(converter):
    assert converter.convert_temperature(0, "C", "K") == 273.15

def test_convert_fahrenheit_to_celsius(converter):
    assert converter.convert_temperature(32, "F", "C") == 0

def test_convert_fahrenheit_to_kelvin(converter):
    assert converter.convert_temperature(32, "F", "K") == 273.15

def test_convert_kelvin_to_celsius(converter):
    assert converter.convert_temperature(273.15, "K", "C") == 0

def test_convert_kelvin_to_fahrenheit(converter):
    assert converter.convert_temperature(273.15, "K", "F") == pytest.approx(32, abs=0.01)

def test_invalid_temperature_units(converter):
    with pytest.raises(ValueError) as error:
        converter.convert_temperature(0, "x", "C")
    assert str(error.value) == "Invalid temperature units. Valid units are 'C' (Celcius), 'F' (Farenheit), and 'K' (Kelvin)"

def test_invalid_temperature_range(converter):
    with pytest.raises(ValueError) as error:
        converter.convert_temperature(-300, "C", "F")
    assert str(error.value) == "Temperature must be a number greater than or equal to -273.15 (Absolute zero)"

def test_convert_decimal_temperatures(converter):
    assert converter.convert_temperature(0.5, "C", "F") == pytest.approx(32.9 , abs=0.01)
    assert converter.convert_temperature(0.5, "F", "C") == pytest.approx(-17.5 , abs=0.01)

def test_convert_same_units(converter):
    assert converter.convert_temperature(100, "C", "C") == 100
    assert converter.convert_temperature(100, "F", "F") == 100
    assert converter.convert_temperature(100, "K", "K") == 100