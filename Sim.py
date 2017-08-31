# -*- coding=utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from math import *

Dic = open('Dic.txt', 'r')
dic = []
line = 0
pie = 3.1415926535

for lines in Dic.xreadlines():
    ln = lines.decode('gbk')
    dic.append(ln)
    print ln
    line = line + 1
    pass
Dic.close()


def sim(wa, wb):
    a = ' ' + wa + ' '
    b = ' ' + wb + ' '
    tas = []
    tbs = []
    ret = []
    for lines in dic:
        if a in lines:
            tas.append(str(lines[0:8]))
        if b in lines:
            tbs.append(str(lines[0:8]))
    if tas == [] or tbs == []:
        print'can\'t find'
        return 0.0
    print tas, tbs

    def GetN():
        ts = ta1 + ta2 + ta3 + ta4
        for lines in dic:
            if ts in lines:
                n = float(lines[5:7])
        print n
        return n

    for ta in tas:
        for tb in tbs:
            ta1 = ta[0]
        tb1 = tb[0]
        ta2 = ta[1]
        tb2 = tb[1]
        ta3 = ta[2:4]
        tb3 = tb[2:4]
        ta4 = ta[4]
        tb4 = tb[4]
        ta5 = ta[5:7]
        tb5 = tb[5:7]
        ta6 = ta[7:8]
        tb6 = tb[7:8]
        if ta==tb:
            ret.append(1.0)
        elif not ta1 == tb1:
            print '1'
            ret.append(0.1)
        elif not ta2 == tb2:
            n = 14
            k = abs(ord(ta2) - ord(tb2))
            print n, k,'2'
            ret.append(0.65 * cos((n * pie / 180) * ((n - k + 1) / n)))
        elif not ta3 == tb3:
            n = 30
            k = abs(int(ta3) - int(tb3))
            print n, k,'3'
            ret.append(0.8 * cos((n * pie / 180) * ((n - k + 1) / n)))
        elif not ta4 == tb4:
            n = 10
            k = abs(ord(ta4) - ord(tb4))
            print n, k,'4'
            ret.append(0.9 * cos((n * pie / 180) * ((n - k + 1) / n)))
        elif not ta5 == tb5:
            n = GetN()
            k = abs(int(ta5) - int(tb5))
            print n,k,'5'
            print 0.96 * cos((n * pie / 180) * (n - k + 1) / n)
            ret.append(0.96 * cos((n * pie / 180) * ((n - k + 1) / n)))
        elif ta6 == '@' or tb6 == '@':
            ret.append(0.0)
        elif ta6 =='=='and tb6 == '==':
            print '='
            ret.append(1.0)
        elif ta6 == '#' or tb6 == '#':
            ret.append(0.5)
    print ret
    return max(ret)

print sim('计算', '计量')