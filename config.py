import os

class Config(object):
    FlASK_ENV = f"development"
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_FOLDER = "templates"