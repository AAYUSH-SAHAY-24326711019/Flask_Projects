import datetime

from flask import Blueprint, render_template,url_for,request,redirect

auth = Blueprint('auth', __name__)

# ----------------Code for signup start----------------
@auth.route('/signup')
def signup():
    # return "This will sign up the users"
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form['email']
    name = request.form['username']
    password = request.form['password']

    print(email,name,password)

    return redirect(url_for('auth.login'))

# ----------------Code for signup end----------------


@auth.route('/login')
def login():
    # return "This will login the users"
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "This will logout the users"