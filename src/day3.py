# Day 3: Python Practice

print("Day 3 - Python 60 Days Challenge")

# Control flow
#If-Else Statements and logical operators
age = 22
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
    #Logical operators
    #AND, OR, NOT
    #AND - Returns True if both statements are true
#Scenario:
#A customer gets a 20% discount if they spend at least $100 and are a premium member.
amount_spent=float(input("Enter the amount spent:Ksh "))
premium =str(input("Are you a premium member? yes/no: "))
if amount_spent >= 100 and premium == "yes":
    print(f"You get a 20% discount")
else: 
    print("You do not qualify for the discount")
#Scenario:
#A user can successfully log in if:
#The username and password are correct.
#The account is active.
#My simulated logins are as follows :
username = "LIONEM"
password = "Emilio123"
active = True
if username == "LIONEM" and password == "Emilio123" and active == True:
    print("Login successful")
else:
    print("Login failed")
    #OR - Returns True if one of the statements is true
    #NOT - Reverse the result, returns False if the result is true
#Scenario:
#Only the admin can access the admin panel.
#The admin is identified by their username or email.
#The admin is not blocked.
admin = "Emilio"
user = "LIONEM"
Admin_email="Adminkenya@kmail.bom"
user_email="liopat@ovamail.com"
blocked = False
#Prompt the user to enter their username or email
username = str(input("Enter your username: "))
email = str(input("Enter your email: "))
if not (username != admin or email != Admin_email) and blocked == False:
    print("Access granted")
if not (username != user or email != user_email) and blocked == False:
    print("Access denied")
else:
    print("Access denied")
    #Updated Code (Using not Operator)

