from dataclasses import dataclass

@dataclass
class TemperatureConverter:
    def convert_temperature(self, temperature, from_unit, to_unit):
        valid_units = ["C", "F", "K"]

        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError("Invalid temperature units. Valid units are 'C' (Celcius), 'F' (Farenheit), and 'K' (Kelvin)")
        
        if not isinstance(temperature, (int, float)) or temperature < -273.15:
            raise ValueError("Temperature must be a number greater than or equal to -273.15 (Absolute zero)")
        
        if from_unit == "C":
            if to_unit == "F":
                return (temperature * 9/5) + 32
            elif to_unit == "K":
                return temperature + 273.15
            else:
                return temperature
            
        elif from_unit == "F":
            if to_unit == "C":
                return (temperature - 32) * 5/9
            elif to_unit == "K":
                return ((temperature - 32)/1.8) + 273.15
            else:
                return temperature
        else:
            if to_unit == "C":
                return temperature - 273.15
            elif to_unit == "F":
                return (temperature - 273.15) * 9/5 + 32
            else:
                return temperature