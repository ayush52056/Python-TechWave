# Example of list comprehension
squares = [x * x for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Creating a 3x3 matrix
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Flattening a list of lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
