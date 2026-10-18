```python
import os
import sqlite3
from datetime import date, timedelta
from tkinter import messagebox
import customtkinter as ctk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'habit_tracker.db')
DAYS_SHOWN = 7

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


class Database:
    def __init__(self, path) -> None:
        self.conn = sqlite3.connect(path)
        self.conn.execute('PRAGMA foreign_keys = ON')
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL
        )
        """)

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS checks (
            habit_id INTEGER NOT NULL,
            day TEXT NOT NULL,
            PRIMARY KEY (habit_id, day),
            FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
        )
        """)

        self.conn.commit()

    def add_habit(self, name):
        self.conn.execute(
            "INSERT INTO habits (name, created_at) VALUES (?, ?)",
            (name, date.today().isoformat())
        )
        self.conn.commit()

    def delete_habit(self, habit_id):
        self.conn.execute(
            "DELETE FROM habits WHERE id = ?", (habit_id,)
        )
        self.conn.commit()

    def get_habits(self):
        cursor = self.conn.execute(
            "SELECT id, name FROM habits ORDER BY id"
        )
        return cursor.fetchall()

    def get_checked_days(self, habit_id):
        cursor = self.conn.execute(
            "SELECT day FROM checks WHERE habit_id = ?",
            (habit_id,)
        )
        return {row[0] for row in cursor.fetchall()}

    def set_check(self, habit_id, day, done):
        if done:
            self.conn.execute(
                "INSERT OR IGNORE INTO checks (habit_id, day) VALUES (?, ?)",
                (habit_id, day)
            )
        else:
            self.conn.execute(
