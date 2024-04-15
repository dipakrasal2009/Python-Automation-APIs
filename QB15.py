#Write a Python program to create tuple of n numbers, print the first half values oftuple in one line and the last half values of tuple on next line.




def split_tuple(numbers):
    # Calculate the midpoint of the tuple
    midpoint = len(numbers) // 2

    # Print the first half values of the tuple
    print("First half values of the tuple:")
    print(*numbers[:midpoint])

    # Print the last half values of the tuple
    print("Last half values of the tuple:")
    print(*numbers[midpoint:])

# Input number of elements in the tuple
n = int(input("Enter the number of elements in the tuple: "))

# Input the elements of the tuple
print("Enter the elements of the tuple:")
numbers = tuple(map(int, input().split()))[:n]

# Call the function to split and print the tuple
split_tuple(numbers)

