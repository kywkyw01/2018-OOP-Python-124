# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time_table = QtWidgets.QTableWidget(self.centralwidget)
        self.time_table.setGeometry(QtCore.QRect(10, 120, 741, 501))
        self.time_table.setShowGrid(True)
        self.time_table.setGridStyle(QtCore.Qt.DashDotLine)
        self.time_table.setWordWrap(True)
        self.time_table.setCornerButtonEnabled(True)
        self.time_table.setRowCount(14)
        self.time_table.setColumnCount(7)
        self.time_table.setObjectName("time_table")
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.time_table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255, 150))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.time_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.time_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.time_table.setItem(0, 0, item)
        self.time_table.horizontalHeader().setVisible(True)
        self.time_table.horizontalHeader().setCascadingSectionResizes(True)
        self.time_table.horizontalHeader().setDefaultSectionSize(110)
        self.time_table.horizontalHeader().setMinimumSectionSize(60)
        self.time_table.verticalHeader().setDefaultSectionSize(80)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 281, 81))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 31, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(77, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(77, 50, 113, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(207, 20, 61, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(770, 120, 341, 501))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 321, 411))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 460, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 460, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 460, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_table.setSortingEnabled(False)
        item = self.time_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1교시"))
        item = self.time_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2교시"))
        item = self.time_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3교시"))
        item = self.time_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4교시"))
        item = self.time_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5교시"))
        item = self.time_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6교시"))
        item = self.time_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7교시"))
        item = self.time_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8교시"))
        item = self.time_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9교시"))
        item = self.time_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "1자-1"))
        item = self.time_table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "1자-2"))
        item = self.time_table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "2자-1"))
        item = self.time_table.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "2자-2"))
        item = self.time_table.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "연장 자습"))
        item = self.time_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "월"))
        item = self.time_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "화"))
        item = self.time_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "수"))
        item = self.time_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "목"))
        item = self.time_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "금"))
        item = self.time_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "토"))
        item = self.time_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "일"))
        __sortingEnabled = self.time_table.isSortingEnabled()
        self.time_table.setSortingEnabled(False)
        self.time_table.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "PW:"))
        self.pushButton_3.setText(_translate("MainWindow", "Sign In"))
        self.groupBox_2.setTitle(_translate("MainWindow", "To Do List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Check"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Assignment Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Deadline"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "dd"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

