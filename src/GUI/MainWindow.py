"""
------------------------------------------------------------------------------------------------------------
This file is the inital version for the main window of the application for the Time Series Data Analyzer.
Please limit additions to this file to changes which pertain to the main window. For future iterations, when
making new widgets, try to make seperate files/classes for those widgets and then include them here.

Please delete comments which do not reflect the current state of the file regardless of author.
------------------------------------------------------------------------------------------------------------
Change History:
2/19/2023   Caleb Hendrix   Initial version for iteration 1
3/2/2023    Caleb Hendrix   Included the test C API call into the button click
3/7/2023    Caleb Hendrix   Deprecated old window code and added the Analyze button
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout
from PyQt6.QtCore import Qt
from gui.AnalyzeButton import AnalyzeButton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Time Series Data Analyzer")
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        # The Analyze button controls progress to the pop-up window
        self.button = AnalyzeButton()

        # Caleb Hendrix 2/19/2023
        # This widget creates a vertical layout of the added widgets
        # When you add a widget to the layout you may need to adjust
        # row and column specifications of the others.
        self.myLayout = QGridLayout()
        self.myLayout.addWidget(self.button, 0,0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        # Caleb Hendrix 2/19/2023
        # We have to set all the widgets specified in the layout in
        # a main widget which will be the central widget in the window.
        self.widget = QWidget()
        self.widget.setLayout(self.myLayout)
        self.setCentralWidget(self.widget)