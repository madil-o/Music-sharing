
from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def home():
  return "<h1>Test</h1>"

@views.route("/<int:number>")
def test(number):
  return f"<h1>{number}</h1>"
