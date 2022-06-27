from application import app, db
from application.models import player, party
from application.forms import PlayerForm, PartyForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():


@app.route('/about')
def about():


@app.route('/addplayer', methods = ['GET', 'POST'])
def add():
    form = PlayerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            playerData = Player(
                name = form.name.data,
                charClass = form.charClass.data,
                level = form.level.data,
                hp = form.hp.data,
                ac = form.ac.data,
                caster = form.caster.data,
                partyID = form.partyID.data
            )
            db.session.add(playerData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addplayer.html', form=form)