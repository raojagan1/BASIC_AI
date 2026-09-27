import sqlite3
import sys


def migrate(connection: sqlite3.Connection) -> None:
    connection.execute('CREATE TABLE IF NOT EXISTS schema_version (version INTEGER NOT NULL)')
    if connection.execute('SELECT COUNT(*) FROM schema_version').fetchone()[0] == 0:
        connection.execute('CREATE TABLE events (id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
        connection.execute('INSERT INTO schema_version VALUES (1)')
    columns = {row[1] for row in connection.execute('PRAGMA table_info(events)')}
    if 'created_at' not in columns:
        connection.execute('ALTER TABLE events ADD COLUMN created_at TEXT')
        connection.execute('UPDATE schema_version SET version = 2')
    connection.commit()

if __name__ == '__main__':
    connection = sqlite3.connect(':memory:')
    migrate(connection)
    migrate(connection)
    assert 'created_at' in {row[1] for row in connection.execute('PRAGMA table_info(events)')}
    print('PASS: migration is repeatable')
