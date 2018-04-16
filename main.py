from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True



#Helper functions to check input. If it returns true there's an error in input.
#
def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return True
    else:
        return False
def validate_password(password):
    if len(password) < 3 or len(password) > 20:
        return True
    else:
        return False
def validate_email(email):
    if email != '':
        if "@" in email and "." in email and len(email) < 3 and len(email) > 20:
            return False
        else: 
            return True
def password_match(password, verify_password):
    if password == verify_password:
        return False
    else:
        return True
def is_it_empty(input_value):
    if (not input_value) or (input_value.strip() == ""):
        return True
    else:
        return False
#
#End helper functions to check input



@app.route("/")
def index():
    return render_template('form.html')



@app.route("/validate", methods=['POST'])
def validate():
    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']

    username_error=''
    username_error_v=''
    password_error=''
    password_error_v=''
    verify_password_error=''
    email_error_v=''

    #Initialize error check
    was_there_an_error = False

    if is_it_empty(username):
        username_error = "Please specify a username."
        was_there_an_error = True
        
    if validate_username(username):
        username_error_v = "Format username correctly"
        was_there_an_error = True
        

    if is_it_empty(password):
        password_error = "Please enter a password."
        password=''
        was_there_an_error = True
        
    if validate_password(password):
        password_error_v = "Format password properly."
        verify_password=''
        was_there_an_error = True
        

    if is_it_empty(verify_password):
        verify_password_error = "Please enter the password again."
        was_there_an_error = True
        
        
    if validate_email(email):
        email_error_v = "Enter a valid email."
        email=''
        was_there_an_error = True
        

    if was_there_an_error == True:
        return render_template('form.html', username_error=username_error, username_error_v=username_error_v, password_error=password_error, password_error_v=password_error_v, verify_password_error=verify_password_error, email_error_v=email_error_v, password=password, verify_password=verify_password, username=username, email=email)
        
    else:
        return render_template('welcome.html', username=username)


app.run()