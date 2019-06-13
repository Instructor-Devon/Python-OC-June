from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from validations import validate

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

    
    # 2) IF SO: check password in db for that user AGAINST the one they provided
    if result:
        if(bcrypt.check_password_hash(result[0]["password"], request.form["password"])):
        
        # if we have successfuly check out our user...PUT ID IN SESH!
            session[USER_KEY] = result[0]["id"]
            return redirect("/success")

    flash("Invalid Email/Password")
    return redirect("/")

@app.route("/register", methods=["POST"])
def register():

    errors = validate(request.form, True)
    if errors:
        for error in errors:
            flash(error)
        return redirect("/")    
    else:
        # we can register our user!
        mysql = connectToMySQL("mydb")
        hashed_pw = bcrypt.generate_password_hash(request.form["password"])
        insert = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
            VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW())"

        data = {
            "fn": request.form["first_name"],
            "ln": request.form["last_name"],
            "em": request.form["email"],
            "pw": hashed_pw,
        }

        new_user = mysql.query_db(insert, data)
        session[USER_KEY] = new_user
        
        return redirect("/dashboard")

    
    # if our validations pass, we can create user 
    # and store new user's id in session
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    # only regisered/loged in users should be here!
    if not USER_KEY in session:
        return redirect("/")
    mysql = connectToMySQL("mydb")
    user = mysql.query_db("SELECT * FROM users WHERE id = %(id)s", {"id": session[USER_KEY]})[0]
    return render_template("dashboard.html", user=user)

@app.route("/create", methods=["POST"])
def create():
    # validating....
    print(request.form)
    if not USER_KEY in session:
        return redirect("/")

    insert = "INSERT INTO posts (topic, content, user_id) VALUES (%(topic)s, %(content)s, %(id)s);"
    data = {
        "topic": request.form["topic"],
        "content": request.form["content"],
        "id": session[USER_KEY]
    }

    connectToMySQL("mydb").query_db(insert, data)

    return redirect('/fetch')

@app.route("/fetch")
def fetch_posts():
    
    
    qs = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC"
    posts = connectToMySQL("mydb").query_db(qs)
    return render_template("posts_partial.html", posts=posts)

app.run(debug=True)
