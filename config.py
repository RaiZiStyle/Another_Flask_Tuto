import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = "development"
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_FOLDER = "templates"

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
