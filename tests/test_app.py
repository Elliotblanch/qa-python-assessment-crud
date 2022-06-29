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
