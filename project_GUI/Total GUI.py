# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

task_list = []

#계획 추가 창 표시
class InputProject(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 200)
        self.setWindowTitle("ADD Project")

        label1 = QLabel("Name: ")
        label2 = QLabel("Spend time: ")
        label3 = QLabel("Deadline: ")

        self.lineEdit1 = QLineEdit()
        self.mycom = QComboBox()
        self.endline = QDateEdit()

        self.pushButton1= QPushButton("ADD")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.mycom.addItems(["1교시","2교시","3교시","4교시","5교시","6교시","7교시","8교시","9교시","1자_1","1자_2","2자_1","2자_2","새벽"])

        self.endline.setDate(QDate.currentDate())
        self.endline.setCalendarPopup(True)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.mycom, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.endline, 2, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.name = self.lineEdit1.text()
        self.SpendTime = self.mycom.currentText()
        d_list = self.endline.date().toString().split(' ')
        self.deadline = [d_list[3], d_list[1], d_list[2]]
        self.close()


class MyTable(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()
        self.__make_layout()
        self.__make_table()

    def __make_table(self):
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(['', '이름', '시간', 'Deadline'])
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table.setColumnWidth(0, 10)


    def __make_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        grid = QGridLayout()
        vbox.addLayout(grid)
        add_button = QPushButton(" Add Schedule ")
        grid.addWidget(add_button, 0, 0)
        del_button = QPushButton(" Del Schedule ")
        grid.addWidget(del_button, 0, 1)
        self.setLayout(vbox)
        add_button.clicked.connect(self.__add_clicked)
        del_button.clicked.connect(self.__del_clicked)

    @pyqtSlot()
    def __add_clicked(self):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count+1)
        ckbox = QCheckBox()
        self.table.setCellWidget(row_count, 0, ckbox)

        add = InputProject()
        add.exec()
        self.table.setItem(row_count, 1, QTableWidgetItem(add.name))
        self.table.setItem(row_count, 2, QTableWidgetItem(add.SpendTime))
        self.table.setItem(row_count, 3, QTableWidgetItem(str(add.deadline[0]) + '년 ' + str(add.deadline[1]) + '월 ' + str(add.deadline[2]) + '일'))
        task_list.append([add.name, add.SpendTime, [int(add.deadline[0]), int(add.deadline[1]), int(add.deadline[2])]])
        # print(task_list)
        # print(self.table.item(0, 2).text()[0:2])
        return


    def __del_clicked(self):
        row_count = self.table.rowCount()
        chk_count = 0
        rem_list = []
        if row_count != 0:
            for idx in range(row_count):
                item = self.table.cellWidget(idx, 0)
                if item.isChecked():
                    rem_list.append(idx)
            if len(rem_list) != 0:
                rem_list.sort()
                rem_list.reverse()
                for idx in range(len(rem_list)):
                    self.table.removeRow(rem_list[idx])
                    chk_count += 1
        # print(rem_list)
        row_count = self.table.rowCount()
        if row_count and chk_count:
            global task_list
            task_list = []
            # print(self.table.item(0, 3).text()[8])
            for idx in range(row_count):
                if self.table.item(idx, 3).text()[7] == '월':
                    if self.table.item(idx, 3).text()[10] == '일':
                        task_list.append([self.table.item(idx, 1).text(), self.table.item(idx, 2).text(),
                                          [int(self.table.item(idx, 3).text()[0:4]), int(self.table.item(idx, 3).text()[6]),
                                           int(self.table.item(idx, 3).text()[9])]])
                    else:
                        task_list.append([self.table.item(idx, 1).text(), self.table.item(idx, 2).text(),
                                          [int(self.table.item(idx, 3).text()[0:4]), int(self.table.item(idx, 3).text()[6]),
                                           int(self.table.item(idx, 3).text()[9:11])]])
                else:
                    if self.table.item(idx, 3).text()[11] == '일':
                        task_list.append([self.table.item(idx, 1).text(), self.table.item(idx, 2).text(),
                                          [int(self.table.item(idx, 3).text()[0:4]),
                                           int(self.table.item(idx, 3).text()[6:8]),
                                           int(self.table.item(idx, 3).text()[10])]])
                    else:
                        task_list.append([self.table.item(idx, 1).text(), self.table.item(idx, 2).text(),
                                          [int(self.table.item(idx, 3).text()[0:4]),
                                           int(self.table.item(idx, 3).text()[6:8]),
                                           int(self.table.item(idx, 3).text()[10:12])]])



# 메인 윈도우
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1200, 600)
        self.setWindowTitle("SASA smart scheduler")

        self.title = QLabel()
        self.title.setText("SASA Smart Scheduler")
        self.title.setAlignment(Qt.AlignCenter)
        font_title = QtGui.QFont()
        font_title.setBold(True)
        font_title.setWeight(100)
        self.title.setFont(font_title)

        self.groupbox = QGroupBox("Project Board")

        self.table_widget =  QTableWidget(14,7)
        self.table_widget.setHorizontalHeaderLabels(["월","화","수","목","금","토","일"])
        self.table_widget.setVerticalHeaderLabels(["1교시","2교시","3교시","4교시","5교시","6교시","7교시","8교시","9교시","1자_1","1자_2","2자_1","2자_2","새벽"])
        # self.table_widget.resizeColumnsToContents()  # 아이템 길이에 맞춰서 크기 조정
        # self.table_widget.resizeRowsToContents()  # 아이템 길이에 맞춰서 크기 조정
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 표를 임의로 수정 불가하게 만듬

        table = MyTable()
        #레이아웃 설정부분(Groupbox)
        groupbox_layout = QVBoxLayout()
        groupbox_layout.addWidget(table)
        self.groupbox.setLayout(groupbox_layout)

        # 레이아웃 설정부분(왼쪽)
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.groupbox)

        #레이아웃 성정부분(오른쪽)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.table_widget)

        #레이아웃 설정부분(아래)
        under_layout = QHBoxLayout()
        under_layout.addLayout(left_layout)
        under_layout.addLayout(right_layout)
        under_layout.setStretchFactor(left_layout,1)
        under_layout.setStretchFactor(right_layout,4)

        total_layout = QVBoxLayout()
        total_layout.addWidget(self.title)
        total_layout.addLayout(under_layout)
        self.setLayout(total_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec()