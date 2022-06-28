from application import db
from application.models import Player, Party
from application import __init__

db.drop_all()
db.create_all()

sample_player = player(
    name = "Shen Shuhan",
    charClass = "Fighter",
    level = 5,
    hp = 55,
    ac = 16,
    caster = True,
    partyID = 1
)

sample_party = party(
    name = "dynasty"
)