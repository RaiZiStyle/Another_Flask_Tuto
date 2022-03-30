import os


class Config(object):
    FLASK_ENV = "development"
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_FOLDER = "templates"
    print(f"secret key is : {SECRET_KEY}")
