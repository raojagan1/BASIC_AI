import sqlite3
import sys


def create_event(db: str, name: str, payload: str) -> int:
    with sqlite3.connect(db) as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, name TEXT, payload TEXT)')
        cursor = connection.execute('INSERT INTO events (name, payload) VALUES (?, ?)', (name, payload))
        connection.commit()
        return int(cursor.lastrowid)

if __name__ == '__main__':
    if '--test' in sys.argv:
        event_id = create_event(':memory:', 'test.event', '{}')
        assert event_id == 1
        print('PASS: SQLite event was inserted')
    else:
        print(create_event('events.db', 'file.created', '{"file":"report.pdf"}'))
