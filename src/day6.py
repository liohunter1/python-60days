# Day 6: Python Practice

print("Day 6 - Python 60 Days Challenge")
#main.py
from day5 import celsius_to_fahrenheit, fahrenheit_to_celsius
# Ask the user to choose the conversion type
conversion_type = input("Choose the conversion type (Celsius to Fahrenheit or Fahrenheit to Celsius): ").lower().strip()
#take inputs and perform the conversion and print the result
if conversion_type == "celsius to fahrenheit":
    celsius = float(input("Enter the temprature in Celcius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif conversion_type == "fahrenheit to celsius":
    fahrenheit = float(input("Enter the temprature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid conversion type")
    #Taccountmain.py
from day5 import BankAccount
#Create a bank account object
account = BankAccount("Emilio", "123456")
#Deposit some money
account.deposit(5000)
#Withdraw some money
account.withdraw(2000)
#Get the account balance
balance = account.get_balance()
print(f"The account balance is Ksh {balance}")
