import re
from mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def validate(form):
    print(form, "from validate.py")
    errors = []

    # first name/last name must be at least 2 characters
    if len(form["first_name"]) < 2:
        errors.append("first name must be at least 2 characters")
    if len(form["last_name"]) < 2:
        errors.append("last name must be at least 2 characters")
    # valid email
    if not EMAIL_REGEX.match(form["email"]):
        errors.append("Invalid Email Address")
    # password over 8 characters
    if len(form["password"]) < 8:
        errors.append("password must be at least 8 characters")
    # password/confirm must match
    if form["password"] != form["confirm"]:
        errors.append("passwords do not match")
    # email must be unique to the database

    mysql = connectToMySQL("private_wall")
    result = mysql.query_db("SELECT id FROM users WHERE email = %(em)s", {"em": form['email']})
    # result is like this [{"id": 3}] OR []
    if len(result) > 0:
        errors.append("Email is already taken!")

    return errors

def authenticate(form, bcrypt):
    # return True/False
    mysql = connectToMySQL("private_wall")
    result = mysql.query_db("SELECT id, password FROM users WHERE email = %(em)s", {"em": form['email']})
    # result is like this [{"id": 3,  "password": "asdfdsaf3sdfws2"}] OR []

    if not result:
        return False
    
    # we know we have something here, lets' just grab the first
    result = result[0]
    
    # we gotta checkout this dude
    is_verifyed = bcrypt.check_password_hash(result["password"], form["password"])

    if not is_verifyed:
        return False
        
    # if user is cool, return the user's id    
    return result["id"]


    

