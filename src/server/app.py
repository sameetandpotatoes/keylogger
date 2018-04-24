from flask import Flask
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
API_PORT = 6969


@app.route('/websites/<website>')
def websites():
    return "Websites %s" % website


@app.route('/users/<ip>')
def index():
    return "Hello, World! %s" % ip

@app.route('/users/<os>')
def users_by_os():
    # TODO convert Mac to Darwin, Linux to etc, Windows to etc.
    pass

@app.route('/copypasta')
def most_copied_phrases():
    pass


def start_flask_app():
    logger.info("Starting flask server on port {}".format(API_PORT))
    app.run(host='0.0.0.0', port=API_PORT)
