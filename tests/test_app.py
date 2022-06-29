

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
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
        db.session.add(sample_player)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
