import random
import time

"""
选择排序 O(N^2)   O(1)    不稳定
冒泡排序 O(N^2)   O(1)    稳定
插入排序 O(N^2)   O(1)    稳定
归并排序 O(NlogN) O(N)    稳定
快速排序 O(NlogN) O(logN) 不稳定
堆排序   O(NlogN) O(1)    不稳定
"""

"""
常见的坑
1. 归并排序的额外空间复杂度可以变成0(1)，但是非常难，不需要掌握，“归并排序 内部缓存法”
2. “原地归并排序”的帖子都是垃圾，会让归并排序的时间复杂度变成0(N^2)
3. 快速排序可以做到稳定性问题，但是非常难，不需要掌握，“01 stable sort”
4. 所有的改进都不重要，因为目前没有找到时间复杂度O(N*logN)，额外空间复杂度O(1)，又稳定的排序
5. 题目：奇数放在数组左边，偶数放在数组右边，还要求原始的相对次序不变，碰到这个问题，可以怼面试官
"""


# 选择排序 O(N^2) O(1)   不稳定
def swapsort(arr):
    for i in range(len(arr)):
        indexmin = i
        for j in range(i, len(arr)):
            if arr[j] < arr[indexmin]:
                indexmin = j
        if indexmin != i:
            arr[i], arr[indexmin] = swap(arr[i], arr[indexmin])

    return arr


# 冒泡排序 O(N^2) O(1)   稳定
def bubblesort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])
                flag = False
        if flag:
            break

    return arr


# 插入排序 O(N^2) O(1)   稳定
def insertsort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])
            else:
                break
    return arr


# 归并排序 O(NlogN) O(N)  稳定
def mergesort(arr, L, R):
    if L == R:
        return

    mid = L + ((R - L) >> 1)
    mergesort(arr, L, mid)
    mergesort(arr, mid + 1, R)
    return merge(arr, L, mid, R)


def merge(arr, L, M, R):
    harr = []

    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] <= arr[p2]:
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
    return arr


# 快速排序 O(NlogN) O(logN)  不稳定
def quicksort(arr, L, R):
    if L < R:
        rnum = L + int(random.random() * (R - L + 1))
        arr[rnum], arr[R] = swap(arr[rnum], arr[R])
        p = partition(arr, L, R)
        quicksort(arr, L, p[0] - 1)
        quicksort(arr, p[1] + 1, R)
    return arr


def partition(arr, L, R):
    left = L - 1
    right = R
    while L < right:
        if arr[L] < arr[R]:
            left += 1
            arr[left], arr[L] = swap(arr[left], arr[L])
            L += 1
        elif arr[L] > arr[R]:
            right -= 1
            arr[L], arr[right] = swap(arr[L], arr[right])
        else:
            L += 1
    arr[right], arr[R] = swap(arr[right], arr[R])
    return left + 1, right


# 堆排序 O(NlogN) O(1)  不稳定
def heapsort(arr):
    # for i in range(len(arr)):
    #     heapinsert(arr, i)

    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, i, len(arr))

    heapsize = len(arr)
    heapsize -= 1
    arr[0], arr[heapsize] = swap(arr[0], arr[heapsize])
    while heapsize > 0:
        heapify(arr, 0, heapsize)
        heapsize -= 1
        arr[0], arr[heapsize] = swap(arr[0], arr[heapsize])
    return arr


def heapinsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        arr[index], arr[int((index - 1) / 2)] = swap(arr[index], arr[int((index - 1) / 2)])
        index = int((index - 1) / 2)


def heapify(arr, index, heapsize):
    left = index * 2 + 1
    while left < heapsize:
        large = left + 1 if left + 1 < heapsize and arr[left] < arr[left + 1] else left
        large = index if arr[index] > arr[large] else large
        if large == index:
            break
        arr[index], arr[large] = swap(arr[index], arr[large])
        index = large
        left = index * 2 + 1


# 基数排序  （or 计数排序） 稳定
def basesort(arr, L, R):
    RADIX = 10
    digits = maxbits(arr)

    backup = [0 for i in range(R - L + 1)]
    for d in range(1, digits + 1):
        count = [0 for i in range(RADIX)]
        for i in range(L, R + 1):
            bitvalue = getbit(arr[i], d)
            count[bitvalue] += 1
        for i in range(1, RADIX):
            count[i] = count[i] + count[i - 1]
        for i in range(R, L - 1, -1):
            bitvalue = getbit(arr[i], d)
            backup[count[bitvalue] - 1] = arr[i]
            count[bitvalue] -= 1
        for i, j in zip(range(L, R + 1), range(0, R - L + 1)):
            arr[i] = backup[j]
    return arr


def maxbits(arr):
    maxvalue = arr[0]
    for i in range(1, len(arr)):
        maxvalue = arr[i] if arr[i] > maxvalue else maxvalue
    digits = 0
    while maxvalue != 0:
        maxvalue = maxvalue // 10
        digits += 1
    return digits


def getbit(num, digits):
    bitvalue = 0
    for i in range(digits):
        bitvalue = num % 10
        num = num // 10
    return bitvalue


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == '__main__':
    # print(swap(1, 2))
    # alist = [1, 3, 4, 2, 5]
    alist = [3, 2, 7, 5, 0, 45, 36, 23, 76, 22]
    start = time.time()

    # print(swapsort(alist))
    # print(bubblesort(alist))
    # print(insertsort(alist))
    # print(mergesort(alist, 0, len(alist) - 1))
    # print(quicksort(alist, 0, len(alist) - 1))
    # print(heapsort(alist))
    print(basesort(alist, 0, len(alist) - 1))
    end = time.time()
    print('time: {}'.format(end - start))
