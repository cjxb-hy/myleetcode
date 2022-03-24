# 二叉树遍历
import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归遍历
def preorder(head: TreeNode):
    if head is None:
        return

    print(head.val)
    preorder(head.left)
    preorder(head.right)


def inorder(head: TreeNode):
    if head is None:
        return

    inorder(head.left)
    print(head.val)
    inorder(head.right)


def postorder(head: TreeNode):
    if head is None:
        return

    postorder(head.left)
    postorder(head.right)
    print(head.val)


# 非递归遍历
def firstorder(head: TreeNode):
    stack = []
    stack.append(head)
    while len(stack) > 0:
        temp = stack.pop()
        print(temp.val)
        if temp.right is not None:
            stack.append(temp.right)
        if temp.left is not None:
            stack.append(temp.left)


def midorder(head: TreeNode):
    stack = []
    cur = head
    while len(stack) > 0 or cur is not None:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.val)
            cur = cur.right


def endorder1(head: TreeNode):
    stack1 = []
    stack2 = []
    stack1.append(head)
    while len(stack1) > 0:
        temp = stack1.pop()
        stack2.append(temp)
        if temp.left is not None:
            stack1.append(temp.left)
        if temp.right is not None:
            stack1.append(temp.right)
    while len(stack2) > 0:
        print(stack2.pop().val)


def endorder2(head: TreeNode):
    pass


# 层次遍历/求宽度
def levelorder(head: TreeNode):
    que = queue.Queue()
    que.put(head)
    while not que.empty():
        temp = que.get()
        print(temp.val)
        if temp.left is not None:
            que.put(temp.left)
        if temp.right is not None:
            que.put(temp.right)


def levelorderwidth(head: TreeNode):
    que = queue.Queue()
    hashdict = {}
    que.put(head)
    hashdict[head] = 1
    curlevel = 1
    curlevelnodes = 0
    max = 0
    while not que.empty():
        temp = que.get()
        curnodelevel = hashdict[temp]
        if curlevel == curnodelevel:
            curlevelnodes += 1
        else:
            max = max if max > curlevelnodes else curlevelnodes
            curlevel += 1
            curlevelnodes = 1
        if temp.left is not None:
            hashdict[temp.left] = curnodelevel + 1
            que.put(temp.left)
        if temp.right is not None:
            hashdict[temp.right] = curnodelevel + 1
            que.put(temp.right)
    max = max if max > curlevelnodes else curlevelnodes
    return max


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

    # preorder(treehead)
    # inorder(treehead)
    # postorder(treehead)

    # firstorder(treehead)
    # midorder(treehead)
    # endorder1(treehead)
    # levelorder(treehead)
    # print(levelorderwidth(treehead))
