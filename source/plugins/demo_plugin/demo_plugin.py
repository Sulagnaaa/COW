from plugin import Plugin, PluginAction
from PyQt5.QtWidgets import QDialog
import numpy as np
from . import helper

class DemoPlugin(Plugin):
    def __init__(self):
        super().__init__("Demo", "Misc")

    def get_actions(self):
        return [PluginAction("Echo", self.template_function, False)]

    def template_function(self, window):
        dlg = QDialog(window)
        dlg.setWindowTitle(self.plugin_name + " " + helper.greeting_message)
        dlg.exec_()

    def process(self, frame):
        return (frame * 0.99).astype(np.uint8)

