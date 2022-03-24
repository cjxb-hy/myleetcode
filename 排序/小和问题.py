# 小和问题

"""
描述
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
例子
[1,3,4,2,5]
1左边比1小的数：没有
3左边比3小的数：1
4左边比4小的数：1,3
2左边比2小的数：1
5左边比5小的数：1,3,4,2
所以小和为1+1+3+1+1+3+4+2=16
"""


def mergesort(arr, L, R):
    if L == R:
        return 0

    mid = L + ((R - L) >> 1)
    s1 = mergesort(arr, L, mid)
    s2 = mergesort(arr, mid + 1, R)
    s3 = merge(arr, L, mid, R)
    return s1 + s2 + s3


def merge(arr, L, M, R):
    harr = []
    ssum = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] < arr[p2]:
            ssum += (R - p2 + 1) * arr[p1]
            harr.append(arr[p1])
            p1 += 1
        else:
            harr.append(arr[p2])
            p2 += 1

    while p1 <= M:
        harr.append(arr[p1])
        p1 += 1

    while p2 <= R:
        harr.append(arr[p2])
        p2 += 1

    for i in range(len(harr)):
        arr[L + i] = harr[i]
    return ssum


# 逆序对

"""
在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对
"""


def mergesort(arr, L, R):
    if L == R:
        return 0

    mid = L + ((R - L) >> 1)
    s1 = mergesort(arr, L, mid)
    s2 = mergesort(arr, mid + 1, R)
    s3 = merge(arr, L, mid, R)
    return s1 + s2 + s3


def merge(arr, L, M, R):
    harr = []
    ssum = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] < arr[p2]:
            # ssum +=  (R - p2 + 1) * arr[p1]
            harr.append(arr[p1])
            p1 += 1
        else:
            ssum += (M - p1 + 1)
            harr.append(arr[p2])
            p2 += 1

    while p1 <= M:
        harr.append(arr[p1])
        p1 += 1

    while p2 <= R:
        harr.append(arr[p2])
        p2 += 1

    for i in range(len(harr)):
        arr[L + i] = harr[i]
    return ssum
