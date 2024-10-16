from flask import Flask, render_template, flash, request, redirect, url_for
from markupsafe import escape
from flask_pretty import Prettify
import secrets

from flask_bootstrap import Bootstrap5

from flask_wtf import CSRFProtect

from models import db, User

from config import Config

from routes import main



prettify = Prettify()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Create all tables in the database
    with app.app_context():
        db.create_all()

    # Generate a secret key
    foo = secrets.token_urlsafe(16)
    app.secret_key = foo

    # Initialize extensions
    bootstrap = Bootstrap5(app)  # Initialize Bootstrap
    csrf = CSRFProtect(app)      # Initialize CSRF protection
    prettify = Prettify()         # Initialize Prettify
    prettify.init_app(app)        # Bind Prettify to the app

    app.register_blueprint(main)

    return app 

# #escaping html
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"



# @app.route('/start.html')
# def start():
#     return render_template('start.html', name = 'Titus')



