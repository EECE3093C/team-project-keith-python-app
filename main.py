"""
------------------------------------------------------------------------------------------------------------
This file just serves as main for all the python code. The QApplication, of which there should only be one, 
is initialized here.

Please delete comments which do not reflect the current state of the file regardless of author.
------------------------------------------------------------------------------------------------------------
Change History:
2/19/2023   Caleb Hendrix   Initial Version for iteration 1
"""

from PyQt6.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()