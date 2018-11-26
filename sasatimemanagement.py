import datetime

class sctable:
    def __init__(self, sctab = ''):
        self.sctab=[['empty' for j in range(7)] for i in range(14)]

class hwtable:
    def __init__(self, hwname, leadtime, deadline):
        self.hwname=hwname
        self.deadline=deadline
        self.leadtime=leadtime

def getschedule ():
    buff=[*map(int, input().split())]
    recenthw.append(hwtable(buff[0], buff[1], [buff[2], buff[3], buff[4]]))
    hwsort(recenthw)

def hwsort(alist):
    for A in range(len(alist)-1):
        for B in range(len(alist)-1-A):
            if alist[A].deadline>alist[A+1].deadline:
                alist[A],alist[A+1]=alist[A+1],alist[A]

todaysc=sctable()
for i in todaysc.sctab:
    for j in i:
        print(j, end=" ")
    print("")
tomorrow=sctable()

recenthw=[]
a=int(input())
for i in range(a):
    getschedule()

for i in recenthw:
    print(i.deadline, i.leadtime)






