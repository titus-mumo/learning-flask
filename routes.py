from flask import Blueprint, render_template, flash, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from forms.form import LoginForm, SignUpForm, ChessPieceForm
from models import User, db, ChessPiece
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
    chess_pieces = ChessPiece.query.all()
    return render_template('home.html', chess_pieces = chess_pieces)


@main.route('/logout.html', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash("Logout successful!")
    return redirect(url_for('main.login'))

@main.route('/add.html', methods=['GET', 'POST'])
@login_required
def add_chess_piece():
    form = ChessPieceForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            points = form.points.data

            chess_piece = ChessPiece(name = name, points = points)
            try:
                db.session.add(chess_piece)
                db.session.commit()
                flash("Piece added successfully")
                return redirect( url_for('main.home'))
            except IntegrityError:
                flash("This piece already exists")
        else:
            flash("Invalid form")
    return render_template('add.html', form = form)