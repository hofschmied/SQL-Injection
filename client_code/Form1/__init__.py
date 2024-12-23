from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def perform_login(self, mode):
        """
        """
        username = self.text_box_1.text
        password = self.text_box_2.text

        if mode == "unsafe":
            result = anvil.server.call('login_insecure', username, password)
        else:
            result = anvil.server.call('login_secure', username, password)
        
        if result == "Eingeloggt!":
            self.label_status.text = result
          
            #open_form('Form2')
        else:
            self.label_status.text = result

    def text_box_2_pressed_enter(self, **event_args):
        """
        """

    def button_unsafe_clicked(self, **event_args):
      """This method is called when the radio button is selected."""
      self.perform_login(mode="unsafe")

    def button_nsafe_clicked(self, **event_args):
      """This method is called when the radio button is selected."""
      self.perform_login(mode="safe")
