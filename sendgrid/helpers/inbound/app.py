"""Receiver module for processing SendGrid Inbound Parse messages.

See README.txt for usage instructions."""
try:
    from config import Config
except:
    # Python 3+, Travis
    from sendgrid.helpers.inbound.config import Config

try:
    from parse import Parse
except:
    # Python 3+, Travis
    from sendgrid.helpers.inbound.parse import Parse

from flask import Flask, request, render_template
import os

app = Flask(__name__)
config = Config()


def debug_enabled(config, port):
    """Return True only when debug mode is explicitly enabled and the app is
    running locally. Debug is never enabled when PORT is provided by the
    hosting platform (e.g. Heroku) or ENV is 'prod', since the Werkzeug
    debugger allows arbitrary code execution."""
    return bool(config.debug_mode) \
        and port == config.port \
        and os.environ.get('ENV') != 'prod'


@app.route('/', methods=['GET'])
def index():
    """Show index page to confirm that server is running."""
    return render_template('index.html')


@app.route(config.endpoint, methods=['POST'])
def inbound_parse():
    """Process POST from Inbound Parse and print received data."""
    parse = Parse(config, request)
    # Sample processing action
    print(parse.key_values())
    # Tell SendGrid's Inbound Parse to stop sending POSTs
    # Everything is 200 OK :)
    return "OK"


if __name__ == '__main__':
    # Be sure to set config.debug_mode to False in production
    port = int(os.environ.get("PORT", config.port))
    app.run(host='0.0.0.0', debug=debug_enabled(config, port), port=port)
