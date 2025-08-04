import json
from databases import Database
from flask import session

DATABASE_URL = "sqlite+aiosqlite:///logs.db"
database = Database(DATABASE_URL)


async def init_db():
    await database.connect()

    # Tabel pentru loguri
    log_query = """
    CREATE TABLE IF NOT EXISTS log_entries (
        id INTEGER PRIMARY KEY,
        endpoint TEXT NOT NULL,
        request_data TEXT NOT NULL,
        response_data TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        status_code INTEGER NOT NULL,
        username TEXT
    );
    """
    await database.execute(query=log_query)

    # Tabel pentru utilizatori
    user_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        is_admin BOOLEAN DEFAULT 0
    );
    """
    await database.execute(query=user_query)


async def log_request(endpoint: str, request_data: dict, response_data: dict, status_code: int):
    username = session.get("user", "anonymous")
    query = """
    INSERT INTO log_entries (endpoint, request_data, response_data, status_code, username)
    VALUES (:endpoint, :request_data, :response_data, :status_code, :username)
    """
    values = {
        "endpoint": endpoint,
        "request_data": json.dumps(request_data),
        "response_data": json.dumps(response_data),
        "status_code": status_code,
        "username": username
    }
    await database.execute(query=query, values=values)
