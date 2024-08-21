from twilio.rest import Client
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/sendsms/<mobilenumber>/<message>")
def send_message(mobilenumber, message):
    try:
        # Store sensitive information in environment variables
        account_sid = 'Add your account sid'
        auth_token = 'add your auth token'
        client = Client(account_sid, auth_token)

        # Send SMS
        sms = client.messages.create(
            from_='add your twilio mobile number',
            body=message,
            to=mobilenumber
        )

        # Return success response
        return jsonify({"status": "success", "message_sid": sms.sid}), 200

    except Exception as e:
        # Return error response
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)















# from twilio.rest import Client
# from flask import Flask

# app = Flask(__name__)

# @app.route("/sendsms/<mobilenumber>/<message>")
# def send_message(mobilenumber,message):
#     account_sid = 'AC6f058ce3b7004c09a831bbec134d9325'
#     auth_token = '4a7bbc69b0e91df8b8ecd489da72db96'
#     client = Client(account_sid, auth_token)
    
#     message = client.messages.create(
  
#     from_='+19788007869',
#     body = message,
#     to = mobilenumber
#     #to='+917219704283'
#     )

#     print(message.sid)

# app.run()
