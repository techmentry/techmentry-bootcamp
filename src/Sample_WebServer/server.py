from flask import Flask, send_file
import random

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>hello visitor!</p>"


@app.route('/mathop/square/<int:num>')
def square(num):
    return f"<p>The square of {num} is <b>{num ** 2}</b>"


@app.route('/mathop/random')
def get_random():
    return f"<p>Here is a random number: <b>{random.randint(1, 100)}</b></p>"


@app.route('/get_image')
def get_image():
    return send_file("cute_cats.jpeg", mimetype='image/gif')
