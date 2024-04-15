def contains_all_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels.issubset(set(string.lower()))

# Test the function
string = input("Enter a string: ")
if contains_all_vowels(string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")

