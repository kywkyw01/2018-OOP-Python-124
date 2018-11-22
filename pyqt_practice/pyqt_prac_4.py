# 출처 : https://www.youtube.com/watch?v=OIe77wIGZXY&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&index=4

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.statusBar()
        self.statusBar().showMessage("Hello World!")  # 상태 메시지

        menu = self.menuBar()
        menu_file = menu.addMenu('File')  # 상단 바에 File이라는 이름을 가진 메뉴 추가
        menu_edit = menu.addMenu('Edit')  # Edit 추가
        menu_view = menu.addMenu('View')

        file_exit = QAction('Exit', self)  # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')  # 단축키
        file_exit.setStatusTip('Don\'t push')  # statusBar에 표시할 메시지
        file_new_txt = QAction('Txt File', self)  # 메뉴 객체 생성
        file_new_py = QAction('Python File', self)
        view_stat = QAction('Status Bar', self, checkable = True)  # view 메뉴에 status bar라는 메뉴 객체 생성(체크박스)

        file_exit.triggered.connect(QCoreApplication.instance().quit)  # Exit 메뉴 선택시 탭이 닫히도록. 단축키로도 가능!
        # file_exit.triggered.connect(qApp.quit) 으로도 실행됨.
        view_stat.triggered.connect(self.tgleStat)


        file_new = QMenu('New', self)  # File 메뉴 안에 New 라는 그룹 생성

        file_new.addAction(file_new_txt)  # New 메뉴 안에 Txt 파일이라는 메뉴 추가
        file_new.addAction(file_new_py)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)
        menu_view.addAction(view_stat)

        self.resize(450, 400)
        self.show()

    def tgleStat(self, state) :
        if state :
            self.statusBar().show()
        else :
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent) :
        cm = QMenu(self)

        quit_code = cm.addAction("Quit")

        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))  # 전체적인 Map의 위치를 저장해서 넘긴다.
        if action :
            qApp.quit()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())