from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

app = Flask(__name__)
#app.config["SECRET_KEY"] = "insertkeyhere"

class myform(FlaskForm):
    serverName = StringField("Server Name")
    characterName = StringField("Character Name")
    
@app.route("/")
def index():
    return "<h2>This page is blank for now.</h2>"
