"""
------------------------------------------------------------------------------------------------------------
This file is the inital version for the main window of the application for the Time Series Data Analyzer.
Please limit additions to this file to changes which pertain to the main window. For future iterations, when
making new widgets, try to make seperate files/classes for those widgets and then include them here.

Please delete comments which do not reflect the current state of the file regardless of author.
------------------------------------------------------------------------------------------------------------
Change History:
2/19/2023   Caleb Hendrix   Initial version for iteration 1
"""

from PyQt6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QPlainTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Time Series Data Analyzer")
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        # Caleb Hendrix 2/19/2023
        # Just using a simple button for now as the main action
        self.button = QPushButton("Process my data")
        self.button.clicked.connect(self.button_clicked_event)
        
        # Caleb Hendrix 2/19/2023
        # This text entry mimicks what we expect users to be able
        # to do when selecting a data file locally.
        self.entryText = ''
        self.entryLine = QLineEdit()
        self.entryLine.textChanged.connect(self.entry_line_changed)

        # Caleb Hendrix 2/19/2023
        # This text box just allows us to see output that we want
        # for testing.
        self.outputArea = QPlainTextEdit()
        self.outputArea.resize(500, 250)

        # Caleb Hendrix 2/19/2023
        # This widget creates a vertical layout of the added widgets
        self.myLayout = QVBoxLayout()
        self.myLayout.addWidget(self.entryLine)
        self.myLayout.addWidget(self.button)
        self.myLayout.addWidget(self.outputArea)

        # Caleb Hendrix 2/19/2023
        # We have to set all the widgets specified in the layout in
        # a main widget which will be the central widget in the window.
        self.widget = QWidget()
        self.widget.setLayout(self.myLayout)
        self.setCentralWidget(self.widget)

    # Caleb Hendrix 2/19/2023
    # When we press the button we can send some text to the output box.
    # This is also where we can call a C++ function to test that functionality.
    def button_clicked_event(self):
        self.outputArea.appendPlainText("Data: %s processed!" % self.entryText)

    # Caleb Hendrix 2/19/2023
    # When someone changes the entry in the line edit we want to track that
    # change with our state variable.
    def entry_line_changed(self):
        self.entryText = self.entryLine.text()