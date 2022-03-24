# 二叉树序列化
# 递归
import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 序列化
def process(head: TreeNode):
    if head is None:
        return '#_'

    res = str(head.val) + '_'
    res += process(head.left)
    res += process(head.right)

    return res


# 反序列化
def reverseprocess(s: str):
    que = queue.Queue()
    alist = s.split('_')
    for i in alist:
        que.put(i)
    return rp(que)


def rp(aque: queue):
    temp = aque.get()
    if temp == '#':
        return None
    head = TreeNode(int(temp))
    head.left = rp(aque)
    head.right = rp(aque)
    return head


if __name__ == '__main__':
    treehead = TreeNode(5)
    treehead.left = TreeNode(3)
    treehead.right = TreeNode(8)
    treehead.left.left = TreeNode(2)
    treehead.left.right = TreeNode(4)
    treehead.left.left.left = TreeNode(1)
    # treehead.right.left = TreeNode(7)
    # treehead.right.left.left = TreeNode(6)
    # treehead.right.right = TreeNode(10)
    # treehead.right.right.left = TreeNode(9)
    # treehead.right.right.right = TreeNode(11)

    sequence = process(treehead)
    treehead2 = reverseprocess(sequence)
    print(treehead2.val)
    print(treehead2.left.val)
    print(treehead2.right.val)
    print(treehead2.left.left.val)
    print(treehead2.left.right.val)
    print(treehead2.left.left.left.val)
