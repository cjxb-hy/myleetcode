# file head
# 多个字符串拼接拥有最小的字典序
from functools import cmp_to_key
from permute import permutation


def comparetor(s1, s2):
    return -1 if s1 + s2 < s2 + s1 else 1


def func(slist: list):
    if slist is None or len(slist) == 0:
        return ''
    inlist = sorted(slist, key=cmp_to_key(comparetor))
    result = ''
    for i in inlist:
        result += i
    return result


def violence(slist: list):
    if slist is None or len(slist) == 0:
        return ''
    minstring = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'
    rlist = permutation(slist, 0, len(slist), [])

    for r in rlist:
        tempstr = ''
        for s in r:
            tempstr += s
        if tempstr < minstring:
            minstring = tempstr
    return minstring


if __name__ == '__main__':
    stringlist = ['b', 'ba']
    print(func(stringlist))
    print(violence(stringlist))
