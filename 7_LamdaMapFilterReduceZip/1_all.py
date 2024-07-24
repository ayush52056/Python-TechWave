# Lambda Functions: Lambda functions are small, anonymous functions defined with the lambda keyword.
square = lambda x: x * x
print("Square of 5:", square(5))
# This defines a lambda function that squares its input.
# square(5) - Calls the lambda function with 5 as the argument, returning 25.

# Map Function: The map function applies a given function to all items in an iterable (e.g., list)
# and returns a map object (which can be converted to a list).
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)
# This applies the lambda function to each item in the numbers list, returning a list of
# squared numbers.

# Filter Function: The filter function filters items in an iterable based on a given function and
# returns a filter object (which can be converted to a list).
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
# This filters the numbers list to include only even numbers.

# Reduce Function: The reduce function from the functools module applies a given function
# cumulatively to the items in an iterable, reducing it to a single value.
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)
# This sums up the numbers in the numbers list.

# Zip Function: The zip function combines items from multiple iterables (e.g., lists) into tuples,
# creating a zip object (which can be converted to a list).
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print("Combined list:", combined)
# This combines the names and ages lists into a list of tuples.