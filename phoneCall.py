from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
auth_token = '4516ccbf9283f938917e84451f2ad4b1'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
        to = input("enter your phone number that want to be call : "),       # The phone number you want to call
    from_='+19788007869',    # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # URL of the TwiML file
)

print(f"Call SID: {call.sid}")

