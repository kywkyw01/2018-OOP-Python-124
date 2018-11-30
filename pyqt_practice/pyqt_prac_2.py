# 출처 : https://www.youtube.com/watch?v=3k2QPRoJqoI&index=2&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("push me!", self)
        btn.resize(btn.sizeHint())  # sizeHint : 글씨를 기준으로 적당히 크기를 조절
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit)  # <Click>이라는 Method와 탭을 닫는 함수를 Connect
        self.resize(500, 500)
        self.setWindowTitle("second")
        self.show()
    def closeEvent(self, QCloseEvent):
        print('tab closed')  # 탭 닫기 시도시에 'tab closed'라는 메시지 출력
        ans = QMessageBox.question(self, 'Quit.', 'Quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)  # 종료 키를 눌렀을 때 재확인 창 출력. Yes 선택시 ans == QMessageBox.Yes
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())