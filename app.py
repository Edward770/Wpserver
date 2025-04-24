from flask import Flask, render_template, request
from send_whatsapp import send_messages
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number = request.form["number"]
        delay = int(request.form["delay"])
        file = request.files["message_file"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        send_messages(number, filepath, delay)
        return "Messages sent successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
