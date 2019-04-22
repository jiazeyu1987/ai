#-*- coding:utf-8 -*-
'''
PushButton
'''
__author__ = 'Tony Zhu'

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(100,100,1300,860)

        self.layout = QHBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)


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
        self.layout.addWidget(f)
       # f.resize(self.width, self.height)

class PaintWidget(QWidget):

    def set_entity(self,entity):
        self.entity = entity

    def paintEvent(self, event):

        qp = QPainter(self)


        qp.setPen(Qt.black)
        size = self.size()

        for i in range(self.entity.shape[0]):
            for j in range(self.entity.shape[1]):
                qp.drawPoint(i, j)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_()) 