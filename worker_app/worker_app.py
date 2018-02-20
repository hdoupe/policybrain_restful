from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hello, world"

@app.route('/start_task', methods=['GET', 'POST'])
def start_task():
    return "ping pong"
