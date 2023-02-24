"""
------------------------------------------------------------------------------------------------------------
This is an example unit test framework fro the python GUIs in this project.
Please use this as an example for making unit tests for the widgets to be made.
------------------------------------------------------------------------------------------------------------
"""
import unittest
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from src.GUI.MainWindow import MainWindow

class MainWindowTest(unittest.TestCase):
    def setUp(self):
        self.form = MainWindow()

    # We just want to clear everything to do a fresh test
    def clearAllEntries(self):
        self.form.entryLine.clear()
        self.form.outputArea.clear()

    # Here we clear all the entries, set the entry line to 
    # contain our test string and then we "press" the button.
    # This should call the clicked event and then we check
    # the output with an assert. All unit tests should be 
    # asserting some exected value.
    def test_entryLineAndProcessData(self):
        self.clearAllEntries()
        self.form.entryLine.insert("TestCSV.csv")

        processButton = self.form.button
        QTest.mouseClick(processButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.outputArea.toPlainText(), "Data: TestCSV.csv processed!")

if __name__ == "__main__":
    unittest.main()