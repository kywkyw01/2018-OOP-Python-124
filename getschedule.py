# pip3 install -U beautifulsoup4
# pip3 install -U requests
'''
https://github.com/kadragon/oop_python_ex/blob/master/student_result/04_parsing/parsing_29.py
'''
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library
import tkinter

# 로그인이 필요한 사이트 파싱을 위한 정보 저장
LOGIN_INFO = {
    'id': '1731',
    'passwd': '1mybissasa!'
}

def find_classroom(cl_num):
    with requests.Session() as s:
        # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
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
        get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/placement?target='+cl_num, data={'target': ''}).text
        timetable_soup = bs(get_timetable, 'html.parser')
        qmp = timetable_soup.select('script')
        qmp = str(qmp).split('\n')
        qmp = list(qmp)
        qmp2 = []
        qmp3 = []
        qoard = [['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','','']]
        for i in qmp:
            if "tar = " in i:
                qmp2.append(i)
            if "$('#time" in i:
                qmp2.append(i)

        for i in qmp2:
            if "tar = " in i:
                i = i.split('"')[1].replace("<br />"," / ").split(" / ")[0:3]
                qmp3.append(i)
            if "$('#time" in i:
                if "append(tar)" in i:
                    i = i.split("'")[1].replace("#time","").split("-")
                    qmp3.extend(i)
                else:
                    i = i.split("'")[4:0:-3]
                    i[0] = i[0].replace(">","").replace('</button");',"")
                    qre_i = i[1].replace("#time", "").split("-")
                    i[1] = qre_i[0]
                    i.append(qre_i[1])
                    qmp3.extend(i)
        for i in range(0, len(qmp3), 3):
            qoard[int(qmp3[i+1])-1][int(qmp3[i+2])-1] = qmp3[i]
        draw_board(qoard)


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

def draw_board(board):
    window = tkinter.Tk()
    window.title("Time_Table")
    window.geometry("1285x673+100+10")
    window.resizable(False, False)

    for j in range(0, 12):
        for i in range(0, 6):
            if i == 0 and j == 0:
                t = tkinter.Button(window, text="시간표",height=3, width=10)
            elif i == 0:
                t = tkinter.Button(window, text="%d교시" % j,height=3, width=10)
            elif j == 0:
                if i == 1:
                    t = tkinter.Button(window, text="월요일",height=3, width=33)
                elif i == 2:
                    t = tkinter.Button(window, text="화요일",height=3, width=33)
                elif i == 3:
                    t = tkinter.Button(window, text="수요일",height=3, width=33)
                elif i == 4:
                    t = tkinter.Button(window, text="목요일",height=3, width=33)
                elif i == 5:
                    t = tkinter.Button(window, text="금요일",height=3, width=33)
            else:
                if type(board[i-1][j-1]) == list:
                    classroom = deco_classroom(board[i-1][j-1][2])
                    t = tkinter.Button(window, text="%s\n%s  %s" % (board[i - 1][j - 1][0], board[i - 1][j - 1][1], board[i - 1][j - 1][2]), height=3, width=33, command = classroom)
                elif board[i-1][j-1] == "":
                    t = tkinter.Button(window, text="%s" % board[i - 1][j - 1], height=3, width=33)
                else:
                    t = tkinter.Button(window, text="%s" % board[i - 1][j - 1], height=3, width=33, fg = "blue", bg = "skyblue")
            t.grid(row=j, column=i)

    window.mainloop()


# 로그인을 유지하는건 session 이라는 기술 | 이를 활용하기 위해서 with 를 사용한다.
with requests.Session() as s:
    # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
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

    sub_html = get_html('https://go.sasa.hs.kr/timetable/search_new')  # get_html() 을 이용해서, 대상 기사에 접속 html tag 를 가져온다.
    sub_soup = bs(sub_html, 'html.parser')  # bs4 parser 를 이용하여, 뽑아오기 쉽게 parsing 한다.

    sch_link = sub_soup.select('div.box')

    print(sch_link)

    teacher_name= input()
    get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/teacher?target='+teacher_name, data={'target': ''}).text
    #get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/student?target=2-5%20방준형').text
    timetable_soup = bs(get_timetable, 'html.parser')
    tmp = timetable_soup.select('script')
    tmp = str(tmp).split('\n')
    tmp = list(tmp)
    tmp2 = []
    tmp3 = []
    board = [['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','',''],['','','','','','','','','','','','']]
    for i in tmp:
        if "tar = " in i:
            tmp2.append(i)
        if "$('#time" in i:
            tmp2.append(i)

    for i in tmp2:
        if "tar = " in i:
            i = i.split('"')[1].replace("<br />"," / ").split(" / ")[0:3]
            tmp3.append(i)
        if "$('#time" in i:
            if "append(tar)" in i:
                i = i.split("'")[1].replace("#time","").split("-")
                tmp3.extend(i)
            else:
                i = i.split("'")[4:0:-3]
                i[0] = i[0].replace(">","").replace('</button");',"")
                pre_i = i[1].replace("#time","").split("-")
                i[1] = pre_i[0]
                i.append(pre_i[1])
                tmp3.extend(i)
    for i in range(0, len(tmp3), 3):
        board[int(tmp3[i+1])-1][int(tmp3[i+2])-1] = tmp3[i]

    draw_board(board)