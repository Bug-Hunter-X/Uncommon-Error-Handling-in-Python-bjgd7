def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "TypeError: unsupported operand type(s) for /: 'str' and 'int'"
except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"
except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: ZeroDivisionError: division by zero
print(function_with_uncommon_error(10, "hello")) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_uncommon_error(10, [1,2])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list'