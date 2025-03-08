# Day 2: Python Practice

print("Day 2 - Python 60 Days Challenge")
# String Manipulation
#4. Accessing First or Last Characters
#Common in parsing tasks or validating input.
code = "TECHXYZ2025"
print(code[:4]) 
print (code[-4:])
#Task 1: Validate Product Codes
#Write a Python program to validate a list of product codes based on the following rules:

#Each product code must:
#Be exactly 8 characters long.
#Start with two uppercase letters (product category).
#End with two digits (year of manufacture).
product_codes = ["EL1234501", "FD9876523", "cl4567819", "XT987654"]
for code in product_codes:
    if (len(code) == 8) and code[:2].isupper() and code[-2:].isdigit():
        print(code + "is valid product code ")
    else:
        print (code + "is invalid product code ")

# Service code validation
#Task 2: Filter Products by Year
#Implement a function to filter and display products manufactured in a specific year.

#Requirements:

#The user should input a year (e.g., 2023), and the program should display all products from that year.
Service_codes = ["SR12345", "SR98765", "sr45678", "SR98765"]
year= input("Enter the year: ")
year = str(year)
print(f"Services Offered in {year}")
for code in Service_codes:
    if code[-2:].isdigit() and year[-2:] == code[-2:]:
       print(f"Service code: {code} (Category: {code[:2]})")

#Task 3: Count Products by Category
#Create a script to count how many products belong to each category.
#Initialize category for code in product_codes: to store the count of each category.
print("\nProduct Counts by Category:")
print("-" * 30)

category_count = {}
# Count products by category
for code in product_codes:
    if len(code) >= 2:  # Ensure code has at least 2 characters
        category = code[:2].upper()  # Convert to uppercase for consistency
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

# Display results
for category, count in category_count.items():
    print(f"{category}: {count} product{'s' if count > 1 else ''}")




