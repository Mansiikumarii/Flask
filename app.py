from flask import Flask, request
app = Flask(__name__)

@app.route("/")

def home():
    return "Hello user! This is my first flask app."

@app.route("/about")
def about():
    return 'This is about us page'

@app.route("/contact")
def contact():
    return 'This is contact us page'

@app.route("/submit",methods = ["GET","POST"])
def submit():
    if request.method == "POST":
        return "You send data!"
    else:
        return "You are only viewing the form."

if __name__ == "__main__":
    # Run directly with: python app.py
    # Uses 127.0.0.1:5000 by default; set debug=True for auto-reload during development
    app.run(debug=True)


