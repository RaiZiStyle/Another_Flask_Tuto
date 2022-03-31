from flask import Flask
from flask_login import LoginManager

# For database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Local import
from config import Config
#  My App




# def main():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     db = SQLAlchemy(app)
#     print(f"db : {db}")
#     migrate = Migrate(app, db)


# if __name__ == "__main__":
#     app = Flask(__name__)


app = Flask(__name__)
# print(f"__name__ : {__name__}")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# from app.models import User
from app import routes, models
