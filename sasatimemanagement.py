import datetime

class sctable:
    def __init__(self, sctab = ''):
        self.sctab=[['empty' for j in range(7)] for i in range(14)]

todaysc=sctable()
todaysc.sctab[0][5]=1
for i in todaysc.sctab:
    for j in i:
        print(j, end=" ")
    print("")
tomorrow=sctable()