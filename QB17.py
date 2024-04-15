#Write a Python program to calculate the average of numbers in a given list.




def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Input list of numbers
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]

# Calculate the average
average = calculate_average(numbers)

# Print the average
if average is not None:
    print("Average:", average)
else:
    print("List is empty. Cannot calculate average.")

