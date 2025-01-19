
from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    song = request.form["song"]

  return render_template("home.html")

@views.route("/<int:number>")
def test(number):
  return f"<h1>{number}</h1>"
