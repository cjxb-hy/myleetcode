# 判断完全二叉树
# 层次遍历
import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isfulltree(head: TreeNode):
    que = queue.Queue()
    que.put(head)
    flag = False
    while not que.empty():
        temp = que.get()
        l = temp.left
        r = temp.right
        if (flag and (l is not None or r is not None)) or (l is None and r is not None):
            return False

        if l is not None:
            que.put(l)
        if r is not None:
            que.put(r)
        if l is None or l is None:
            flag = True
    return True


if __name__ == '__main__':
    treehead = TreeNode(5)
    treehead.left = TreeNode(3)
    treehead.right = TreeNode(8)
    treehead.left.left = TreeNode(2)
    treehead.left.right = TreeNode(4)
    treehead.left.left.left = TreeNode(1)
    treehead.right.left = TreeNode(7)
    treehead.right.left.left = TreeNode(6)
    treehead.right.right = TreeNode(10)
    treehead.right.right.left = TreeNode(9)
    treehead.right.right.right = TreeNode(11)

    print(isfulltree(treehead))
