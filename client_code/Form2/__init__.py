from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """Extrahiert Informationen aus der URL und prüft die Anmeldung"""
    # Beispiel: URL könnte zusätzliche Parameter wie `account_no` enthalten
    url_params = get_url_hash()  # Anvil-spezifische Methode, um URL-Parameter abzurufen
    account_no = url_params.get("account_no", "")
    password = url_params.get("password", "")

    if account_no and password:
      is_valid = anvil.server.call('check_login', account_no, password)
      if is_valid:
        alert("Erfolgreich angemeldet!")
      else:
        alert("Anmeldung fehlgeschlagen.")
    else:
      alert("Ungültige URL-Daten.")
      
    pass

def check_login_unsafe(username, password):
    # Unsicher: Direkte SQL-Eingabe ohne Schutz
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = app_tables.users.search(q.raw_sql(query))
    return bool(result)

def check_login(username, password):
    # Sicher: Verwendet vorbereitete Abfragen
    result = app_tables.users.search(
        q.all_of(q.column("username") == username, q.column("password") == password)
    )
    return bool(result)
