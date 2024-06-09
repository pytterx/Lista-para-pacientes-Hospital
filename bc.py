import sqlite3



conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''
        CREATE TABLE IF NOT EXISTS data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sintoma TEXT NOT NULL,
            numero TEXT NOT NULL,
            data_de_naicimento TEXT NOT NULL
        )
    ''')
conn.commit()
conn.close()
