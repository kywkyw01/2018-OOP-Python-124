import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("Hello World!")  # 상태 메시지

        menu = self.menuBar()
        menu_file = menu.addMenu('File')  # 상단 바에 File이라는 이름을 가진 메뉴 추가
        menu_edit = menu.addMenu('Edit')  # Edit 추가

        file_exit = QAction('Exit', self)  # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')  # 단축키
        file_exit.setStatusTip('Don\'t push')  # statusBar에 표시할 메시지
        file_new_txt = QAction('Txt File', self)  # 메뉴 객체 생성
        file_new_py = QAction('Python File', self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)  # Exit 메뉴 선택시 탭이 닫히도록. 단축키로도 가능!

        file_new = QMenu('New', self)  # File 메뉴 안에 New 라는 그룹 생성

        file_new.addAction(file_new_txt)  # New 메뉴 안에 Txt 파일이라는 메뉴 추가
        file_new.addAction(file_new_py)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)
        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())