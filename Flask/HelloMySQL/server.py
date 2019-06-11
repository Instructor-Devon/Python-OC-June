from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re

# re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "sadf3jwckjlksdjfl"

@app.route("/")
def index():

    for key in session:
        print(session[key])

    mysql = connectToMySQL("mydb")
    homies = mysql.query_db("SELECT * FROM homies")
    print(homies)
    return render_template("index.html", all_homies=homies)

@app.route("/create", methods=["POST"])
def create():
    print(request.form)

    data = {
        "name": request.form["name"],
        "em": request.form["email"],
        "loc": request.form["location"]
    }
    # we are invalid if there is a _flashes key in session
    # check data for all fields containging data
    
    if len(request.form["name"]) < 1:
        flash("Name field is required")
    if len(request.form["email"]) < 1:
        flash("Email field is required")
    if len(request.form["location"]) < 1:   
        flash("Location field is required")
    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email address")
    

    if not "_flashes" in session.keys():
        insert = "INSERT INTO homies (name, email, location) VALUES (%(name)s, %(em)s, %(loc)s);"
        
        mysql = connectToMySQL("mydb")
        mysql.query_db(insert, data)
    return redirect("/")

@app.route("/show/<user_id>")
def show(user_id):
    query = "SELECT * FROM homies WHERE id = %(id)s"
    data = {
        "id": user_id
    }
    mysql = connectToMySQL("mydb")
    result = mysql.query_db(query, data)
    user = result[0]
    print(user)
    return render_template("show.html", user=user)


app.run(debug=True)