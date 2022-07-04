from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, SubmitField

class PlayerForm(FlaskForm):
    name = StringField("Name")
    charClass = SelectField("Class", choices =[
        ("Artficer", "Artificer"),
        ("Barbarian", "Barbarian"),
        ("Bard", "Bard"),
        ("Cleric", "Cleric"),
        ("Druid", "Druid"),
        ("Fighter", "Fighter"),
        ("Monk", "Monk"),
        ("Paladin", "Paladin"),
        ("Ranger", "Ranger"),
        ("Rogue", "Rogue"),
        ("Sorcerer", "Sorcerer"),
        ("Warlock", "Warlock"),
        ("Wizard", "Wizard")
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