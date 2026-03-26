import datetime

from flask import Blueprint, render_template,url_for,request,redirect

from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .import db

auth = Blueprint('auth', __name__)

# ----------------Code for signup start----------------
@auth.route('/signup')
def signup():
    # return "This will sign up the users"
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')

    # print(email,name,password)
    # ------------------code for the database -------------------start
    user = User.query.filter_by(email=email).first()
    if user:
        print("user already exists")

    # new_user = User(email=email,name=name,password=generate_password_hash(password ,method='pbkdf2:sha256'))
    # db.session.add(new_user)
    # db.session.commit()
    else:
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
    # ------------------code for the database -------------------end
    return redirect(url_for('auth.login'))

# ----------------Code for signup end----------------


# ----------------Code for Login start----------------
@auth.route('/login')
def login():
    # return "This will login the users"
    return render_template('login.html')
@auth.route('/login',methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email,password)
    return redirect(url_for('main.profile'))

# ----------------Code for Login end----------------
@auth.route('/logout')
def logout():
    return "This will logout the users"