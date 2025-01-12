# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT = 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT

def main():
    try:
        # Get temperature input
        temp_str = input("Enter the temperature to convert: ")
        temp = float(temp_str)
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Perform conversion
        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            print("Invalid unit. Please enter C or F.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()