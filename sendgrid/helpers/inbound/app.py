from config import Config
from flask import Flask, request
from parse import Parse

app = Flask(__name__)
config = Config()

@app.route (config.endpoint, methods =['POST'])
def inbound_parse():
    parse = Parse(config, request)
    print parse.key_values()
    # Tell SendGrid's Inbound Parse to stop sending POSTs
    # Everything is 200 OK :)
    return "OK"

if __name__=='__main__':
    app.run(debug=True, port=int("5000"))