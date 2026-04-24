from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

# 🔥 EMAIL DESTINATAIRE
TO_EMAIL = "azizwang29@gmail.com"

# ⚠️ UTILISE UN MOT DE PASSE D'APPLICATION GMAIL
FROM_EMAIL = "azizwang47@gmail.com"
PASSWORD = "TON_APP_PASSWORD_GMAIL"


def send_email(name, email, message):

    subject = "Nouveau message depuis le site Artisan"

    body = f"""
Nouveau message reçu :

Nom : {name}
Email : {email}

Message :
{message}
"""

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        print("Erreur SMTP:", e)
        raise e


@app.route("/")
def home():
    return "Backend OK 🚀"


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"message": "Champs obligatoires"}), 400

    try:
        send_email(name, email, message)
        return jsonify({"message": "Message envoyé avec succès !"})

    except Exception as e:
        return jsonify({"message": "Erreur envoi email"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
