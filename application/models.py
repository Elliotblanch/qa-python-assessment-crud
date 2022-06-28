from application import db

class Player(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(30))
    charClass = db.Column(db.String(30))
    level = db.Column(db.integer)
    hp = db.Column(db.integer)
    ac = db.Column(db.integer)
    caster = db.Column(db.Boolean, default=False)
    partyID = db.Column(db.integer, foreign_key=True)

class Party(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(30))