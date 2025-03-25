# Day 9: Python Practice

print("Day 9 - Python 60 Days Challenge")
# Write a Python program to store and retrieve user credentials securely.
import hashlib

def save_credentials(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    filename = "User_credentials.txt"
    
    try:
        with open(filename, "a") as uc:  # Changed to append mode
            uc.write(f"{username}:{hashed_password}\n")
        print("User credentials saved successfully")
    except Exception as e:
        print(f"Error saving credentials: {e}")

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    save_credentials(username, password)

if __name__ == "__main__":
    main()



