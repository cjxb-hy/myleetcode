# 将单向链表按某值划分成左边小、中间相等、右边大的形式
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partitionsort(h, value):
    tmplist = []
    cur = h
    while cur:
        tmplist.append(cur.val)
        cur = cur.next
    tmplist.append(value)
    partitionlist = partition(tmplist, 0, len(tmplist) - 1)
    cur = h
    for index in range(len(partitionlist) - 1):
        cur.val = partitionlist[index]
        cur = cur.next
    return h


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
    return arr


# 空间复杂度O(1)
def partitionsort2(h, value):
    sh = None
    st = None
    eh = None
    et = None
    bh = None
    bt = None
    while h:
        cur = h.next
        h.next = None
        if h.val < value:
            if sh is None:
                sh = h
                st = h
            else:
                st.next = h
                st = h
        elif h.val == value:
            if eh is None:
                eh = h
                et = h
            else:
                et.next = h
                et = h
        else:
            if bh is None:
                bh = h
                bt = h
            else:
                bt.next = h
                bt = h
        h = cur

    if st is not None:
        st.next = eh
        et = et if et is not None else st

    if et is not None:
        et.next = bh

    cur = sh if sh is not None else eh
    cur = cur if cur is not None else bh
    return cur


def swap(value1, value2):
    value1 = value1 ^ value2
    value2 = value1 ^ value2
    value1 = value1 ^ value2
    return value1, value2


if __name__ == '__main__':
    alist = [0, 4, 1, 6, 5, 4, 5, 7, 8, 4, 3]
    head = ListNode(alist[0])
    P = head
    for i in range(1, len(alist)):
        node = ListNode(alist[i])
        P.next = node
        P = P.next

    blist = []
    partitionlink = partitionsort2(head, 4)
    while partitionlink is not None:
        blist.append(partitionlink.val)
        partitionlink = partitionlink.next
    print(blist)
