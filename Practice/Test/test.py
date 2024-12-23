# Python Full Tutorial  

# Basic Print Statement  
print("Welcome to Python Full Tutorial!")  

# Variables and Data Types  
a = 10               # Integer  
b = 3.5              # Float  
name = "Shardendu"   # String  

print(a)  
print(b)  
print(name)  

# User Input  
user_input = input("Enter your favorite color: ")  
print("Your favorite color is:", user_input)  

# Basic Arithmetic Operations  
x = 20  
y = 5  

print(x + y)    # Addition  
print(x - y)    # Subtraction  
print(x * y)    # Multiplication  
print(x / y)    # Division  
print(x // y)   # Integer Division  
print(x % y)    # Modulus  
print(x ** 2)   # Exponentiation  

# Conditional Statements  
if x > y:  
    print(f"{x} is greater than {y}")  
elif x == y:  
    print(f"{x} is equal to {y}")  
else:  
    print(f"{x} is less than {y}")  

# Loops  
print("\n--- Loops ---")  
# For Loop  
for i in range(5):  
    print(i)  

# While Loop  
count = 0  
while count < 5:  
    print(count)  
    count += 1  

# Functions  
print("\n--- Functions ---")  
def greet(name):  
    return f"Hello, {name}!"  

print(greet("Student"))

# Advanced Functions  
def add(a, b):  
    return a + b  

def subtract(a, b):  
    return a - b  

print(add(10, 20))  
print(subtract(20, 10))  

# Lists  
print("\n--- Lists ---")  
my_list = [1, 2, 3, 4, 5]  
print(my_list)  

# Adding Elements  
my_list.append(6)  
print(my_list)  

# Removing Elements  
my_list.pop()  
print(my_list)  

# Slicing Lists  
print(my_list[1:4])  

# Tuples  
print("\n--- Tuples ---")  
my_tuple = (10, 20, 30)  
print(my_tuple)  

# Dictionaries  
print("\n--- Dictionaries ---")  
my_dict = {"name": "Shardendu", "age": 20, "city": "Kanpur"}  
print(my_dict)  

# Accessing Elements  
print(my_dict["name"])  

# Sets  
print("\n--- Sets ---")  
my_set = {1, 2, 3, 3, 4}  # Duplicates are automatically removed  
print(my_set)  

# Error Handling  
print("\n--- Error Handling ---")  
try:  
    result = 10 / 0  
except ZeroDivisionError:  
    print("Cannot divide by zero!")  

# File I/O (Reading and Writing)  
print("\n--- File I/O ---")  
with open('sample.txt', 'w') as file:  
    file.write("This is a sample text file created using Python.\n")  
    file.write("File handling operations are useful for managing data.")  

# Reading from a file  
with open('sample.txt', 'r') as file:  
    content = file.read()  
    print(content)  

# Classes and Objects  
print("\n--- Classes and Objects ---")  
class Person:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  

    def display(self):  
        return f"{self.name} is {self.age} years old."

person1 = Person("Shardendu", 20)  
print(person1.display())  

# Advanced Topics - Generators  
print("\n--- Generators ---")  
def my_generator():  
    for i in range(5):  
        yield i  

gen = my_generator()  
print(next(gen))  
print(next(gen))  

# Advanced Topics - Decorators  
print("\n--- Decorators ---")  
def decorator_function(original_function):  
    def wrapper_function():  
        print("Wrapper executed before the original function.")  
        return original_function()  
    return wrapper_function  

def display_message():  
    print("Display message executed.")  

decorated_display = decorator_function(display_message)  
decorated_display()  

print("\n--- End of Python Tutorial ---")