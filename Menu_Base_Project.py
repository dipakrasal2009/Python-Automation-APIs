import os
import pywhatkit as kit
from twilio.rest import Client
import qrcode
import yagmail
import schedule
import time
from googlesearch import search
import pyttsx3
import speech_recognition as sr
import webbrowser



print("\t\t\t\t My Menu Project ")
print("\t\t\t\t------------------")

print("""for sending the whatsapp nessage.
        for sending the SMS message.
        for generate the qr code.
        making the call.
         to send the email
        search on the google and get top 5 results
        it speak the text that you enterd
        """)


# Initialize recognizer
recognizer = sr.Recognizer()

# Capture voice input from the microphone
with sr.Microphone() as source:
    print("how can I help you :=>  ")
    # Adjust the recognizer sensitivity to ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1)
    # Capture the audio from the microphone
    audio = recognizer.listen(source)

# Recognize speech using Google Web Speech API
try:
    string = recognizer.recognize_google(audio)
    print("You Speak =>  " + string)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio.")
    string = ""
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
    string = ""

if 'whatsapp' in string.lower():
    print("Please, Enter the mobile number and message that you want to send.")
    phone_number = input("Enter the mobile number: ")
    message = input("Enter the message that you want to send: ")
    kit.sendwhatmsg_instantly(phone_number, message)
    print("After filling the information, web WhatsApp will open and send the message automatically.")

elif 'sms' in string.lower() or 'text' in string.lower():
    print("Enter the message and mobile number that you want to send the message to.")
    account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
    auth_token = '9fdbad4d67f2d7853b108f83b2ab788e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+19788007869',
      body=input("Enter the message that you want to send: "),
      to=input("Enter the number that you want to send the message to: ")
    )
    print(message.sid)   

elif 'qr' in string.lower():
    print("Enter the URL that you want to create the QR code for and the name of the file to save the QR code.")
    URL = input("Enter your URL here: ")
    qr_img = qrcode.make(URL)
    file_name = input("Enter your QR code file name: ")
    qr_img.save(file_name)

elif 'call' in string.lower():
    print("Call only for Twilio account holders.")
    account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
    auth_token = '9fdbad4d67f2d7853b108f83b2ab788e'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=input("Enter your phone number that you want to call: "),
        from_='+19788007869',
        url='http://demo.twilio.com/docs/voice.xml'
    )
    print(f"Call SID: {call.sid}")

elif 'email' in string.lower() or 'mail' in string.lower():
    recipient_mail = input("Enter the recipient's email ID: ")
    subject_mail = input("Enter the subject of the email: ")
    contents_mail = input("Enter the contents of the email: ")

    def send_email():
        sender_email = 'dipakrasal2009@gmail.com'
        app_password = 'ufnmhoiswqesajsb'
        recipient_email = recipient_mail

        yag = yagmail.SMTP(sender_email, app_password)
        yag.send(
            to=recipient_email,
            subject=subject_mail,
            contents=contents_mail
        )
        print('Email sent successfully!')

    schedule_time = input("enter the time that you want to send the mail  :: ")
    schedule.every().day.at(schedule_time).do(send_email)
    print(f'Scheduled email to be sent at {schedule_time} every day.')
    
    while True:
        schedule.run_pending()
        time.sleep(1)

elif 'results' in string.lower():
    query = input("Enter the text you want to search: ")
    results = search(query, num_results=5)
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result}")

elif 'speak' in string.lower():
    engine = pyttsx3.init()
    text = input("Enter the text that you want to be spoken: ")
    rate = engine.getProperty('rate')
    print(f"Current speaking rate: {rate}")
    new_rate = 150
    engine.setProperty('rate', new_rate)
    print(f"New speaking rate: {new_rate}")
    engine.say(text)
    engine.runAndWait()
else:
    print("Invalid choice")

