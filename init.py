from flask import Flask, render_template, flash
from markupsafe import escape
from flask_pretty import Prettify

prettify = Prettify()

app = Flask(__name__)

def create_app():
    prettify.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World<p>"


# #escaping html
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"


#rendering templates
@app.route('/start')
def start():
    return render_template('start.html', name = 'Titus')