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
    form = request.form

    data = {
        'headers': form['headers'],
        'dkim': form['dkim'],
        'from': form['from'],
        'to': form['to'],
        'subject': form['subject'],
        'body': form['text'],
        'attachments': form['attachments'],
        'charsets': form['charsets']
    }

    output = """\
    ------------------ INCOMING WEBHOOK DATA ------------------

    [HEADERS]
    {headers}

    [DKIM]
    {dkim}

    [FROM]
    {from}

    [TO]
    {to}

    [SUBJECT]
    {subject}

    [BODY]
    {body}

    [ATTACHMENTS]
    {attachments}

    [CHARSETS]
    {charsets}

    ------------------ END WEBHOOK DATA ------------------
    """.format(**data)

    print(output)

    return Response(output, status=200)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
