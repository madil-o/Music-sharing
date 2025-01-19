
from . import db

class Url(db.Model):
  id = db.Column(db.String(9), primary_key=True)
  song = db.Column(db.String(100))
  links = db.Column(db.String(1500))
  