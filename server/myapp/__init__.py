import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
# from flask_restful_swagger import swagger

app = Flask(__name__, static_folder='../../client/dist', static_url_path='', template_folder='../../client/dist')
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from myapp import routes