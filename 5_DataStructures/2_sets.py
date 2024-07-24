# Sets

# Definition: Sets are unordered collections of unique items.
unique_numbers = {1, 2, 3, 4, 4, 5}
print("Original set:", unique_numbers)

# Add: Adds an item to the set.
unique_numbers.add(6)
print("After add:", unique_numbers)

# Remove: Removes a specified item.
unique_numbers.remove(3)
print("After remove:", unique_numbers)

# Length: Returns the number of items in the set.
print("Set length:", len(unique_numbers))


s = {1, 2, 3, 4}
s.add(5)
print(s)                 # {1, 2, 3, 4, 5}
s.update([6, 7])
print(s)                 # {1, 2, 3, 4, 5, 6, 7}
s.remove(3)
print(s)                 # {1, 2, 4, 5, 6, 7}
s.discard(2)
print(s)                 # {1, 4, 5, 6, 7}
print(s.pop())           # Removes and returns an arbitrary element
print(s)                 # Remaining elements in the set
s.clear()
print(s)                 # set()
