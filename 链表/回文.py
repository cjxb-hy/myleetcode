# 判断单链表是否为回文链表
# 如 1->2->3->2->1
class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def ishw_stack(h) -> bool:
    stack = []
    p = h
    while p:
        stack.append(p.val)
        p = p.next
    p = h
    while len(stack) > 0 and p:
        if p.val != stack.pop():
            return False
        p = p.next
    return True


def fs_point(h) -> bool:
    fast = h
    slow = h
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    cur = slow.next
    slow.next = None
    while cur:
        tmp = cur.next
        cur.next = slow
        slow = cur
        cur = tmp

    right = slow
    left = h
    flag = True
    while left and right:
        if left.val != right.val:
            flag = False
            break
        left = left.next
        right = right.next

    cur = slow.next
    slow.next = None
    while cur:
        tmp = cur.next
        cur.next = slow
        slow = cur
        cur = tmp
    return flag


if __name__ == '__main__':
    alist = [0, 1, 2, 3, 2, 1, 0]
    head = ListNode(alist[0])
    P = head
    for i in range(1, len(alist)):
        node = ListNode(alist[i])
        P.next = node
        P = P.next
    b = fs_point(head)
    print('是回文数' if b else '不是回文数')
