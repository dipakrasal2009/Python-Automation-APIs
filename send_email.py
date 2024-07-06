import yagmail

sender_email = 'dipakrasal2009@gmail.com'
sender_password = 'ufnmhoiswqesajsb'
recipient_email = input("enter the mail id that you want to send the mail  ::  ")

yag = yagmail.SMTP(sender_email, sender_password)
yag.send(
    to=recipient_email,
    subject=input("enter the subjcet of the mail  :: "),
    contents=input("enter the body content of the mail  ::  ")
)
print('Email sent successfully!')

