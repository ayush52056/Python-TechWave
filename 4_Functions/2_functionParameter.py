# Function Parameters:

# Positional Parameters: Parameters are assigned based on their position in the function call.
def subtract(a, b):
    return a - b
result = subtract(10, 5)  # a = 10, b = 5

# Keyword Parameters: Parameters are assigned based on their names in the function call.
result = subtract(b=5, a=10)  # a = 10, b = 5

# Default Parameters: Parameters with default values. If not provided, the default value is used.
def multiply(a, b=2):
    return a * b
result = multiply(5)  # a = 5, b = 2
