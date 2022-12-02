from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon

import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("dollar.jpg"))

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message",
                                     "Are you sure? You want quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)