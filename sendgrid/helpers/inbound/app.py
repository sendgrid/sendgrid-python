"""Receiver module for processing SendGrid Inbound Parse messages"""
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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route(config.endpoint, methods=['POST'])
def inbound_parse():
    parse = Parse(config, request)
    # Sample proccessing action
    print(parse.key_values())
    # Tell SendGrid's Inbound Parse to stop sending POSTs
    # Everything is 200 OK :)
    return "OK"


if __name__ == '__main__':
    # Be sure to set config.debug_mode to False in production
    port = int(os.environ.get("PORT", config.port))
    if port != config.port:
        config.debug = False
    app.run(host='0.0.0.0', debug=config.debug_mode, port=port)
