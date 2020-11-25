from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'

@app.route('/data-exploration')
def data_exploration():
    return 'data-exploration'


@app.route('/analysis')
def analysis():
    return 'analysis'


