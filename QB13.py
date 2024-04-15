
#Write a Python program to create a tuple of n numbers and print maximum, minimum,and sum of elements in a tuple.



def tuple_stats(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    sum_num = sum(numbers)
    return max_num, min_num, sum_num

# Input number of elements in the tuple
n = int(input("Enter the number of elements in the tuple: "))

# Input the elements of the tuple
print("Enter the elements of the tuple:")
numbers = tuple(int(input()) for _ in range(n))

# Calculate maximum, minimum, and sum of the elements in the tuple
max_num, min_num, sum_num = tuple_stats(numbers)

# Print the results
print("Maximum element in the tuple:", max_num)
print("Minimum element in the tuple:", min_num)
print("Sum of elements in the tuple:", sum_num)

