import codecs
import sqlite3
import json

def get_all_users( json_str = False):
    conn = sqlite3.connect('my_database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    rows = cursor.execute('''
        SELECT *
        FROM Application,Service,Client,Worker
        ''').fetchall()
    conn.commit()
    conn.close()

    if json_str:
        return json.dumps([dict(ix) for ix in rows ])
    return rows

print(get_all_users(json_str=True))
