user_name = "Yazeed"
user_age = 25

def greet_user(name, age):
    print(f"Hello, {name}. You are {age} years old.")

def add_two_numbers(a, b):
    return a + b

total = add_two_numbers(5, 10)
print(total)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
person = Person(user_name, user_age)
person.display_details()
