from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import connectToMySQL
from validations import validate, authenticate
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secretttsssss"
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    los_errors = validate(request.form)

    if los_errors:
        for err in los_errors:
            flash(err)
        
        return redirect("/")

    # we made here!
    # we can make a user now
    # hash password
    hashed = bcrypt.generate_password_hash(request.form["password"])

    ins = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s)"
    data = {
        "fn": request.form["first_name"],
        "ln": request.form["last_name"],
        "em": request.form["email"],
        "pw": hashed,
    }
    mysql = connectToMySQL("private_wall")
    new_user_id = mysql.query_db(ins, data)
    session['user_id'] = new_user_id

    return redirect("/wall")

@app.route("/login", methods=["POST"])
def login():
    # autheticate will give me either False OR user_id
    result = authenticate(request.form, bcrypt)
    if result == False:
        flash("Invalid Email/Password")
        return redirect("/")

    session['user_id'] = result
    return redirect("/wall")

@app.route("/wall")
def wall():
    if not "user_id" in session:
        return redirect("/")

    users = connectToMySQL("private_wall").query_db("SELECT * FROM users WHERE id = %(id)s", {"id": session["user_id"]})
    user = users[0]

    mess_query = "SELECT m.id, m.content, m.created_at, s.first_name AS sender_name, s.id AS sender_id, r.id AS recip_id FROM messages AS m JOIN users AS s ON m.sender_id = s.id JOIN users AS r ON m.recip_id = r.id WHERE r.id = %(rec)s"
    mess_data = {
        "rec": session["user_id"]
    }
    
    users_messages = connectToMySQL("private_wall").query_db(mess_query, mess_data)

    print(users_messages)

    one_message = users_messages[0]
    time_delta = datetime.now() - one_message["created_at"]
    print(time_delta.seconds)

    others = connectToMySQL("private_wall").query_db("SELECT * FROM users WHERE id != %(id)s", {"id": session["user_id"]})

    return render_template("wall.html", user=user, messages=users_messages, others=others)

@app.route("/create", methods=["POST"])
def create():
    ins = "INSERT INTO messages (content, sender_id, recip_id) VALUES (%(con)s, %(s)s, %(r)s);"
    data = {
        "con": request.form["message"],
        "s": session["user_id"],
        "r": request.form["recip"]
    }

    connectToMySQL("private_wall").query_db(ins, data)
    return redirect("/wall")

@app.route("/delete/<message_id>")
def delete(message_id):
    
    if not "user_id" in session:
        return redirect("/")

    # verify we can delete message
    rec_query = "SELECT recip_id FROM messages WHERE id = %(m)s"
    message_result = connectToMySQL("private_wall").query_db(rec_query, {"m": message_id})
    message = message_result[0]

    if message["recip_id"] != session["user_id"]:
        # sorry hacker
        return "SORRY HACKER BRO"

    del_query = "DELETE FROM messages WHERE id = %(id)s"
    data = {
        "id": message_id
    }
    connectToMySQL("private_wall").query_db(del_query, data)

    return redirect("/wall")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)