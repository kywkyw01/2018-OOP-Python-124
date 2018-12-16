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





todaysc=sctable()
for i in todaysc.sctab:
    for j in i:
        print(j, end=" ")
    print("")

printsc=deepcopy(todaysc)



recenthw=[]
a=int(input())
for i in range(a):
    getschedule()

for i in recenthw:
    print(i.hwname, i.leadtime,'시간', i.deadline)

for i in recenthw:
    Flag=0
    for j in range(14):
        if Flag==1: break
        for k in range(7):
            if todaysc.sctab[j][k]=='empty':
                print(j, k)
                todaysc.sctab[j][k]=i.hwname
                i.leadtime-=1
                if i.leadtime==0:
                    Flag=1
                    break

for i in todaysc.sctab:
    for j in i:
        print(j, end=" ")
    print("")





