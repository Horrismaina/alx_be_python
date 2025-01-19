# robust_division_calculator.py
def safe_divide(numerator, denominator):
    """
    Safely performs division with comprehensive error handling.
    
    Args:
        numerator: The number to be divided (string or number)
        denominator: The number to divide by (string or number)
        
    Returns:
        str: A message indicating the result or describing any errors encountered
    """
    try:
        # Convert inputs to float, catching any non-numeric values
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division, catching division by zero
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
            
    except ValueError:
        return "Error: Please enter numeric values only."

# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 2")
        sys.exit(1)
    
    # Get numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform division and display result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
    