
import random
import string
from flask import Blueprint, render_template, request, redirect

from .model import Url
from . import db
from . import get_platform_links


views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    song = request.form["song"]

    url = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    links = ";".join(get_platform_links.get_links(song))

    new_url = Url(id=url, song=song, links=links)
    db.session.add(new_url)
    db.session.commit()

    return redirect(f"/{url}")

  return render_template("home.html")

@views.route("/<string:link>")
def test(link):
  song_db = Url.query.filter_by(id=link).first()
  if song_db:
    return f"<h1>{song_db.links}</h1>"
  else:
    return "<h1>Inconnu</h1>"
