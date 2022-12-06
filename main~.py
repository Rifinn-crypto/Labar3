from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDesktopWidget, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import os
import sys
from typing import Union
import datetime
import numpy
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

from get import tuple_for_next_data

file = "C:/Users/esh20/Desktop/dataset.csv"

def get_data(input_file: str, date: datetime.date) -> Union[numpy.float64, None]:
    if os.path.exists(input_file):
        df = pd.read_csv(input_file)
        df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
        df["Day"] = df["Day"].dt.date
        for i in range(0, df.shape[0], 1):
            if str(df["Day"].iloc[i]).replace("-", "") == str(date).replace("-", ""):
                return df.iloc[i]["Exchange rate"]
        return None
    raise FileNotFoundError


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):
        """
        The location of the button and the search bar.
        Application icon design
        """
        self.lbl = QLabel(self)
        self.resize(150, 150)
        self.center()
        butt = QPushButton("button 1", self)
        butt.move(30, 50)
        self.qle = QLineEdit(self)
        self.qle.move(35, 100)
        butt.setText("Получить")
        butt.clicked.connect(self.handleButton)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("dollar.jpg"))


    def handleButton(self):
        """
        Search str
        """
        self.lbl.setText("")
        self.lbl.adjustSize()
        lst = self.qle.text()
        lst = lst.split('-')
        if len(lst) == 3 and lst[2] != "":
            data = get_data(file, datetime.date(int(lst[0]), int(lst[1]), int(lst[2])))
            if data != None:
                self.lbl.setText(str(data))
                self.lbl.adjustSize()



    def closeEvent(self, event):
        """
        Request to exit the program
        param event:
        """

        reply = QMessageBox.question(self, "Message",
                                     "Are you sure? You want quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def center(self):
        """
        centering
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
