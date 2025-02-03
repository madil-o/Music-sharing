
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
    cover = get_platform_links.get_cover(song)

    new_url = Url(id=url, song=song, links=links, cover=cover)
    db.session.add(new_url)
    db.session.commit()

    return redirect(f"/{url}")

  return render_template("home.html")

@views.route("/<string:link>")
def song_page(link):
  song_db = Url.query.filter_by(id=link).first()
  if song_db:
    song_db.links = get_platform_links.dico_of_link_string(song_db.links)
    return render_template("sharing_page.html", song_db=song_db)
  else:
    return "<h1>Inconnu</h1>"
