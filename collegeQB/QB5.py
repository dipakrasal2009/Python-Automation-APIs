# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Set difference
difference_set = set1 - set2 
# Elements present in set1 but not in set2

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2) 
# Elements present in either set1 or set2, but not in both

# Print the results
print("Set difference (set1 - set2):", difference_set)
print("Symmetric difference:", symmetric_difference_set)

