from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# ---------- HOME / LOGIN PAGE ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response(
                '''
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {
                            background: linear-gradient(135deg, #ff9966, #ff5e62);
                            font-family: "Poppins", sans-serif;
                            color: white;
                            text-align: center;
                            margin-top: 120px;
                        }
                        .error {
                            color: #fff;
                            background-color: rgba(255,0,0,0.3);
                            padding: 10px;
                            border-radius: 6px;
                            display: inline-block;
                            margin-bottom: 15px;
                        }
                        a {
                            color: #fff;
                            text-decoration: underline;
                        }
                    </style>
                </head>
                <body>
                    <div class="error">
                        <h3>❌ Invalid credentials. Try again.</h3>
                    </div>
                    <a href="/">Go Back</a>
                </body>
                </html>
                ''', mimetype="text/html"
            )

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Login | Think41 Portal</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            .container {
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                width: 350px;
                padding: 30px;
                text-align: center;
            }
            h2 {
                color: #444;
                margin-bottom: 25px;
            }
            input[type="text"], input[type="password"] {
                width: 85%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
            }
            input[type="submit"] {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 15px;
                transition: 0.3s ease;
            }
            input[type="submit"]:hover {
                transform: scale(1.05);
                background: linear-gradient(135deg, #6b8de3, #8f6ed5);
            }
            .note {
                font-size: 13px;
                color: #777;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🔐 Login to Think41</h2>
            <form method="POST">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Login">
            </form>
            <div class="note">
                <p>Hint: admin / 123</p>
            </div>
        </div>
    </body>
    </html>
    '''


# ---------- WELCOME PAGE ----------
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Welcome</title>
            <style>
                body {{
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #00c6ff, #0072ff);
                    color: white;
                    text-align: center;
                    margin-top: 100px;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    background-color: rgba(255,255,255,0.2);
                    color: #fff;
                    text-decoration: none;
                    padding: 10px 20px;
                    border-radius: 6px;
                    transition: 0.3s;
                }}
                a:hover {{
                    background-color: rgba(255,255,255,0.4);
                }}
            </style>
        </head>
        <body>
            <h2>👋 Welcome, {session["user"]}!</h2>
            <p>You have successfully logged in to the Think41 Portal.</p>
            <a href="{url_for('logout')}">Logout</a>
        </body>
        </html>
        '''
    return redirect(url_for("login"))


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
