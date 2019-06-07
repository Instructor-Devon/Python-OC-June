from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "SUPER SECRET KEY HERE!!! shhhhh"

@app.route("/")
def index():
    # first time user experience
    # check if "clicks" is in session

    if not "clicks" in session:
        session["clicks"] = 0
    # session["clicks"] = 0
    # print(session["name"])

    has_entered = True
    if not "name" in session:
        has_entered = False

    # build a session["history"] -> ["devo", "howard"...]
    if not "history" in session:
        session["history"] = []

    print(has_entered)
    print(session["clicks"])
    print(session)
    return render_template("index.html", has_entered=has_entered)

@app.route("/click")
def click():
    # increment session["clicks"]
    session["clicks"] += 1
    return redirect("/")

@app.route("/signout")
def signout():
    # session.clear()
    # remove a single key!
    if "name" in session:
        del session["name"]
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

# POST!!
@app.route("/add/name", methods=["POST"])
def add_name():
    session["name"] = request.form["name"]
    session["history"].append(request.form["name"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)