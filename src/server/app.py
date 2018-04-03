from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

def start_flask_app():
    app.run()
