# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library
import datetime
from copy import deepcopy


class sctable:
    def __init__(self, sctab = ''):
        self.sctab=[['empty' for j in range(7)] for i in range(14)]

class hwtable:
    def __init__(self, hwname, leadtime, deadline):
        self.hwname=hwname
        self.deadline=deadline
        self.leadtime=leadtime

def getschedule ():
    buff=input().split()
    rtm=datetime.datetime.now() #현재 시각
    nowdate=datetime.date(rtm.year, rtm.month, rtm.day)
    recentdate=datetime.date(int(buff[2]), int(buff[3]), int(buff[4]))
    delta=recentdate-nowdate
    if delta.days<0:
        print("이미 마감된 과제입니다")
        return
    if 14-rtm.weekday()<delta.days:
        print("너무 먼 미래입니다")
        return
    recenthw.append(hwtable(buff[0], int(buff[1]), [int(buff[2]), int(buff[3]), int(buff[4])])) # 2:년 3:월 4:일
    hwsort(recenthw)

def hwsort(alist):
    for A in range(len(alist)-1):
        for B in range(len(alist)-1-A):
            if alist[B].deadline[0]==alist[B+1].deadline[0] and alist[B].deadline[1]==alist[B+1].deadline[1]:
                if alist[B].deadline[2]>alist[B+1].deadline[2]:
                    alist[B], alist[B+1]=alist[B+1], alist[B]
            elif alist[B].deadline[0]==alist[B+1].deadline[0]:
                if alist[B].deadline[1]>alist[B+1].deadline[1]:
                    alist[B], alist[B+1] = alist[B+1], alist[B]
            else:
                if alist[B].deadline[0]>alist[B+1].deadline[1]:
                    alist[B], alist[B+1]= alist[B+1], alist[B]


todaysc=sctable() #고정테이블
printsc=sctable() #유동테이블
#배열접근: printsc.sctab[i][j]

task_list = []

# 0번째 index에 이름
# 1번째 index에 시간
# 2번째 index에 과제 마감
# 3번째 index에 요일
task1_list = []

ProfileData = {
    'id': '',
    'password': ''
}  # 유저 데이터 담고있는 딕셔너리
LOGIN_INFO = {
    'id': '',
    'passwd': ''
}


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def deco_classroom(classroom_number):
    classroom_number = classroom_number
    def give_class():
        find_classroom(classroom_number)
    return give_class



def Right(User_id, User_pw):         # 구현해주세요!! 달빛학사 아이디 비번 확인함수
    with requests.Session() as s:
        # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
        LOGIN_INFO = {
            'id': User_id,
            'passwd': User_pw
        }
        print(LOGIN_INFO)
        first_page = s.get('https://go.sasa.hs.kr')
        html = first_page.text
        soup = bs(html, 'html.parser')

        # cross-site request forgery 방지용 input value 를 가져온다.
        # https://ko.wikipedia.org/wiki/사이트_간_요청_위조
        csrf = soup.find('input', {'name': 'csrf_test_name'})

        # 두개의 dictionary 를 합친다.
        LOGIN_INFO.update({'csrf_test_name': csrf['value']})

        # 만들어진 로그인 데이터를 이용해서, 로그인을 시도한다.
        login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
        print("A")
        if login_req.status_code != 200:
            return 0
        else:
            SI = input().split()
            # get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/teacher?target='+teacher_name, data={'target': ''}).text
            get_timetable = s.get(
                'https://go.sasa.hs.kr/timetable/search_new/student?target=' + SI[0] + '-' + SI[1] + '%20' + SI[2]).text
            timetable_soup = bs(get_timetable, 'html.parser')
            tmp = timetable_soup.select('script')
            tmp = str(tmp).split('\n')
            tmp = list(tmp)
            tmp2 = []
            tmp3 = []
            board = [['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''],
                     ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''],
                     ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '']]
            for i in tmp:
                if "tar = " in i:
                    tmp2.append(i)
                if "$('#time" in i:
                    tmp2.append(i)

            for i in tmp2:
                if "tar = " in i:
                    i = i.split('"')[1].replace("<br />", " / ").split(" / ")[0:3]
                    tmp3.append(i)
                if "$('#time" in i:
                    if "append(tar)" in i:
                        i = i.split("'")[1].replace("#time", "").split("-")
                        tmp3.extend(i)
                    else:
                        i = i.split("'")[4:0:-3]
                        i[0] = i[0].replace(">", "").replace('</button");', "")
                        pre_i = i[1].replace("#time", "").split("-")
                        i[1] = pre_i[0]
                        i.append(pre_i[1])
                        tmp3.extend(i)
            for i in range(0, len(tmp3), 3):
                board[int(tmp3[i + 1]) - 1][int(tmp3[i + 2]) - 1] = tmp3[i]

            for i in range(12):
                for j in range(6):
                    if board[j][i] != '': todaysc.sctab[i][j] = board[j][i][0]
            printsc=deepcopy(todaysc)
            print(printsc.sctab)
        return [1, printsc.sctab]

