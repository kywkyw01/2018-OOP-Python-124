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
        MainWindow.resize(1125, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time_table = QtWidgets.QTableWidget(self.centralwidget)
        self.time_table.setGeometry(QtCore.QRect(10, 10, 981, 561))
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
        self.time_table.horizontalHeader().setDefaultSectionSize(125)
        self.time_table.horizontalHeader().setMinimumSectionSize(60)
        self.time_table.verticalHeader().setDefaultSectionSize(80)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.time_table.scrollToTop)
        self.pushButton_2.clicked.connect(self.time_table.scrollToBottom)
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
        self.pushButton.setText(_translate("MainWindow", "Top"))
        self.pushButton_2.setText(_translate("MainWindow", "Bottom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

