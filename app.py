from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


def load_keyboards():
    with open('keyboards.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/keyboard")
def keyboard():
    return render_template('keyboard.html')

@app.route("/game/RedDeadRedemption2")
def RedDeadRedemption2():
    return render_template('RedDeadRedemption2.html')

@app.route("/game/DetroitBecomeHuman")
def DetroitBecomeHuman():
    return render_template('DetroitBecomeHuman.html')


if __name__ == "__main__":
    app.run(debug=True)

