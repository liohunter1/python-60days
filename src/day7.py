# Day 7: Python Practice

print("Day 7 - Python 60 Days Challenge")
#Today we dive into Data Structures in Python
#Data structures are a way of organizing and storing data so that it can be accessed and modified efficiently.
#Python has several built-in data structures such as lists, tuples, sets, and dictionaries.
#Lists are ordered, mutable, and allow duplicate elements.
#Creating a list
courses = ["Networking", "Cybersecurity", "Programming", "Data Science"]
print(courses)
#Common List Methods
#1. append() - Adds an element to the end of the list
courses.append("Machine Learning")
print(courses)
#2. insert() - Adds an element at a specific position
courses.insert(2, "Web Development")
print(courses)
#3. remove() - Removes the first occurrence of the specified element
courses.remove("Programming")
print(courses)
#4. pop() - Removes the element at the specified index
courses.pop(3)
print(courses)
#Length of the list
print(len(courses))
#accesing elements in a list
print(courses[0]) #Networking
#5. clear() - Removes all elements from the list
courses.clear()
print(courses)
#List slicing
#Syntax: list_name[start:stop:step]
courses = ["Networking", "Cybersecurity", "Programming", "Data Science"]
print(courses[1:3]) #['Cybersecurity', 'Programming']
print(courses[::2]) #get every second element ['Networking', 'Programming']
#List comprehension
#List comprehension is a concise way to create lists in Python.
#Syntax: [expression for item in iterable if condition]
squared = [x**2 for x in range(10)]
print(squared) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#List comprehension with condition
even_numbers = [x for x in range(10) if x % 2 == 0] # this will give [0, 2, 4, 6, 8] because we are only taking even numbers
print(even_numbers)
#List comprehension with nested loops
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs) #[(0, 0), (0, 1), (1, 0), (1, 1)]
#List comprehension with if-else
numbers = [x if x % 2 == 0 else "odd" for x in range(10)] # this will give [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']
print(numbers)
#List comprehension with functions
def square(x):
    return x**2
squared = [square(x) for x in range(10)]
print(squared) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#List comprehension with strings
names = ["cybersecurity", "networking", "programming"]
uppercase_names = [name.upper() for name in names] #['CYBERSECURITY', 'NETWORKING', 'PROGRAMMING']
print(uppercase_names) #
#Password strength checker 
#Task 1: Password Strength Checker
#Create a Python program that checks the strength of a password.
my_passwords = []
weak_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "password1"]
password = input("Enter your password: ")
my_passwords.append(password)
print(my_passwords)
#check if the password is strong

def is_strong(password):
    if my_passwords == weak_passwords :
        return "Weak password! It is a common password."
    elif len(password) < 8:
        return "Weak password! It should be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak password! It should contain at least one digit."
    elif not any(char.isupper() for char in password):
        return "Weak password! It should contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Weak password! It should contain at least one lowercase letter."
    elif not any(char in "!@#$%^&*()_+" for char in password):
        return "Weak password! It should contain at least one special character."
    return "Strong Password"
#check the strength of the password
print(is_strong(password))
