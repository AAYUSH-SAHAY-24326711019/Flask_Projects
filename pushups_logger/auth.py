from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "This will signup the users"

@auth.route('/login')
def login():
    return "This will login the users"

@auth.route('/logout')
def logout():
    return "This will logout the users"