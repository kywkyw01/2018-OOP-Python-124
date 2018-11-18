import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('click!', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('just click!<b>Hello<b/>')
        btn.move(20, 30)
        self.setGeometry(300, 0, 300, 300)
        self.setWindowTitle('First class')
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
