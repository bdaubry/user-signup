from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def valid_check(word, t):
    if t == "name":
        for l in word:
            if l == " ":
                return False
            else:
                return True
    if len(word) >= 3 and len(word) <= 20:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def handle_form():
    name = request.form['name']
    password = request.form['password']
    passconf = request.form['passconf']
    email = request.form['email']
    name_error = password_error = passconf_error = email_error = ''

    if name == '' or valid_check(name, name) == False:
        name_error = "That's not a valid username"

    if password == '' or valid_check(password, password) == False:
        password_error = "That's not a valid password"

    if passconf == '' or valid_check(passconf, password) == False or password != passconf:
        passconf_error = "Passwords don't match"

    at_count = 0
    period_count = 0

    for l in email:
        if l == '@':
            at_count = at_count + 1
        elif l == '.':
            period_count = period_count + 1
        if l == ' ':
            email_error = "That is not a valid email!"
            break

    if email != '' and (at_count != 1 or period_count != 1):
        email_error = "That is not a valid email!"
    

    if name_error == '' and password_error == '' and passconf_error == '' and email_error == '':
        return render_template('signup.html', name=name)
    else:
        return render_template('form.html', name=name, email=email, name_error=name_error, password_error=password_error, passconf_error=passconf_error, email_error=email_error)

app.run()