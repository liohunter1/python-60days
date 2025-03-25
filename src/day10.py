# Day 10: Python Practice

print("Day 10 - Python 60 Days Challenge")
#Write a script that checks if a file has been modified by comparing its hash.
import os
import hashlib

# Function to compute file hash using SHA256
def compute_file_hash(filename):
    try:
        with open(filename, "rb") as file:
            file_content = file.read()
            hashed = hashlib.sha256(file_content).hexdigest()  # SHA256 hash
        return hashed
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Function to store hashes in a file (hashes.txt)
def store_hash(filename, hash_value):
    try:
        with open("hashes.txt", "a") as hash_file:
            hash_file.write(f"{filename}:{hash_value}\n")
    except Exception as e:
        print(f"❌ Error storing hash: {e}")

# Function to check file integrity
def check_file_integrity(filename):
    current_hash = compute_file_hash(filename)
    if current_hash is None:
        return False

    try:
        with open("hashes.txt", "r") as hash_file:
            hashes = hash_file.readlines()
            
            # Search for filename in hash records
            for line in hashes:
                stored_filename, stored_hash = line.strip().split(":")
                if stored_filename == filename:
                    if stored_hash == current_hash:
                        print(f"✅ File '{filename}' is intact.")
                        return True
                    else:
                        print(f"⚠️ ALERT! File '{filename}' has been modified!")
                        return False
            
            # If file is not found in hashes.txt, store its hash
            print(f"📝 No previous hash found for '{filename}'. Storing new hash...")
            store_hash(filename, current_hash)
            return True
            
    except FileNotFoundError:
        print("📝 Hash file not found. Creating new hash file...")
        store_hash(filename, current_hash)
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

# Function to create a test file
def create_test_file(filename, content="Test content"):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error creating test file: {e}")
        return False

# Test script
if __name__ == "__main__":
    test_file = "test_file.txt"
    
    print("\n🔍 Starting File Integrity Tests")
    print("=" * 40)
    
    # Test 1: Non-existent file
    print("\n📋 Test 1: Non-existent file")
    check_file_integrity("nonexistent.txt")
    
    # Test 2: Create and check new file
    print("\n📋 Test 2: New file check")
    if create_test_file(test_file):
        check_file_integrity(test_file)
    
    # Test 3: Check unmodified file
    print("\n📋 Test 3: Unmodified file check")
    check_file_integrity(test_file)
    
    # Test 4: Check modified file
    print("\n📋 Test 4: Modified file check")
    if create_test_file(test_file, "Modified content"):
        check_file_integrity(test_file)
    
    # Cleanup
    try:
        os.remove(test_file)
        os.remove("hashes.txt")
        print("\n🧹 Cleanup completed")
    except Exception as e:
        print(f"\n⚠️ Cleanup error: {e}")
