from application import db
from application.models import player, party
from application import __init__

db.drop_all()
db.create_all()

sample_player = Player(
    name = "Shen Shuhan",
    charClass = "Fighter",
    level = 5,
    hp = 55,
    ac = 16,
    caster = True,
    partyID = 1
)

sample_party = Party(
    name = "dynasty"
)