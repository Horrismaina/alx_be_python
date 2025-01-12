def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float: Result of the operation
        str: Error message in case of division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"