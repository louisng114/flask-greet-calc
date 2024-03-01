from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """Display welcome message"""
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    """Display welcome home message"""
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    """Display welcome back message"""
    return "welcome back"
