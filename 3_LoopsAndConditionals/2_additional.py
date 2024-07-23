# If-Else Statement
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
total = 0
while total <= 10:
    print(total)
    total += 1

# Nested Loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
