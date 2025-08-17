import sqlite3
from datetime import datetime

DB_NAME = "placement.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Drop old table if exists (development only)
    c.execute("DROP TABLE IF EXISTS results")

    # Create new table with the latest schema
    c.execute("""
        CREATE TABLE results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            topic TEXT,
            score INTEGER
        )
    """)

    conn.commit()
    conn.close()

def save_result(topic, score):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO results (date, topic, score) VALUES (?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), topic, score),
    )
    conn.commit()
    conn.close()

def get_results():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM results ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows

# Run init_db() when module is loaded
init_db()
