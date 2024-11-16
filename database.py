import sqlite3

def init_db():
    conn = sqlite3.connect('requests.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_number TEXT,
            amount TEXT,
            reason TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_request(project_number, amount, reason):
    try:
        conn = sqlite3.connect('requests.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO requests (project_number, amount, reason)
            VALUES (?, ?, ?)
        ''', (project_number, amount, reason))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding request to database: {e}")
        return False
