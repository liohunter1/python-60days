# Day 5: Python Practice

print("Day 5 - Python 60 Days Challenge")
# functions and modularization
# A function is a block of code that performs a specific task when called.
# Functions help in modularizing code, making it reusable and easier to read.
#Task 1: Temperature Converter
#Create a modular Python program to convert temperatures between Celsius and Fahrenheit.
#converter.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#Task 2 
#Create a modular Python program that simulates basic bank account operations.
#account.py
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


