import os

print("\t\t\t\t My Menu Project ")
print("\t\t\t\t------------------")

print("""press 1 : to open the terminal
        press 2 : to open the text editor (gedit)
        press 3 : to open the web browser (firefox)
        press 4 : to open the file manager (nautilus)
        press 5 : to open system settings
        """)
ch = input("Enter your choice: ")

if "terminal" in ch:
    os.system("gnome-terminal")
elif "editor" in ch:
    os.system("gedit")
elif "firefox" in ch:
    os.system("firefox")
elif "files" in ch:
    os.system("nautilus")
elif "settings" in ch:
    os.system("gnome-control-center")
else:
    print("Invalid choice")
