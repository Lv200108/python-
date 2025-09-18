# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 08:44:30 2021

@author: wangh
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from sum import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
    
    def add(self):
        n1 = int(self.lineEdit.text())
        n2 = int(self.lineEdit_2.text())
        print(str(n1 + n2))
        self.lineEdit_3.setText(str(n1 + n2))
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())