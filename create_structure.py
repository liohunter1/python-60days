import os

# Base project directory
base_dir = os.getcwd()

# Directory structure for the Python 60-Day Challenge
folders = [
    "src",                     # Source code
    "tests",                   # Unit tests
    "resources",               # Learning materials
    "src/projects",            # Major projects
    "src/projects/calculator", # Day 5-6: Calculator Project
    "src/projects/todo_app",   # Day 7-8: To-Do List Project
    "src/projects/contact_book", # Day 9-10: Contact Book Project
    "src/projects/banking_system", # Day 14-15: Banking System
    "src/projects/weather_app",    # Day 18-20: Weather App
    "src/projects/student_manager", # Day 24-25: Student Manager
    "src/projects/personal_diary",  # Day 28-30: Personal Diary
    "src/projects/simple_blog",     # Day 31-35: Blog App
    "src/projects/task_manager",    # Day 38-40: Task Manager
    "src/projects/api_visualizer",  # Day 44-46: API Visualizer
    "src/projects/file_organizer",  # Day 47-50: File Organizer
    "src/projects/capstone_project", # Day 51-60: Final Capstone
]

# Create folders
for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Created: {path}")

# Generate daily practice files (day1.py to day60.py)
for day in range(1, 61):
    file_path = os.path.join(base_dir, "src", f"day{day}.py")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f'# Day {day}: Python Practice\n\nprint("Day {day} - Python 60 Days Challenge")\n')
        print(f"Created: {file_path}")

# Create initial files
init_files = ["README.md", "requirements.txt"]
for file in init_files:
    file_path = os.path.join(base_dir, file)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f"# Python 60-Day Challenge\n\nTracking Python learning from Day 1 to Day 60.\n")
        print(f"Created: {file_path}")

print("\n✅ Python 60-Day Folder Structure Created Successfully!")
 
