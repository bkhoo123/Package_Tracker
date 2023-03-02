from flask import render_template, Flask
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def index():
    return "<h1>Package Tracker</h1>"

@app.route('/new_package', ['GET', 'POST'])
def new_route():
    return render_template('shipping_request.html')