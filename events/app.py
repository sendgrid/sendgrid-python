import os
import json
import sqlite3

from flask import Flask, request, g, jsonify


DATABASE = './data/events.db'
app = Flask(__name__)


def create_table():
    """Create a table to store received events if it does not yet exist"""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY, 
            timestamp INTEGER,
            email TEXT,
            content TEXT
        )
    ''')
    db.commit()
    db.close()


def get_db():
    """Get a connection to the database"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def get_events(email=None):
    """Get events from the DB, optionally filtered by email address"""
    db = get_db()
    c = db.cursor()
    query = 'SELECT * FROM EVENTS'
    if email is not None:
        query = query + ' WHERE email=:email'
    query = query + ' ORDER BY timestamp DESC'
    c.execute(query, {'email': email})
    return c.fetchall()


@app.teardown_appcontext
def close_connection(exception):
    """Close the connection at the end of the request"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def create_event_record(event):
    """Return a tuple containing the fields for our SQL record"""
    return (event['timestamp'], event['email'], json.dumps(event))


@app.route('/events', methods=['POST'])
def consume_events():
    """Consume events and store them in our SQLite DB"""
    events = request.get_json()
    with get_db() as db:
        c = db.cursor()
        event_records = [create_event_record(e) for e in events]
        for record in event_records:
            app.logger.info('Received event: %s', record)
        c.executemany('INSERT INTO events (timestamp, email, content) VALUES (?, ?, ?)', event_records)
    return 'OK'


@app.route('/', methods=['GET'])
def index():
    """Return events currently stored in our DB"""
    events = get_events(request.args.get('email'))
    events_content = [json.loads(e['content']) for e in events]
    return jsonify({
        'count': len(events_content),
        'events': events_content,
    })


if __name__ == '__main__':
    if not os.path.exists('./data'):
        os.makedirs('./data')
    create_table()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=port)
