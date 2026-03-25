from flask import Blueprint, render_template,url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    # return "This will signup the users"
    return render_template('signup.html')


@auth.route('/login')
def login():
    # return "This will login the users"
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "This will logout the users"