import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
)
from mysqlconnection import connectToMySQL

def validate(form, unique_email):
    # validations: all fields required, email must be valid, email must be unique
    
    errors = []
    if len(form["first_name"]) < 1:
        errors.append("First Name is required")
    if len(form["last_name"]) < 1:
        errors.append("Last Name is required")
    if len(form["email"]) < 1:
        errors.append("Email field is required")
    if len(form["password"]) < 8:
        errors.append("Password must be at least 8 characters")

    if not EMAIL_REGEX.match(form["email"]):
        errors.append("Invalid Email")
    elif unique_email:
        mysql = connectToMySQL("mydb")
        # see if we have a unique email
        result = mysql.query_db("SELECT id FROM users WHERE email = %(email)s", {"email": form["email"]})
        print(result)
        if result:
            errors.append("Email already in use")

    return errors



