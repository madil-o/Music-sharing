
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
  from pathlib import Path
  from .views import views
  from .model import Url

  app = Flask(__name__)

  script_location = Path(__file__).absolute().parent
  f = open(f"{script_location}/key", "r")
  app.config["SECRET_KEY"] = f.read()
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///urls_db.db"
  db.init_app(app)

  app.register_blueprint(views, url_prefix="/")

  with app.app_context():
    db.create_all()

  return app
