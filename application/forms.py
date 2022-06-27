from flask_wtf import FlaskForms
from wtforms import StringField, BooleanField, IntegerField, SubmitField

class PlayerForm(FlaskForm):
    name = StringField("Name")
    charClass = StringField("Class")
    level = IntegerField("Level")
    hp = IntegerField("HP")
    ac = IntegerField("Armour Class")
    caster = BooleanField("Caster?")
    partyID = IntegerField("Party ID") 