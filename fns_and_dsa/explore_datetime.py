from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get and display the current date and time.
    Returns the current date for potential future use.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    """
    Calculate and display a future date based on user input.
    Args:
        current_date: datetime object representing the current date
    Returns:
        datetime object representing the future date
    """
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Get and display current datetime
    current_date = display_current_datetime()
    
    # Calculate and display future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()