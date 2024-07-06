import yagmail
import schedule
import time




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

