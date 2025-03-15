# Day 8: Python Practice

print("Day 8 - Python 60 Days Challenge")
#Rest of Data structures in Python
#Tuples
#Tuples are ordered and immutable collections of elements.
#Creating a tuple
courses = ("Networking", "Cybersecurity", "Programming", "Data Science")
print(courses)
#Tuple Operations
#Accessing elements in a tuple
print(courses[0]) #Networking
#Tuple slicing
print(courses[1:3]) #('Cybersecurity', 'Programming')
#Length of a tuple
print(len(courses))
#Unpacking a tuple
course1, course2, course3, course4 = courses
print(course1) #Networking
print(course2) #Cybersecurity
#concatenating tuples
courses += ("Machine Learning", "Web Development")
print(courses)
#repetition
print(courses * 2
)
#Scenarios where tuples are preferred over lists
#1. When the data should not be changed
#2. When the data is accessed frequently
#3. When the data is used for iteration
#Example 
#Immutable Logs- Foresics evidence
#Creating a tuple of IIS logs
logs1 = ("2023-01-01", "10:30:00", "Failed login attempt", " 192.168.1.42")
logs2 = ("2023-01-01", "10:35:00", "Successful login", "192.168.1.42")
logs3 = ("2023-01-01", "10:40:00", "Failed login attempt", "192.168.1.42")
#LOG STORAGE (tuples of tuples )
log_storage = (logs1, logs2, logs3)
for log in log_storage:
    print(log)
    #Scenario you have the log entries above and want to analyze unauthorized access
    #Create a script to filter and display failed login attempts
    target_ip = "192.168.1.42"
    #Extract failed login attempts
    print("\nUnauthorized Access Attempts:")
    print("-" * 30)
    for log in log_storage:
        if log[2] == "Failed login attempt" and log[3] == target_ip:
            print(log)
#Enforce Read only access
credentials = (
    ("admin", "afff56@#", "root"),
    ("analyst", "fghj56@#", "user")
)
def check_access(username, required_role):
    for user,_ , role in credentials:
        if user == username and role == required_role:
            return True
    return False
print(check_access("admin", "root")) #True
print(check_access("analyst", "root")) #False
#Sets
#Sets are unordered collections of unique elements
#Creating a set
#Creating a set using curly braces
malicious_ips = {"192.168.1.10", "10.0.0.8", "192.168.1.42"}
print(malicious_ips)
#Creating a set using set() constructor
Active_IPs = set()
Active_IPs.add(input("Enter IP Address: "))
print(Active_IPs)
#Set Operations
#Adding elements to a set
Active_IPs.add(input("Enter IP Adress") )
#Remove elements from a set
if Active_IPs:  # Check if set is not empty
    first_ip = next(iter(Active_IPs))
    Active_IPs.discard(first_ip)
print(Active_IPs)

#Dictionaries 
#An unordered, mutable collection of key-value pairs
#Dictionaries in Python are key-value pairs that provide fast and efficient data storage and retrieval
#critical for tasks like logging, access control, and incident tracking in cybersecurity.
#Creating a dictionary 
user_info = {
    "username":"Emilio",
    "role": "Root",
    "acess_level": 5
}
print(user_info) 
