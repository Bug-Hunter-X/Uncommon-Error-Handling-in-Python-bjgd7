def function_with_uncommon_error(a, b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
          if b == 0:
            raise ZeroDivisionError("Division by zero")
          result = a / b
          return result
        else:
          raise TypeError("Unsupported operand type(s)")
    except TypeError:
        return "TypeError: unsupported operand type(s)"
except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"
except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: ZeroDivisionError: division by zero
print(function_with_uncommon_error(10, "hello")) # Output: TypeError: unsupported operand type(s)
print(function_with_uncommon_error(10, [1,2])) # Output: TypeError: unsupported operand type(s)
print(function_with_uncommon_error("hello",10)) # Output: TypeError: unsupported operand type(s)