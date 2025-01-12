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
    return (fahrenheit - FREEZING_POINT_ADJUSTMENT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_ADJUSTMENT

def get_valid_temperature():
    """
    Get a valid temperature input from the user.
    
    Returns:
        float: Valid temperature value
    
    Raises:
        ValueError: If input is not a valid number
    """
    temp = input("Enter the temperature to convert: ")
    try:
        return float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_valid_unit():
    """
    Get a valid temperature unit from the user.
    
    Returns:
        str: 'C' for Celsius or 'F' for Fahrenheit
    """
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit in ['C', 'F']:
            return unit
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    try:
        # Get temperature and unit from user
        temperature = get_valid_temperature()
        unit = get_valid_unit()
        
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