from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)

        debug_flag = True
        if debug_flag:
            print("Debugging aktiv.")

        self.url = anvil.js.window.location.href
        print(f"Geladene URL: {self.url}")
      
        self.accNo = anvil.server.call('getQuery', self.url)
        if self.accNo is None:
            self.label_1.text = "Login Successful but AccountNo was not passed."
            print("Warnung: Keine Kontonummer erhalten.")
        else:
            print(f"Gefundene Kontonummer: {self.accNo}")
            if isinstance(self.accNo, str):
                res = anvil.server.call('getUserId', self.accNo)
                self.label_1.text = res
            else:
                print("Kontonummer ist kein gültiger String.")

    def button_1_click(self, **event_args):
        print("Zurücksetzen der Sitzung gestartet...")
        anvil.server.call('resetSession')
        print("Sitzung erfolgreich zurückgesetzt.")
        open_form('Form1')
        print("Zur Login-Formular gewechselt.")
