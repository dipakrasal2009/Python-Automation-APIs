
from flask import Flask, jsonify
import pywhatkit as kit
import threading

app = Flask(__name__)

@app.route("/whatsapp/<mobileNumber>/<message>")
def whatsapp(mobileNumber, message):
    def send_whatsapp_message():
        try:
            # Send the message instantly
            kit.sendwhatmsg_instantly(f"+{mobileNumber}", message)
            print("Message sent successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # Run the send_whatsapp_message function in a separate thread to prevent blocking
    threading.Thread(target=send_whatsapp_message).start()
    
    return jsonify({"status": "Message is being sent"}), 200

if __name__ == "__main__":
    app.run(debug=True)





















# # pip install pywhatkit
# from flask import Flask
# import pywhatkit as kit
# #this is a module that is use in whatspp 

# app = Flask(__name__)

# @app.route("/whatsapp/<mobileNumber>/<message>")
# def whatsapp(mobileNumber,message):
#     # Specify the phone numebr with the country code 
#     phone_number = mobileNumber

#     #enter the message that you want to send the perticular numeber
#     send_message = message

#     # Send the message instantly
#     status = kit.sendwhatmsg_instantly(phone_number, send_message) 

# app.run()
