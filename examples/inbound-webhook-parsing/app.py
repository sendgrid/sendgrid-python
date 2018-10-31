from flask import Flask, request, Response
import os

HOST = '0.0.0.0'
PORT = 5000

app = Flask(__name__)


@app.route('/')
def hello():
    print("testing")
    return Response("Up and running", status=200)


@app.route('/parse_inbound', methods=['POST'])
def inbound_parser():
    data = request.form
    output = ""

    output += "------------------ INCOMING WEBHOOK DATA ------------------"
    output += "\n\n"
    output += "[HEADERS]\n"
    output += data['headers']
    output += "\n\n"
    output += "[DKIM]\n"
    output += data['dkim']
    output += "\n\n"
    output += "[FROM]\n"
    output += data['from']
    output += "\n\n"
    output += "[TO]\n"
    output += data['to']
    output += "\n\n"
    output += "[SUBJECT]\n"
    output += data['subject']
    output += "\n\n"
    output += "[BODY]\n"
    output += data['text']
    output += "\n\n"
    output += "[ATTACHMENTS]\n"
    output += data['attachments']
    output += "\n\n"
    output += "[CHARSETS]\n"
    output += data['charsets']
    output += "\n\n"
    output += "------------------ END WEBHOOK DATA ------------------"

    print(output)

    return Response(output, status=200)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
