# Arbitrary Arguments (*args): Allows a function to accept any number of positional arguments.
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")
greet_all("Alice", "Bob", "Charlie")

# Keyword Arguments (**kwargs): Allows a function to accept any number of keyword arguments.
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25, city="Wonderland")
