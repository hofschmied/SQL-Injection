from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from ..Form2 import Form2
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    username = self.text_box_1.text
    password = self.text_box_2.text

    if self.check_box_4.checked:
      is_valid = anvil.server.call('check_login_unsafe', username, password)
    else:
      is_valid = anvil.server.call('check_login', username, password)
    if is_valid:
      self.Loginbox.text = "geschafft"
    else:
      self.Loginbox.text = "nicht geschafft"

  