from flask import Flask

app = Flask(__name__)



@app.route("/")
def print_hello():
    return "<p>Nusaiba was here :)</p>"