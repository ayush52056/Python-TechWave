# Defining a function
def greet(name):
    """This function greets the person passed as a parameter"""
    print(f"Hello, {name}!")

# Calling a function
greet("Alice")
greet("Bob")

# Function with return value
def add(a, b):
    """This function returns the sum of two numbers"""
    return a + b

result = add(3, 5)
print("Sum:", result)
