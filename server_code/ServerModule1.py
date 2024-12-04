import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3
from anvil.tables import app_tables


db = data_files['database.db']
@anvil.server.callable
def check_login(username, password):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

@anvil.server.callable
def check_login_unsafe(username, password):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user is not None