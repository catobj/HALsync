from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "sk"

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["message"]
        # Your chat logic and calls to the OpenAI API go here
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)