import sqlite3

DB_NAME = "errors.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error TEXT,
            explanation TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_error(error, explanation):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO history (error, explanation) VALUES (?, ?)",
        (error, explanation)
    )
    conn.commit()
    conn.close()

def fetch_history():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT error, explanation FROM history ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

 
