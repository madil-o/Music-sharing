
import random
import string
from flask import Blueprint, render_template, request, redirect

from .model import Url
from . import db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    song = request.form["song"]
    link = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    new_url = Url(id=link,song=song)
    db.session.add(new_url)
    db.session.commit()

    return redirect(f"/{link}")

  return render_template("home.html")

@views.route("/<string:link>")
def test(link):
  song_db = Url.query.filter_by(id=link).first()
  if song_db:
    return f"<h1>{link}</h1>"
  else:
    return "<h1>Inconnu</h1>"
