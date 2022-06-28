from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, SubmitField

class PlayerForm(FlaskForm):
    name = StringField("Name")
    charClass = SelectField("Class", choices =[
        ("artficer", "Artificer"),
        ("barbarian", "Barbarian"),
        ("bard", "Bard"),
        ("cleric", "Cleric"),
        ("druid", "Druid"),
        ("fighter", "Fighter"),
        ("monk", "Monk"),
        ("paladin", "Paladin"),
        ("ranger", "Ranger"),
        ("rogue", "Rogue"),
        ("sorcerer", "Sorcerer"),
        ("warlock", "Warlock"),
        ("wizard", "Wizard")
    ])
    level = IntegerField("Level")
    hp = IntegerField("HP")
    ac = IntegerField("Armour Class")
    caster = BooleanField("Caster?")
    partyID = IntegerField("Party ID") 
    submit = SubmitField("Submit")

class PartyForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")