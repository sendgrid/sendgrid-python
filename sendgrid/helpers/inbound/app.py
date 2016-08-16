"""Receiver module for processing SendGrid Inbound Parse messages"""
from config import Config
from flask import Flask, request
from parse import Parse

app = Flask(__name__)
config = Config()

@app.route (config.endpoint, methods =['POST'])
def inbound_parse():
    parse = Parse(config, request)
    # Sample proccessing action
    print(parse.key_values())
    # Tell SendGrid's Inbound Parse to stop sending POSTs
    # Everything is 200 OK :)
    return "OK"

if __name__=='__main__':
    # Be sure to set config.debug_mode to False in production
    app.run(host = '0.0.0.0', debug=config.debug_mode, port=int(config.port))
