from flask import render_template
from PageF import app
import json


with open("PageF/JSON.txt", "r") as J:
    Dander =json.loads(J.read())
@app.route('/')
@app.route('/index')
def i():
    return render_template("Job-Viewer.html", all=Dander)
@app.route("/placeholder")
def p():
    return render_template("placeholder.html")
