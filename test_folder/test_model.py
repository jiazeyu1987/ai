import  data_model_folder as dmf
import tkinter
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
import time
import sys
from .QtMain import App
def test_model():
    app = QApplication(sys.argv)
    f = App()
    f.show()
    sys.exit(app.exec_())





