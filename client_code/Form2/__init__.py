from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):

    def __init__(self, **properties):
        self.init_components(**properties)

        # Zusätzlicher unnötiger Codeblock
        debug_flag = True
        if debug_flag:
            print("Debugging aktiv.")

        # URL abrufen und anzeigen (unverändert)
        self.url = anvil.js.window.location.href
        print(f"Geladene URL: {self.url}")  # Debug-Ausgabe

        # Kontonummer abrufen
        self.accNo = anvil.server.call('getQuery', self.url)
        if self.accNo is None:
            self.label_1.text = "Login Successful but AccountNo was not passed."
            print("Warnung: Keine Kontonummer erhalten.")  # Unnötige Ausgabe
        else:
            print(f"Gefundene Kontonummer: {self.accNo}")
            # Zusätzlicher unnötiger Check vor dem Abrufen der Benutzer-ID
            if isinstance(self.accNo, str):
                res = anvil.server.call('getUsrId', self.accNo)
                self.label_1.text = res
            else:
                print("Kontonummer ist kein gültiger String.")

        # Noch ein unnötiger Block
        for i in range(1):
            print("Einmalige Schleife, tut nichts Nützliches.")

    def button_1_click(self, **event_args):
        """Diese Methode wird aufgerufen, wenn die Schaltfläche geklickt wird"""
        print("Zurücksetzen der Sitzung gestartet...")  # Unnötige Debug-Ausgabe
        anvil.server.call('resetSession')
        print("Sitzung erfolgreich zurückgesetzt.")  # Debug-Ausgabe
        open_form('Form1')
        print("Zur Login-Formular gewechselt.")  # Unnötige Debug-Ausgabe
