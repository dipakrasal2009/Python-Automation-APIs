from flask import Flask, jsonify
import yagmail

app = Flask(__name__)

@app.route("/contact/<name>/<email>/<message>")
def sendEmail(name, email, message):
    try:
        sender_email = 'add sender email id'
        sender_password = 'add sender password'
        recipient_email = email

        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=recipient_email,
            subject=name,
            contents=message
        )
        return jsonify({"message": "Email sent successfully!",
                        "sender mail" : sender_email,
                        "reciver mail" : recipient_email,
                        "content" : message},), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
