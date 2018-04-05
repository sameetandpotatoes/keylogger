from flask import Flask
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
API_PORT = 6969

@app.route('/')
def index():
    return "Hello, World!"

def start_flask_app():
    logger.info("Starting flask server on port {}".format(API_PORT))
    app.run(host='0.0.0.0', port=API_PORT)
