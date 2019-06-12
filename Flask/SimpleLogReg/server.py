from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

EMAIL_RE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "asdf"
bcrypt = Bcrypt(app)

USER_KEY = "user_id"

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    # 1) is there an email in the db with the one user has provided?
    query = "SELECT password, id FROM users WHERE email = %(em)s"
    result = connectToMySQL("mydb").query_db(query, {"em": request.form["email"]})
    print(result)
    
    # 2) IF SO: check password in db for that user AGAINST the one they provided
    if result:
        print(bcrypt.check_password_hash(result[0]["password"], request.form["password"]))
        # if we have successfuly check out our user...PUT ID IN SESH!
        session[USER_KEY] = result[0]["id"]
        return redirect("/success")

    return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    # validations: all fields required, valid email
    # also UNIQUE email!  (we gotta check db for this)

    provided_email = request.form["email"]
    # is this email unique?
    query = "SELECT password FROM users WHERE email = %(em)s"
    data = { "em": provided_email }
    mysql = connectToMySQL("mydb")
    result = mysql.query_db(query, data)

    if not EMAIL_RE.match(provided_email):
        flash("Invalid email")

    if(len(result) > 0):
        # uh oh, someone has that
        flash("Email is already in use!")




    if "_flashes" in session:
        # we are invalid
        return redirect("/")
    else:
        # we can register our user!
        mysql2 = connectToMySQL("mydb")
        hashed_pw = bcrypt.generate_password_hash(request.form["password"])
        insert = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
            VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW())"

        data = {
            "fn": request.form["first_name"],
            "ln": request.form["last_name"],
            "em": request.form["email"],
            "pw": hashed_pw,
        }

        new_user = mysql2.query_db(insert, data)
        session[USER_KEY] = new_user
        print(new_user)
        return redirect("/success")



    
    # if our validations pass, we can create user 
    # and store new user's id in session
    return redirect("/")

@app.route("/success")
def success():
    # only regisered/loged in users should be here!
    if not USER_KEY in session:
        return redirect("/")
    mysql = connectToMySQL("mydb")
    user = mysql.query_db("SELECT * FROM users WHERE id = %(id)s", {"id": session[USER_KEY]})[0]
    return f"S U C C E S S, {user['first_name']}"


app.run(debug=True)
