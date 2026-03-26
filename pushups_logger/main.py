from flask import Blueprint, render_template,url_for,redirect,request,flash,abort
from flask_login import login_required, current_user
from . import db
from .models import User
from .models import Workout


main = Blueprint('main', __name__)

@main.route('/')
def index():
    # return 'Hello World'
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # return 'Hello World'
    return render_template('profile.html',name=current_user.name)

# -------------Section to add the workouts -------------------start
@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')

@main.route('/new',methods=['POST'])
@login_required
def new_workout_post():
    pushups= request.form.get('pushups')
    comment = request.form.get('comment')

    workout = Workout(pushups=pushups,comment=comment,author=current_user)
    db.session.add(workout)
    db.session.commit()

    flash('Your workout has been added!')

    return redirect(url_for('main.user_workouts'))

# -------------Section to add the workouts -------------------end

# -------------Section to see the workouts -------------------start
@main.route('/all')
@login_required
def user_workouts():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    workouts = user.workouts
    return render_template('all_workouts.html',workouts=workouts,user=user)
# -------------Section to see the workouts -------------------end