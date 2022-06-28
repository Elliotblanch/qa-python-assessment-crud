from application import app, db
from application.models import player, party
from application.forms import PlayerForm, PartyForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    player = Player.query.all()

    return render_template('player.html', players=player)

@app.route('/about')
def about():
    return render_template("about.html")

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

@app.route('/updateplayer/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = PlayerForm()
    player = Player.query.get(id)
    if form.validate_on_submit():
        player.name = form.name.data,
        player.charClass = form.charClass.data,
        player.level = form.level.data,
        player.hp = form.hp.data,
        player.ac = form.ac.data,
        player.caster = form.caster.data,
        player.partyID = form.partyID.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method = 'GET'
        form.name.data = player.name,
        form.charClass.data = player.charClass,
        form.level.data = player.level,
        form.hp.data = player.hp,
        form.ac.data = player.ac,
        form.caster.data = player.caster
        form.partyID.data = player.partyID
    return render_template('updateplayer.html', form=form)

@app.route('/deleteplayer/<int:id>')
def delete(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('index'))
    