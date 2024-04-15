# Define a set
my_set = {3, 5, 2, 8, 1, 9}

# Calculate the sum of all elements
sum_of_elements = sum(my_set)

# Calculate the total number of elements
num_elements = len(my_set)

# Calculate the average
average = sum_of_elements / num_elements if num_elements != 0 else 0  # Avoid division by zero

# Print the average
print("Average of all elements in the set:", average)

