def function_with_improved_error_handling(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
        return None  # Or raise the exception for more detailed debugging
    return result

# Example usage:
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Cannot divide by zero.
None
print(function_with_improved_error_handling(10, "a")) # Output: Error: Invalid input type.
None
print(function_with_improved_error_handling(10, [1,2])) # Output: An unexpected error occurred: TypeError - unsupported operand type(s) for /: 'int' and 'list'
None