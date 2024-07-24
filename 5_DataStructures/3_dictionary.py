# Dictionaries

# Definition: Dictionaries are collections of key-value pairs.
student = {"name": "Alice", "age": 25, "city": "Wonderland"}
print("Original dictionary:", student)

# Update: Changes the value of a specified key.
student["age"] = 26
print("After update:", student)

# Add: Adds a new key-value pair.
student["course"] = "Computer Science"
print("After adding new key:", student)

# Delete: Removes a key-value pair.
del student["city"]
print("After deleting key:", student)

# Length: Returns the number of key-value pairs.
print("Dictionary length:", len(student))


d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])             # 1
print(len(d))             # 3
print('a' in d)           # True
print(d.keys())           # dict_keys(['a', 'b', 'c'])
print(d.values())         # dict_values([1, 2, 3])
print(d.items())          # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(d.get('a'))         # 1
d.update({'d': 4})
print(d)                  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.pop('a'))         # 1
print(d)                  # {'b': 2, 'c': 3, 'd': 4}
print(d.popitem())        # ('d', 4)
print(d)                  # {'b': 2, 'c': 3}
d.clear()
print(d)                  # {}
