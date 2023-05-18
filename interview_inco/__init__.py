from flask import Flask, render_template
from interview_inco.contorl import control
from interview_inco import db

app = Flask(__name__)
app.config.from_pyfile("./config.py")
db.init_app(app)

@app.route("/")
def hello_world():
    return render_template("index.html")
