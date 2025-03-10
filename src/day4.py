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