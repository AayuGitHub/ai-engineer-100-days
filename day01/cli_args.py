import sys

# Check whether exactly two arguments are provided
if len(sys.argv) != 3:
    print("Error: Please provide exactly two arguments: name and age.")
    sys.exit(1)

name = sys.argv[1]
age = sys.argv[2]

# validate name
if not name.strip():
    print("Error: Name cannot be empty.")
    sys.exit(1)

# Convert age string into integer
try:
    age = int(age)  
except ValueError:
    print("Error: Age must be a valid integer.")
    sys.exit(1)

# Validate age range
if age < 0:
    print("Error: Age cannot be negative.")
    sys.exit(1)

# print greeting only when all validation pass
print(f"Hello, {name}! You are {age} years old.")