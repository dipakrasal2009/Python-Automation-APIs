#Write a Python program to accept and convert string in uppercase or vice versa.



def convert_case(string):
    # Check if the string is in lowercase
    if string.islower():
        return string.upper()  # Convert to uppercase
    # Check if the string is in uppercase
    elif string.isupper():
        return string.lower()  # Convert to lowercase
    else:
        return string  # Return the string unchanged if it's not all lowercase or all uppercase

# Input a string from the user
input_string = input("Enter a string: ")

# Convert the case of the string
converted_string = convert_case(input_string)

# Print the converted string
print("Converted string:", converted_string)

