from flask import Blueprint, render_template, flash, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from forms.form import LoginForm, SignUpForm
from models import User, db
from flask_login import login_required, login_user, logout_user

# Create a blueprint
main = Blueprint('main', __name__)


#rendering templates
@main.route("/")
def hello_world():
    return render_template('start.html')


# #escaping html
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"



# @app.route('/start.html')
# def start():
#     return render_template('start.html', name = 'Titus')

@main.route('/signup.html', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            new_user = User(username = username, email = email)
            new_user.set_password(password)

            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully")
                return redirect( url_for('main.login'))
            except IntegrityError:
                db.session.rollback()
                flash("Username or email already exists")
        else:
            flash("Invalid form")
    return render_template('signup.html', form = form)


@main.route('/login.html', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username  = form.username.data
            password = form.password.data
            user = User.query.filter(User.username == username).first()
            if user:
                if user.check_password(password):
                    login_user(user, remember=True)
                    flash("Login successful")
                    return redirect( url_for('main.home'))
                else:
                    flash("Invalid credentials")
            else:
                flash("Invalid username")

        else:
            flash('Invalid form')
    return render_template('login.html', form = form)


@main.route('/home.html', methods=['GET'])
@login_required
def home():
    return render_template('home.html')


@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("Logout successful!")
    return redirect(url_for('main.login'))