#시작전에 login logout
def DataAbsence(exist):     #exist==1 로그인 절차 x     exist==0 로그인 절차 필요
    if exist == 1:
        app = QApplication(sys.argv)
        mywindow = MyWindow()
        mywindow.show()
        app.exec()

    else:
        global ProfileData
        Login = True
        while Login:
            ap = QApplication(sys.argv)
            window= SignIn()
            window.show()
            ap.exec()
            flag = Right(ProfileData['id'],ProfileData['password']) #아이디 비번이 맞는지 확인 맞으면 1 틀리면 0
            if flag[0]:
                Login = False

            else:
                print("Q")
                Login = True
                ProfileData = {
                    'id': '',
                    'password': ''
                }

        app = QApplication(sys.argv)
        mywindow = MyWindow(flag[1])
        mywindow.show()
        app.exec()



class SignIn(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200,300,100)
        self.setWindowTitle("Sign_In")

        self.ID = QLabel("ID :")
        self.PW = QLabel("PW :")
        self.ID_input = QLineEdit()
        self.PW_input = QLineEdit()
        self.SignIn = QPushButton("SignIn")

        self.SignIn.clicked.connect(self.SignInClicked)

        layout = QGridLayout()
        layout.addWidget(self.ID, 0,0)
        layout.addWidget(self.PW, 1,0)
        layout.addWidget(self.ID_input, 0,1)
        layout.addWidget(self.PW_input ,1,1)
        layout.addWidget(self.SignIn , 2, 0)
        self.setLayout(layout)

    def SignInClicked(self):
        self.ID_data = self.ID_input.text()
        self.PW_data = self.PW_input.text()
        ProfileData['id']=self.ID_data
        ProfileData['password']=self.PW_data
        self.close()

#계획 추가 창 표시
class InputProject1(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 200)
        self.setWindowTitle("ADD Project")

        label1 = QLabel("Name: ")
        label2 = QLabel("Spend time: ")
        label3 = QLabel("Deadline 또는 일자: ")
        label4 = QLabel("(필수라면) 몇교시? :")

        self.lineEdit1 = QLineEdit()
        self.mycom = QComboBox()
        self.endline = QDateEdit()
        self.period = QComboBox()

        self.pushButton1= QPushButton("ADD")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        #self.mycom.addItems(["1교시","2교시","3교시","4교시","5교시","6교시","7교시","8교시","9교시","1자_1","1자_2","2자_1","2자_2","새벽"])
        self.mycom.addItems(["1시간","2시간","3시간","4시간"])
        self.period.addItems(["필수 아님", "1교시","2교시","3교시","4교시","5교시","6교시","7교시","8교시","9교시","1자_1","1자_2","2자_1","2자_2","새벽"])
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
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.period, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.name = self.lineEdit1.text()
        self.SpendTime = int(self.mycom.currentText().replace("시간", ""))
        d_list = self.endline.date().toString().split(' ')
        self.deadline = [d_list[3], d_list[1], d_list[2]]
        self.day = self.endline.date().dayOfWeek()  # 월요일을 1로 기준하여 요일을 숫자로 return
        if self.period.currentText() == '필수 아님':
            self.per = -1
        else:
            self.per = int(self.period.currentText().replace("교시",""))-1
        self.close()

    def closeEvent(self, QCloseEvent):
        '''
        추후 작업 통해 그냥 close하면 버그 발생하는 오류 수정할 것
        :param QCloseEvent: 
        :return:
        '''
        self.close()



