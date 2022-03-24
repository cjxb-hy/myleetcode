# 复制含有随机指针节点的链表

class ListNode(object):
    def __init__(self, val=0, next=None, rand=None):
        self.val = val
        self.next = next
        self.rand = rand


def hashtable(h):
    hashdict = {}
    cur = h
    while cur:
        newnode = ListNode(cur.val)
        hashdict[cur] = newnode
        cur = cur.next

    cur = h
    while cur:
        hashdict[cur].next = hashdict[cur.next]
        hashdict[cur].rand = hashdict[cur.rand]
        cur = cur.next
    return hashdict[h]


# 空间复杂度 O(1)
# 1->2->3->4    1->1'->2->2'->3->3'->4->4'
def insertlist(h):
    cur = h
    while cur:
        newnode = ListNode(cur.val)
        next_cur = cur.next
        cur.next = newnode
        newnode.next = next_cur
        cur = newnode.next

    cur = h
    while cur:
        cur.next.rand = cur.rand.next if cur.rand is not None else None
        cur = cur.next.next

    cur = h
    res = h.next
    while cur:
        next_cur = cur.next.next
        copy_cur = cur.next
        copy_cur.next = next_cur.next if next_cur is not None else None
        cur.next = next_cur
        cur = next_cur
    return res


if __name__ == '__main__':
    pass
