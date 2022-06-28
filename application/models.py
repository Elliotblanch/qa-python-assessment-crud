from application import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    charClass = db.Column(db.String(30))
    level = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    ac = db.Column(db.Integer)
    caster = db.Column(db.Boolean, default=False)
    partyID = db.Column(db.Integer, foreign_key=True)


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))