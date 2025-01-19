from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as query
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        print("Initialisierung von Form1 gestartet...")
        self.extra_flag = False

        user_logged_in = anvil.server.call('login_ueberpruefen')
        if user_logged_in:
            print("Benutzer ist eingeloggt. Wechselt zu Form2...")
            open_form('Form2')
        else:
            print("Benutzer nicht eingeloggt. URL-Hash wird gesetzt.")
            set_url_hash()

    def button_1_click(self, **event_args):
        print("Login-Prozess gestartet...")

        input_username = self.text_box_1.text
        input_password = self.text_box_2.text
        remember_me = self.check_box_1.checked

        print(f"Benutzername eingegeben: {input_username}")

        login_response = anvil.server.call("login", input_password, input_username, remember_me)
        login_message, login_successful = login_response[0], login_response[1]

        if not login_successful:
            print("Login fehlgeschlagen. Zeigt Fehlermeldung an...")
            alert(login_message, title="Login Fehlgeschlagen")
        else:
            print("Login erfolgreich, weitere Überprüfung wird durchgeführt...")

            account_no = anvil.server.call('getAccNo', input_username, input_password)
            if account_no is not None:
                print(f"Kontonummer gefunden: {account_no}")
                set_url_hash(f'?AccountNo={account_no}')
            else:
                print("Keine Kontonummer zurückgegeben. Fortsetzung des Login-Prozesses...")

            open_form('Form2')
            print("Form2 wurde geöffnet.")