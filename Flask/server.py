from flask import Flask, render_template, request

app = Flask(__name__)

# localhost:5000/
# listening for a request
@app.route("/")
# return a server respose
def index():
    parties = [
        "Birthday",
        "Anniversday",
        "Saturday"
    ]
    return render_template("index.html", party_choices=parties)

# localhost:5000/party/<party_type>
@app.route("/party/<party_type>")
def party(party_type):
    print(party_type)
    color = "black"
    if party_type == "Saturday":
        color = "pink"
    return render_template("party.html", party=party_type, color=color)

@app.route("/doit", methods=["POST"])
def do_it():
    # dictionary for the post request: request.form
    print(request)
    print(request.form["alias"])
    return f"Welcome to the party {request.form['alias']}"

app.run(debug=True)