class MyTable(QWidget):
    def __init__(self, table_widget):
        super().__init__()
        self.table = QTableWidget()
        self.table_widget = table_widget
        self.__make_layout()
        self.__make_table()

    def __make_table(self):
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(['삭제?', '시간표로', '이름', '시간', 'Deadline', '요일', '교시'])
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
        to_schedule = QPushButton(" Make Table ")
        grid.addWidget(to_schedule, 0, 2)
        self.setLayout(vbox)
        add_button.clicked.connect(self.__add_clicked)
        del_button.clicked.connect(self.__del_clicked)
        to_schedule.clicked.connect(self.__make_clicked)

    @pyqtSlot()
    def __add_clicked(self):
        add = InputProject1()
        add.exec_()
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        ckbox1 = QCheckBox()
        totablebutton = QPushButton()
        self.table.setCellWidget(row_count, 0, ckbox1)
        self.table.setCellWidget(row_count, 1, totablebutton)
        totablebutton.clicked.connect(self.__to_table)
        self.table.setItem(row_count, 2, QTableWidgetItem(add.name))
        self.table.setItem(row_count, 3, QTableWidgetItem(add.SpendTime))
        self.table.setItem(row_count, 4, QTableWidgetItem(
            str(add.deadline[0]) + '년 ' + str(add.deadline[1]) + '월 ' + str(add.deadline[2]) + '일'))
        rtm = datetime.datetime.now()  # 현재 시각
        nowdate = datetime.date(rtm.year, rtm.month, rtm.day)
        recentdate = datetime.date(int(add.deadline[0]), int(add.deadline[1]), int(add.deadline[2]))
        delta = recentdate - nowdate
        print(delta.days)
        if delta.days < 0:
            print("이미 마감된 과제입니다")
            self.table.removeRow(row_count)
            return
        if  delta.days >= 7:
            print("너무 먼 미래입니다")
            self.table.removeRow(row_count)
            return
        task_list.append(
            [add.name, add.SpendTime, [int(add.deadline[0]), int(add.deadline[1]), int(add.deadline[2])], add.day, add.per])


        # print(task_list)
        # print(self.table.item(0, 2).text()[0:2])
        return

    def __to_table(self, row_count):
        self.table_widget.setItem(task_list[row_count][4], task_list[row_count][3] - 1, QTableWidgetItem(task_list[row_count][0]))
        printsc.sctab[task_list[row_count][4]][task_list[row_count][3]-1] = task_list[row_count][0]
        self.table.removeRow(row_count)
        del task_list[row_count]

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
                if self.table.item(idx, 4).text()[7] == '월':
                    if self.table.item(idx, 4).text()[10] == '일':
                        task_list.append([self.table.item(idx, 2).text(), self.table.item(idx, 3).text(),
                                          [int(self.table.item(idx, 4).text()[0:4]), int(self.table.item(idx, 4).text()[6]),
                                           int(self.table.item(idx, 4).text()[9])]])
                    else:
                        task_list.append([self.table.item(idx, 2).text(), self.table.item(idx, 3).text(),
                                          [int(self.table.item(idx, 4).text()[0:4]), int(self.table.item(idx, 4).text()[6]),
                                           int(self.table.item(idx, 4).text()[9:11])]])
                else:
                    if self.table.item(idx, 4).text()[11] == '일':
                        task_list.append([self.table.item(idx, 2).text(), self.table.item(idx, 3).text(),
                                          [int(self.table.item(idx, 4).text()[0:4]),
                                           int(self.table.item(idx, 4).text()[6:8]),
                                           int(self.table.item(idx, 4).text()[10])]])
                    else:
                        task_list.append([self.table.item(idx, 2).text(), self.table.item(idx, 3).text(),
                                          [int(self.table.item(idx, 4).text()[0:4]),
                                           int(self.table.item(idx, 4).text()[6:8]),
                                           int(self.table.item(idx, 4).text()[10:12])]])
        else:
            pass
            # "체크를 한 뒤 버튼을 클릭해주세요!" 메시지 출력해야 함

    def __make_clicked(self):
        autoschedule()
        print(printsc.sctab)
        for i in range(14):
            for j in range(7):
                item = printsc.sctab[i][j]
                if item == 'empty':
                    pass
                else:
                    self.table_widget.setItem(i, j, QTableWidgetItem(item))
        task_list = []
        row_count = self.table.rowCount()
        for i in range(row_count-1, -1, -1):
            self.table.removeRow(i)



# 메인 윈도우
class MyWindow(QWidget):
    def __init__(self, table):
        self.table = table

        super().__init__()
        self.setupUI()
        self.update_table()

    def setupUI(self):
        self.setGeometry(0, 0, 1300, 700)
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

        table = MyTable(self.table_widget)

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

    def update_table(self):
        for idx in range(7):
            for day in range(14):
                item = self.table[day][idx]
                if item == 'empty':
                    pass
                else:
                    self.table_widget.setItem(day, idx, QTableWidgetItem(item))
                    printsc.sctab[day][idx] = item



def autoschedule():
    print("AFEF")
    rtm=datetime.datetime.now()
    nowdate=datetime.date(rtm.year, rtm.month, rtm.day)
    s=rtm.weekday()
    for i in task_list:
        print(i)
        Flag = 0
        for j in range(s+1,s+8):
            if Flag == 1: break
            for k in range(14):
                if printsc.sctab[k][j%7] == 'empty':
                    print(i[0])
                    printsc.sctab[k][j%7] = i[0]
                    i[1] -= 1
                    if i[1] == 0:
                        Flag = 1
                        break
        print(printsc.sctab)
    return

if __name__ == "__main__":
    exist = 0
    DataAbsence(exist)