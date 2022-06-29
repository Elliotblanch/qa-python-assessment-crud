from application import models, db, app
from application.models import Player, Party
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
       
        sample_party = Party(
            name = "Dynasty"
        )
        sample_player = Player(
            name = "Shen Shuhan",
            charClass = "Fighter",
            level = 5,
            hp = 55,
            ac = 16,
            caster = True,
            partyID = 1
        )
        db.session.add(sample_party)
        db.session.add(sample_player)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_party_index_get(self):
        response = self.client.get(url_for('partyindex'))
        self.assertEqual(response.status_code, 200)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_player_get(self):
        response = self.client.get(url_for('addplayer'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_party_get(self):
        response = self.client.get(url_for('addparty'))
        self.assertEqual(response.status_code, 200)


class TestAddPlayer(TestBase):
    def test_add_Player(self):
        response = self.client.post(
            url_for('addplayer'),
            data = dict(name = "Feng Lei",
                charClass = "Ranger",
                level = 3,
                hp = 30,
                ac = 17,
                caster = True,
                partyID = 1
            )
        )
        
        assert Player.query.filter_by(name="Feng Lei").id == 2

class TestAddParty(TestBase):
    def test_add_Party(self):
        response = self.client.post(
            url_for('addparty'),
            data = dict(name = "Crucible")
        )
        
        assert Party.query.filter_by(name="Crucible").id == 2

class TestUpdatePlayer(TestBase):
    def test_update_player(self):

        assert

class TestUpdateParty(TestBase):
    def test_update_party(self):

        assert


class TestDeletePlayer(TestBase):
    def test_delete_player(self):
        response = self.client.delete(
            url_for('deleteplayer'),
            data = dict(name = "Shen Shuhan")
        )
        assert len(Player.query.all()) == 0

        
class TestDeleteParty(TestBase):
    def test_delete_party(self):
        response = self.client.delete(
            url_for('deleteparty'),
            data = dict(name = "Dynasty")
        )
        assert len(Party.query.all()) == 0