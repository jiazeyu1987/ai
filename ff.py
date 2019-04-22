#-*- coding:utf-8 -*-
'''
PushButton
'''
__author__ = 'Tony Zhu'

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
import sys

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(100,100,1300,860)

        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.jj)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(100,100)

    def jj(self):
        f = PaintWidget(self)
        f.move(200,200)
       # f.resize(self.width, self.height)

class PaintWidget(QWidget):
    def paintEvent(self, event):

        qp = QPainter(self)


        qp.setPen(Qt.black)
        size = self.size()

        for i in range(1024):
            x = i
            y = i
            qp.drawPoint(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_()) 