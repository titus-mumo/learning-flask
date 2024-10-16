from flask_frozen import Freezer

from init import create_app

app  = create_app()

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()