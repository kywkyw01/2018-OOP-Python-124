# pip3 install -U beautifulsoup4
# pip3 install -U requests
'''
https://github.com/kadragon/oop_python_ex/blob/master/student_result/04_parsing/parsing_29.py
'''
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

# 로그인이 필요한 사이트 파싱을 위한 정보 저장
LOGIN_INFO = {
    'id': '1731',
    'passwd': '10mybissasa!'
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


    SI= input().split()
    #get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/teacher?target='+teacher_name, data={'target': ''}).text
    get_timetable = s.get('https://go.sasa.hs.kr/timetable/search_new/student?target='+SI[0]+'-'+SI[1]+'%20'+SI[2]).text
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

    print(board)