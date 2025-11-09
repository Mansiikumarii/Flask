from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='template')

# Home page route
@app.route("/")
def home():
    # This will render the home.html template with a link to the welcome page
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to Home Page</h1>
        <p>Click the button below to go to the Welcome page:</p>
        <a href="/welcome"><button>Go to Welcome Page</button></a>
    </body>
    </html>
    """

# Welcome page route
@app.route("/welcome")
def welcome():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Welcome Page</title>
    </head>
    <body>
        <h1>Welcome Page</h1>
        <p>You have been redirected to the welcome page!</p>
        <a href="/"><button>Go Back Home</button></a>
        <br><br>
        <a href="/redirect-example"><button>Try Automatic Redirect</button></a>
    </body>
    </html>
    """

# Example of automatic redirection
@app.route("/redirect-example")
def redirect_example():
    # This will automatically redirect to the home page
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)