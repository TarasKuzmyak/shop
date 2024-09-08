from flask import Flask, render_template, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os






app = Flask(__name__)









@app.route("/")
def home():
    return render_template('home.html')

@app.route("/game")
def game():
    return render_template('game.html')


@app.route("/keyboard")
def GrandTheftAuto5():
    return render_template('keyboard.html')

@app.route("/game/RedDeadRedemption2")
def RedDeadRedemption2():
    return render_template('RedDeadRedemption2.html')


@app.route("/game/DetroitBecomeHuman")
def DetroitBecomeHuman():
    return render_template('DetroitBecomeHuman.html')
app.run()