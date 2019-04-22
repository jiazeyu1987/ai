import sys
from PyQt5.QtWidgets import *
from PyQt5 import  *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import  threading
import random
import  data_model_folder as dmf
import tkinter
import threading
import time
from .QtDelegate import QtDelegate1
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - pythonspot.com'
        self.left = 410
        self.top = 30
        self.width = 1100
        self.height = 1000
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('File')

        # 给menu创建一个Action
        exitAction = QAction(QIcon('exit.png'), 'Start', self)
        exitAction.setShortcut('s')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.timeStop)

        # 将这个Action添加到fileMenu上
        fileMenu.addAction(exitAction)



        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)



        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

        self.delegate = QtDelegate1()

        #workThread = WorkThread()
        #workThread.start()
        #workThread.trigger.connect(self.timeStop)

    def timeStop(self):
        entitys = self.delegate.entry()
        self.form_widget.draw_entitys(entitys)
        pass




class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QGridLayout(self)
        self.f = None
        self.button1 = QPushButton("Button 1")
        #self.layout.addWidget(self.f)
        self.button2 = QPushButton("Button 2")
        self.setLayout(self.layout)

        self.paint = PaintWidget()
        self.paint.init()
        self.layout.addWidget(self.paint,1,1)








    def draw_entitys(self,entitys):
        for i in entitys:
            start = time.time()
            self.paint.set_entity(i)
            self.paint.update()
            QApplication.processEvents()
            end = time.time()-start
            if(end<0.2):
                time.sleep(0.2-end)
        pass




    def test_triangle(self):
        e = dmf.get_empty_entity(100, 100)
        center_point = dmf.get_center_point(e)
        entity_triangle = dmf.draw_triangle(e, center_point, 3, 1, "left")
        list1 = dmf.step_move_to_point(entity_triangle, [1], (0, 0))
        self.draw_entitys(list1)

    def test_circle(self):
        e = dmf.get_empty_entity(100, 100)
        entity_circle = dmf.draw_circle(e, 1, 4)

        for i in range(12):
            dmf.enlarge(entity_circle, 1)
            new_entity = dmf.get_empty_entity(entity_circle.shape[0], entity_circle.shape[1])
            for i1 in range(entity_circle.shape[0]):
                for j in range(entity_circle.shape[1]):
                    new_entity[i1][j] = entity_circle[i1][j]

            self.paint.set_entity(new_entity)
            self.paint.update()
            QApplication.processEvents()


class GridPaint(QWidget,):
    def __int__(self, para1):
        QWidget.__init__(self, None)
        self.para1 = para1

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        qp.fillRect(0, 0, 10, 10, Qt.black)

class PaintWidget(QWidget):

    def init(self):
        self.entity = None
        self.colors = {}

    def set_entity(self,entity):
        self.entity = entity



    def paintEvent(self, event):
        if(self.entity is None):
            return

        qp = QPainter(self)
        qp.setPen(Qt.black)
        len1 = min(1000/self.entity.shape[0],1000/self.entity.shape[1])
        for i in range(self.entity.shape[0]):
            for j in range(self.entity.shape[1]):
                #if(self.entity[j][i]==0):
                    #qp.fillRect(i*len1,j*len1,len1,len1,self.get_color(self.entity[j][i]))
                #else:
                    color1 = Qt.black
                    if(self.entity[i][j] in self.colors):
                        color1 = self.colors[self.entity[i][j]]
                    else:
                        color1 = self.get_color(self.entity[j][i])
                        self.colors[self.entity[i][j]] = color1
                    qp.fillRect(j * len1, i * len1,len1,len1,color1)

        index=0
        font1 = QFont()
        font1.setPointSize(len1)
        font1.setBold(True)
        qp.setFont(font1)
        for i in self.colors:
            index+=1
            qp.fillRect(self.entity.shape[0] * len1+len1, index * len1*2, len1, len1, self.colors[i])
            qp.drawText(self.entity.shape[0] * len1+len1*3 ,index * len1*2.45,str(i))

    def get_color(self,val):
        if(val==11):
            return Qt.black
        elif(val==0):
            return Qt.white
        else:
            color1 = (qrand()*val)%255
            color2 = (qrand() * val) % 255
            color3 = (qrand() * val) % 255
            return QColor(color1,color2,color3)

class WorkThread(QThread):
    #实例化一个信号对象
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        #开始进行循环
        # for i in range(100):
        #     pass
        time.sleep(1)
        # 循环完毕后发出信号
        self.trigger.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())