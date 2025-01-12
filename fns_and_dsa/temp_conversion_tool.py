# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_ADJUSTMENT = 32

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    try:
        return (float(fahrenheit) - FREEZING_POINT_ADJUSTMENT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature value")

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    try:
        return (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_ADJUSTMENT
    except ValueError:
        raise ValueError("Invalid temperature value")

def main():
    try:
        # Get temperature from user
        temp = input("Enter the temperature to convert: ")
        
        # Validate temperature input
        try:
            temperature = float(temp)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Get unit from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Validate unit input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Perform conversion based on input unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()