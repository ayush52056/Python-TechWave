# Lists:

# Definition: Lists are ordered, mutable collections of items.
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Append: Adds an item to the end of the list.
fruits.append("date")
print("After append:", fruits)

# Remove: Removes the first occurrence of a specified item.
fruits.remove("banana")
print("After remove:", fruits)

# Length: Returns the number of items in the list.
a= len(fruits)
print(f"length: {a}")


lst = [1, 2, 3, 4]
lst.append(5)
print(lst)                 # [1, 2, 3, 4, 5]
lst.extend([6, 7])
print(lst)                 # [1, 2, 3, 4, 5, 6, 7]
lst.insert(0, 0)
print(lst)                 # [0, 1, 2, 3, 4, 5, 6, 7]
lst.remove(3)
print(lst)                 # [0, 1, 2, 4, 5, 6, 7]
print(lst.pop(0))          # 0
print(lst)                 # [1, 2, 4, 5, 6, 7]
print(lst.index(4))        # 2
print(lst.count(2))        # 1
lst.sort()
print(lst)                 # [1, 2, 4, 5, 6, 7]
lst.reverse()
print(lst)                 # [7, 6, 5, 4, 2, 1]
