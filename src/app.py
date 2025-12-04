#!/usr/bin/python3

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from panel_sim import panel

app = QApplication(sys.argv)

control_panel = panel.ControlPanel()
control_panel.show()
app.exec()
