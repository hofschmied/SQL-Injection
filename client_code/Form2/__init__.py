
from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.js
from anvil.js.window import URLSearchParams

class Form2(Form2Template):
    def __init__(self, **properties):
        
        self.init_components(**properties)

        hash_str = anvil.js.window.location.hash