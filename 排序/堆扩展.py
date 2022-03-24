"""
已知一个几乎有序的数组，几乎有序是指，如果把数组排好顺序的话，每个元
素移动的距离可以不超过k，并且k相对于数组来说比较小。请选择一个合适的
排序算法针对这个数据进行排序。
"""
import queue as Q


def heapfunc(arr, k):
    que = Q.PriorityQueue()
    index = 0
    flag = len(arr) if len(arr) < k else k
    while index < flag:
        que.put(arr[index])
        index += 1
    i = 0
    while index < len(arr):
        que.put(arr[index])
        arr[i] = que.get()
        i += 1
        index += 1
    while not que.empty():
        arr[i] = que.get()
        i += 1
    return arr


if __name__ == '__main__':
    alist = [5, 7, 3, 8, 1, 0, 2, 9, 6]
    print(heapfunc(alist, 5))
