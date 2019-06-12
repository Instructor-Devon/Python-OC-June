from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "asdf"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    pass

@app.route("/register", methods=["POST"])
def register():
    # validations: all fields required, valid email
    # also UNIQUE email!  (we gotta check db for this)

    
    # if our validations pass, we can create user 
    # and store new user's id in session
    pass

@app.route("/success")
def success():
    return "S U C C E S S"

app.run(debug=True)
