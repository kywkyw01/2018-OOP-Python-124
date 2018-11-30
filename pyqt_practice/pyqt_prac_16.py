from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, cv2, numpy, time

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cam_exam")
        self.setGeometry(150, 150, 650, 540)
        self.initUI()
    def initUI(self):
        self.cpt = cv2.VideoCapture(0)
        self.fps = 24
        self.sens = 300
        _, self.img_o = self.cpt.read()
        self.img_o = cv2.cvtColor(self.img_o, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('img_o.jpg', self.img_o)

        self.cnt = 0
        self.prt = QLabel(self)
        self.prt.resize(200, 25)
        self.prt.move(5+105+105, 490)

        self.sldr = QSlider(Qt.Horizontal, self)
        self.sldr.resize(100, 25)
        self.sldr.move(5+105+105+200, 490)
        self.sldr.setMinimum(1)
        self.sldr.setMaximum(30)
        self.sldr.setValue(24)
        self.sldr.valueChanged.connect(self.setFps)
        self.show()

    def setFps(self):
        self.fps = self.sldr.value()
        self.prt.setText("FPS "+str(self.fps)+"(으)로 조정!")
        self.timer.stop()
        self.timer.start(1000. / self.fps)

    def setSens(self):
        self.sens = self.sldr1.value()
        self.prt.setText("감도 "+str(self.sens)+"(으)로 조정!")

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000. / self.fps)

    def nextFrameSlot(self):
        _, cam = self.cpt.read()
        cam = cv2.cvtColor(cam, cv2.COLOR_RGB2GRAY)

