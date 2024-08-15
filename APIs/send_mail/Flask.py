from flask import Flask, jsonify
import yagmail

app = Flask(__name__)

@app.route("/mail/<receiver>/<subject>/<message>")
def sendEmail(receiver, subject, message):
    try:
        sender_email = 'dipakrasal2009@gmail.com'
        sender_password = 'ufnmhoiswqesajsb'
        recipient_email = receiver

        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=recipient_email,
            subject=subject,
            contents=message
        )
        return jsonify({"message": "Email sent successfully!",
                        "sender mail" : sender_email,
                        "reciver mail" : recipient_email,
                        "subject" : subject,
                        "content" : message},), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
