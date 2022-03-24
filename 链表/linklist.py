class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


# 不带头节点
# def reverse(h):
#     pre = None
#     cur = h
#     while cur:
#         tmp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = tmp
#     return pre


# if __name__ == '__main__':
#     alist = [0, 1, 2, 3, 4, 5, 6]
#     head = ListNode(alist[0])
#     P = head
#     for i in range(1, len(alist)):
#         node = ListNode(alist[i])
#         P.next = node
#         P = P.next
#     reversehead = reverse(head)
#     while reversehead is not None:
#         print(reversehead.val)
#         reversehead = reversehead.next


# 带头结点
def reverse(h):
    p = h.next
    h.next = None
    while p:
        q = p
        p = p.next
        q.next = h.next
        h.next = q
    return h


# 两个有序链表共有值
def share(h1, h2):
    p1 = h1.next
    p2 = h2.next
    sharelist = []
    while p1 and p2:
        if p1.val == p2.val:
            sharelist.append(p1.val)
            p1 = p1.next
            p2 = p2.next
        elif p1.val < p2.val:
            p1 = p1.next
        else:
            p2 = p2.next
    return sharelist


if __name__ == '__main__':
    alist = [0, 1, 2, 3, 4, 5, 6]
    head = ListNode()
    P = head
    for i in range(len(alist)):
        node = ListNode(alist[i])
        P.next = node
        P = P.next

    alist2 = [0, 2, 4, 5, 6, 7, 8]
    head2 = ListNode()
    P2 = head2
    for i in range(len(alist2)):
        node = ListNode(alist2[i])
        P2.next = node
        P2 = P2.next
    print(share(head, head2))

    # reverse
    value = []
    reversehead = reverse(head)
    reversehead = reversehead.next
    while reversehead is not None:
        value.append(reversehead.val)
        reversehead = reversehead.next
    print(value)
