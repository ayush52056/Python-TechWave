# Class in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Objects in Python
dog = Animal("Buddy")  # This will raise an error because Animal is not meant to be instantiated directly
cat = Animal("Whiskers")  # Same as above

print(dog.speak())
print(cat.speak())