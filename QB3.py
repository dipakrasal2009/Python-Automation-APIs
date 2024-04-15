def find_repeated_items(my_tuple):
    repeated_items = []
    seen_items = set()

    for item in my_tuple:
        if item in seen_items:
            if item not in repeated_items:
                repeated_items.append(item)
        else:
            seen_items.add(item)

    return repeated_items

# Example tuple
my_tuple = (1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 3)

# Find repeated items
repeated_items = find_repeated_items(my_tuple)

# Print the repeated items
if repeated_items:
    print("Repeated items:", repeated_items)
else:
    print("No repeated items found.")

