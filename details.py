from flask import Flask

app = Flask(__name__)



@app.route("https://details-nusaiba.herokuapp.com/")
def print_hello():
    return "<p>Hello, World!</p>"