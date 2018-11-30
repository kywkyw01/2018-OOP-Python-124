import sys
from PyQt5.QtWidgets import *

project_list = []

def AddProjectList(name,spend_time,deadline):
    project_list.append([name,spend_time,deadline])


#계획 추가 창 표시
class InputProject(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.name = None
        self.SpendTime = None
        self.deadline = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 200)
        self.setWindowTitle("ADD Project")

        label1 = QLabel("Name: ")
        label2 = QLabel("Spend time: ")
        label3 = QLabel("Deadline: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()

        self.pushButton1= QPushButton("ADD")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.name = self.lineEdit1.text()
        self.SpendTime = self.lineEdit2.text()
        self.deadline = self.lineEdit3.text()
        self.close()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(0  , 0 ,1500 ,900)
        self.setWindowTitle("SASA smart scheduler")

        self.groupbox = QGroupBox("Project Board")
        self.add_label = QLabel()
        self.add_button = QPushButton("ADD Project")
        self.del_button = QPushButton("DEL Project")



        self.table_widget =  QTableWidget(14,7)
        self.table_widget.setHorizontalHeaderLabels(["월","화","수","목","금","토","일"])
        self.table_widget.setVerticalHeaderLabels(["1교시","2교시","3교시","4교시","5교시","6교시","7교시","8교시","9교시","1자_1","1자_2","2자_1","2자_2","새벽"])
#       self.table_widget.resizeColumnsToContents()  #아이템 길이에 맞춰서 크기 조정
#       self.table_widget.resizeRowsToContents()  #아이템 길이에 맞춰서 크기 조정
        self.table_widget.resize(3000,1000)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)  #표를 임의로 수정 불가하게 만듬



        #레이아웃 설정부분(Groupbox)
        groupbox_layout = QVBoxLayout()
        groupbox_layout.addWidget(self.add_label)
        groupbox_layout.addWidget(self.add_button)
        groupbox_layout.addWidget(self.del_button)
        self.groupbox.setLayout(groupbox_layout)


        # 레이아웃 설정부분(왼쪽)
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.groupbox)


        #레이아웃 성정부분(오른쪽)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.table_widget)

        #레이아웃 설정부분(전체)
        total_layout = QHBoxLayout()
        total_layout.addLayout(left_layout)
        total_layout.addLayout(right_layout)
        total_layout.setStretchFactor(left_layout,1)
        total_layout.setStretchFactor(right_layout,4)


        self.setLayout(total_layout)

        #기능
        self.add_button.clicked.connect(self.AddButtonClicked)

    def AddButtonClicked(self):
        add = InputProject()
        add.exec_()
        name = add.name
        spendtime = add.SpendTime
        deadline = add.deadline

        AddProjectList(name,spendtime,deadline)
        T = self.add_label.text()
        self.add_label.setText(T+ "Name: %s || Spend Time: %s || Deadline: %s \n"%(name,spendtime,deadline))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()