from flask import jsonify, render_template, flash, redirect, url_for, session, logging, request
from app import app
from . import models
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

#user = models.User.createUser()
user = models.User()
repo = {}

userlist = [{'userdetails':['d@gmail.com','David', 'password123']}]


#API END-POINTS
@app.route('/api/users', methods=['GET'])
def allUsers():

    return jsonify({'users':userlist})

@app.route('/api/users', methods=['POST'])
def registeruser():

    user = {'userdetails':[request.json['userdetails']]}

    userlist.append(user)

    return jsonify({'users':userlist})

@app.route('/api/users', methods=['POST'])
def logoutuser():

    pass

@app.route('/api/users', methods=['POST'])
def resetpassword():

    pass


class RegisterForm(Form):

 	name = StringField('Name', [validators.Length(min=1,max=50)])
 	email = StringField('Émail', [validators.Length(min=6, max=50)])
 	password = PasswordField('Password', [
 			validators.DataRequired(),
            validators.EqualTo('confirmpassword', message='Password do not match')])
 	confirmpassword = PasswordField('Confirm Password')

@app.route('/', methods = ['GET', 'POST'])

def index():

    form =RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        #confirmpassword = form.confirmpassword.data

        data = user.createUser(name, email, password)

        repo.update(data)

        #"You have signed up and can now login"

        flash(repo[email][1], 'success')

        return redirect(url_for('login'))

    return render_template('index.html', form = form)

@app.route('/about')

def about():

    return render_template('about.html')

@app.route('/login', methods = ['GET','POST'])

def login():

    if request.method == 'POST' and form.validate():

        email = request.form['email']

        password = request.form['password']

        if email in repo.keys():

            if repo[email][1] == password:

                session['logged_in'] = True

                session['email'] = email

                flash('You are now logged in', 'success')

                return redirect(url_for('home'))

            else:

                error = 'Invalid Login'

                return render_template('login.html', error=error)
        else:
            error = 'User does not exist'

            return render_template('login.html', error=error)


    return render_template('login.html')

@app.route('/home')

def home():

    return render_template('home.html')

@app.route('/addEvent')

def addEvent():

    return render_template('addEvent.html')

@app.route('/myEvents')

def myEvents():

    return render_template('myEvents.html')

app.secret_key = 'MumbleJumble123'
