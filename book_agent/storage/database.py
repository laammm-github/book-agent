"""SQLite persistence layer for book agent."""

import sqlite3
from pathlib import Path


class Database:
    def __init__(self, path: str = "book_agent.db"):
        self.path = Path(path)
        self.conn = sqlite3.connect(self.path)
        self._init()

    def _init(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, content TEXT)"
        )
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, book_id INTEGER, content TEXT)"
        )
        self.conn.commit()

    def add_book(self, title: str, content: str):
        self.conn.execute(
            "INSERT INTO books(title, content) VALUES (?, ?)",
            (title, content),
        )
        self.conn.commit()
