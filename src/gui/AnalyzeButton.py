"""
------------------------------------------------------------------------------------------------------------
This file defines the button class for the push button that will initialize the data processing of the 
application.

Please delete comments which do not reflect the current state of the file regardless of author.
------------------------------------------------------------------------------------------------------------
Change History:
3/7/2023   Caleb Hendrix   Initial version for iteration 3
"""

from PyQt6.QtWidgets import QPushButton
from gui.PopUpWindow import PopUpWindow

class AnalyzeButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Analyze")
        self.setDefault(True)
        self.setFixedSize(75, 25)

        self.clicked.connect(self.onButtonClick)
        self.popup = None

    def onButtonClick(self):
        # <Caleb Hendrix>
        # We will need to call the initializer for the pop_up window here.
        # TODO I think it would be good to make the analyze button non-clickable 
        # as long as the popupmenu is open, then on close of popup menu, we
        # enable the button again
        if self.popup == None:
            self.popup = PopUpWindow()
        self.popup.show()