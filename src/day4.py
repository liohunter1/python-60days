# Day 4: Python Practice

print("Day 4 - Python 60 Days Challenge")
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#Syntax
#for variable in sequence:
    #code block
    #print(variable)
    #Example
courses = ["Python", "Java", "C++", "JavaScript"]
for course in courses:
     print(course)
     #Example 2 
     #Iterating over a range of numbers
for i in range(10):
    print(i)
    #indexed looping
    #Enumerate() function is used to loop through the iterable objects and provides an index to the items in the object.
    hacking_Tools = ["Nmap", "Wireshark", "Metasploit", "Burp Suite"]
    for index, tool in enumerate(hacking_Tools):
         print(f"{index}: {tool}")
#Looping with zip()     
#zip() function is used to combine two or more lists into a single list.
#Lab Question: Advanced zip() Implementation

#Scenario:
#You are a data analyst working with customer data from two different departments—Sales and Support. Each department provides monthly reports with customer details. Your task is to:

    #Merge data from both reports using zip() while handling cases where one report may have more entries than the other.
    #Identify discrepancies in customer satisfaction scores between the two departments.
    #Generate a summary report highlighting:
    #    Customer ID
     #   Sales satisfaction score
      #  Support satisfaction score
       # Difference in scores

#Sales and support report data
sales_report = [
     ("kca001", 7),
     ("kca002", 8),
     ("kca003", 6),
     ("kca004", 9),
     ("kca005", 5),
]
support_report = [
     ("kca001", 4),
     ("kca002", 10),
     ("kca003", 6),
     ("kca004", 8),
     ("kca005", 9)
]
#Merging data from both reports
for sales, support in zip(sales_report, support_report):
    sales_id, sales_score = sales
    support_id, support_score = support

    if sales_id == support_id:
         score_difference = abs(sales_score - support_score)
         print(f"Customer ID: {sales_id}")
         print(f"Sales satisfaction score: {sales_score}")
         print(f"Support satisfaction score: {support_score}")
         print(f"Difference in scores: {score_difference}")
         print("_" * 40)

         #While loops 
           #While loop is used to execute a block of code repeatedly as long as the condition is true.
           #Scenario:
           #User Aunthenication system
           #The user is prompted to enter their username and password.
correct_username = "Emilio"
correct_password = "Emilio123"
username = input("Enter your username: ")
password = input("Enter your password: ")
#Check if the username(case-insensitive) and password are correct
while username.lower() != correct_username.lower()  or password != correct_password:
    
    if username.lower() != correct_username.lower() and  password != correct_password:
         print("Invalid username and password. Try again.")

    elif username.lower()!= correct_username.lower():
           print("Invalid username. Try again.")
    elif password != correct_password:
           print("Invalid password. Try again.")
    #Prompt the user to enter their username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
print("Login successful")
          #Task: Brute-Force Detection System
          #Scenario:
          #You are building a brute-force detection system that tracks the number of failed login attempts. The system will lock the user out after three failed attempts.
import datetime
import time
username = "admin"
password = "secure123"
attempt = 0
max_attempts = 3
attempts_log = []
print("WELCOME TO THE LOGIN SYSTEM")
print("_" * 100)
while attempt < max_attempts:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    #capture current timestamp
    timestamp = datetime.datetime.now()
    #Log the access attempt
    attempts_log.append(f"TIMESTAMP:{timestamp}, USERNAME:{username_input}, PASSWORD:{password_input}")
    
    #Print the log
    print(attempts_log)
    if username_input == username and password_input == password:
        print("Access granted")
        break
    else:
        attempt += 1
        remaining_attempts = max_attempts - attempt
        if remaining_attempts > 0:
            print(f"Access denied. Remaining attempts are {remaining_attempts}. Try again ...")
            print("_" * 60)
        else:
            print("Access denied. Maximum attempts reached")    
            time.sleep(300)#lock the system for 5 minutes
             