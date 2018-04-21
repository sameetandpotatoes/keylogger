from flask import Flask
from models.user import User
from models.phrasestroke import PhraseStroke
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
API_PORT = 6969

# Pretend we have a user u, and a bunch of their phrasestrokes
sameet = User()
strokes = [
    PhraseStroke(start_time=datetime.now() - timedelta(seconds=3),
                 phrase="www.gmail.com", terminating="Key.enter"),
    PhraseStroke(start_time=datetime.now() - timedelta(seconds=2),
                phrase="sameet.sapra", terminating="Key.tab"),
    PhraseStroke(start_time=datetime.now() - timedelta(seconds=1),
                phrase="mycompletelyrealpassword", terminating="Key.tab")
]

@app.route('/websites/<website>'):
    return "Websites %s" % website

@app.route('/users/<ip>')
def index():
    return "Hello, World! %s" % ip

@app.route('/copypasta'):
    # TODO return copied strings that people may have copied?

def start_flask_app():
    logger.info("Starting flask server on port {}".format(API_PORT))
    app.run(host='0.0.0.0', port=API_PORT)
