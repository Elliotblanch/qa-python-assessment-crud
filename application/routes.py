from application import app, db
from application.models import Player, Party
from application.forms import PlayerForm, PartyForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    player = Player.query.all()

    return render_template('player.html', players=player)

@app.route('/partyindex')
def partyindex():
    party = Party.query.all()

    return render_template('party.html', parties=party)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/addplayer', methods = ['GET', 'POST'])
def addplayer():
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
def updateplayer(id):
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
    elif request.method == 'GET':
        form.name.data = player.name,
        form.charClass.data = player.charClass,
        form.level.data = player.level,
        form.hp.data = player.hp,
        form.ac.data = player.ac,
        form.caster.data = player.caster
        form.partyID.data = player.partyID
    return render_template('updateplayer.html', form=form)

@app.route('/deleteplayer/<int:id>')
def deleteplayer(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addparty', methods = ['GET', 'POST'])
def addparty():
    form = PartyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            partyData = Party(
            name = form.name.data
            )
            db.session.add(partyData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addparty.html', form=form)

@app.route('/updateparty/<int:id>', methods = ['GET', 'POST'])
def updateparty(id):
    form = PartyForm()
    party = Party.query.get(id)
    if form.validate_on_submit():
        party.name = form.name.data,
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = party.name    
    return render_template('updateparty.html', form=form)


@app.route('/deleteparty/<int:id>')
def deleteparty(id):
    party = Party.query.get(id)
    db.session.delete(party)
    db.session.commit()
    return redirect(url_for('index'))
