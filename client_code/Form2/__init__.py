from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):

    def __init__(self, **properties):
        self.init_components(**properties)
        print("Form2 wird initialisiert...")

        self.accNo = anvil.server.call('getQuery', self.url)
      
        self.url = anvil.js.window.location.href
        print(f"Aktuelle URL: {self.url}")

        if self.accNo is None:
            self.label_1.text = "Login Successful but AccountNo was not passed."
            print("Keine Kontonummer gefunden.")
        else:
            print(f"Kontonummer: {self.accNo}")
            res = anvil.server.call('getUsrId', self.accNo)
            self.label_1.text = res

    def button_1_click(self, **event_args):
        print("Logout wird ausgeführt...")
        anvil.server.call('resetSession')
        print("Sitzung wurde zurückgesetzt.")
        open_form('Form1')
        print("Form1 wurde geöffnet.")