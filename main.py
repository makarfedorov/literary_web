from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/research")
def load_researh():
    return render_template('research.html')

@app.route("/materials")
def load_materials():
    return render_template('materials.html')
