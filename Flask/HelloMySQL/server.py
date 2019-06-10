from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("mydb")
    homies = mysql.query_db("SELECT * FROM homies")
    print(homies)
    return render_template("index.html", all_homies=homies)

@app.route("/create", methods=["POST"])
def create():
    print(request.form)

    data = {
        "name": request.form["name"],
        "loc": request.form["location"]
    }

    insert = "INSERT INTO homies (name, location) VALUES (%(name)s, %(loc)s);"
    
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