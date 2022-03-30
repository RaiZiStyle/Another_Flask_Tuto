from flask import Flask
from config import Config

# For database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#  My App
# from app import routes, models

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
