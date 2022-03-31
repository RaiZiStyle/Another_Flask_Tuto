from flask import Flask
from config import Config

# For database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#  My App
# from app import routes, models



# def main():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     db = SQLAlchemy(app)
#     print(f"db : {db}")
#     migrate = Migrate(app, db)


# if __name__ == "__main__":
#     app = Flask(__name__)


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from app.models import User
