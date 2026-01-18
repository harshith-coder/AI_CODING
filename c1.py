# Get input from the user for a list of numbers
numbers_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers or floats
try:
    numbers = [float(num) for num in numbers_str.split()]
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    numbers = [] # Set an empty list in case of error

# Extract negative numbers
negative_numbers = [num for num in numbers if num < 0]

# Create a new list without negative numbers
non_negative_numbers = [num for num in numbers if num == 0 or num>0]

print(f"Original list: {numbers}")
print(f"Negative numbers: {negative_numbers}")
print(f"List without negative numbers: {non_negative_numbers}")