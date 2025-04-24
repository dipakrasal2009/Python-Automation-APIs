# pip install pywhatkit
import pywhatkit as kit
#this is a module that is use in whatspp 

# Specify the phone numebr with the country code 
phone_number = input("enter the mobile number : ")

#enter the message that you want to send the perticular numeber
message = input("enter the message that you want to send :")

# Send the message instantly
status = kit.sendwhatmsg_instantly(phone_number, message) 
