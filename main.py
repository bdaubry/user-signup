from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def handle_form():
    name = request.form['name']
    password = request.form['password']
    passconf = request.form['passconf']
    email = request.form['email']

    if name == '' or password == '' or passconf == '':
        name_error = "That's not a valid username"
        password_error = "That's not a valid password"
        passconf_error = "Passwords don't match"
        return render_template('form.html', name_error=name_error, password_error=password_error, passconf_error=passconf_error)

    return render_template('signup.html', name=name)

app.run()