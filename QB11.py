#Find the length of string without using inbuilt fuction

def find_string_length(string):
    length = 0
    for _ in string:
        length += 1
    return length

# Test the function
input_string = input("Enter a string: ")
length = find_string_length(input_string)
print("Length of the string:", length)

