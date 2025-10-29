from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():
    return "Hello user! This is my first flask app."


if __name__ == "__main__":
    # Run directly with: python app.py
    # Uses 127.0.0.1:5000 by default; set debug=True for auto-reload during development
    app.run(debug=True)
