import os
import pywhatkit as kit
from twilio.rest import Client
import qrcode
import yagmail
import schedule
import time

print("\t\t\t\t My Menu Project ")
print("\t\t\t\t------------------")

print("""press 1 : for sending the whatsapp nessage.
        press 2 : for sending the SMS message.
        press 3 : for generate the qr code.
        press 4  : making the call.
        press 5 : to send the email
        """)

ch = input("Enter your choice: ")

if  int(ch) == 1:

    print("Please , Enter the mobile number and message that you want to send the message")
    #this is a module that is use in whatspp

    # Specify the phone numebr with the country code
    phone_number = input("enter the mobile number : ")

    #enter the message that you want to send the perticular numeber
    message = input("enter the message that you want to send :")

    # Send the message instantly
    status = kit.sendwhatmsg_instantly(phone_number, message)
    print("After filling the informanion web watsapp will be  open and send the message automatically")
elif int(ch) == 2:

    print("enter the message and monile number that you want to send the message")

    account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
    auth_token = '9fdbad4d67f2d7853b108f83b2ab788e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(

      from_='+19788007869',
      body = input("enter the message that you want to send  :  "),
      to = input("enter the number that you want to send the message : ")
      #to='+917219704283'
    )

    print(message.sid)


elif  int(ch) == 3:
    print("""enter the URL that you want to create the QR code
            enter the name of file that you want to save the QR""")
    URL = input("Enter your URL here : ")
    qr_imj = qrcode.make(URL)
    file_name = input("enter your qr code  code file name  : ")
    qr_imj.save(file_name)

elif int(ch) == 4 :

    print("call only for twilio account holders")
    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
    auth_token = '9fdbad4d67f2d7853b108f83b2ab788e'

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Make the call
    call = client.calls.create(
        to = input("enter your phone number that want to be call : "),       # The phone number you want to call
        from_='+19788007869',    # Your Twilio phone number
        url='http://demo.twilio.com/docs/voice.xml'  # URL of the TwiML file
    )

    print(f"Call SID: {call.sid}")

elif int(ch) == 5:


#    sender_email = 'dipakrasal2009@gmail.com'
#    sender_password = 'ufnmhoiswqesajsb'
#    recipient_email = input("enter the mail id that you want to send the mail : ")
    #
#    yag = yagmail.SMTP(sender_email, sender_password)
#    yag.send(
#        to=recipient_email,
#        subject=input("enter the subject of your mail  :  "),
#        contents=input("enter the content of your mail :  ")
#    )
#    print('Email sent successfully!')

    recipient_mail = input("enter the mail id of recipient  ::  ")
    subject_mail = input("enter the subject of the mail  ::  ")
    contents_mail = input("enter the contents of the mail  ::  ")
    #time = int(input("enter the time of your mail"))
    def send_email():
        sender_email = 'dipakrasal2009@gmail.com'
        app_password = 'ufnmhoiswqesajsb'  # Use the generated app password here
        #recipient_email = input("enter the mail id that you want to send the mail ::  ")
        recipient_email = recipient_mail

        yag = yagmail.SMTP(sender_email, app_password)
        yag.send(
            to=recipient_email,
            subject=subject_mail,
            contents=contents_mail
      )
        print('Email sent successfully!')

    # Schedule the email to be sent at a specific time (e.g., 14:30)
    schedule_time = '16:44'  #this is deaily send 
    #schedule.every(10).minutes.do(send_email)
    schedule.every().day.at(schedule_time).do(send_email)

    print(f'Scheduled email to be sent at {schedule_time} every day.')

    while True:
        schedule.run_pending()
        time.sleep(1)

else:
    print("Invalid choice")

