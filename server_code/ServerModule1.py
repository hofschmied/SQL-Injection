import sqlite3
import anvil.server

# Verbindung zur SQLite-Datenbank herstellen
def get_db_connection():
    return sqlite3.connect('database.db')

@anvil.server.callable
def get_user_data(account_no=None):
    db = get_db_connection()
    cursor = db.cursor()
    

@anvil.server.callable
def get_user(user_id):
    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM users WHERE AccountNo = ?", (user_id,))
    user_id = cursor.fetchone()
    db.close()
  