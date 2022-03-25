# -些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲
# 给你每一个项目开始的时间和结束的时间(给你一个数组，里面是一个个具体的项目)
# 你来安排宣讲的日程，要求会议室进行的宣讲的场次最多
# 返回这个最多的宣讲场次
from functools import cmp_to_key


class Program(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


def comparator(p1: Program, p2: Program):
    return p1.end - p2.end


def bestArrange(prolist: list, starttime: int) -> int:
    prolist = sorted(prolist, key=cmp_to_key(comparator))
    result = 0
    for p in prolist:
        if starttime <= p.start:
            result += 1
            starttime = p.end
    return result


if __name__ == '__main__':
    alist = [[6, 10], [6, 8], [7, 11], [9, 13], [10, 13], [12.5, 14]]
    plist = []
    for a in alist:
        temp = Program(a[0], a[1])
        plist.append(temp)
    print(bestArrange(plist, 6))
