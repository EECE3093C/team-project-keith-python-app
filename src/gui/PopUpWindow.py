"""
------------------------------------------------------------------------------------------------------------
This file contins the definition for the popup window. This window will hold all the settings defined 
in the gui mockup and by the issues. The data collected fromt he popup window should be translated to 
the C++ API for analysis.

Please delete comments which do not reflect the current state of the file regardless of author.
------------------------------------------------------------------------------------------------------------
Change History:
3/9/2023    Caleb Hendrix   inital code for iteration 3
"""

from PyQt6.QtWidgets import QMainWindow

class PopUpWindow(QMainWindow):
    def __init__(self):
        super(PopUpWindow, self).__init__()
        self.setWindowTitle("About your data")
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)