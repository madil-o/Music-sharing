
from flask import Flask
from pathlib import Path
from .views import views


def create_app():
  app = Flask(__name__)

  script_location = Path(__file__).absolute().parent
  f = open(f"{script_location}/key", "r")
  app.config["SECRET_KEY"] = f.read()

  app.register_blueprint(views, url_prefix="/")

  return app
