# 判断搜索二叉树
# 中序遍历，升序
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def issearcht(head: TreeNode):
    stack = []
    cur = head
    predata = -sys.maxsize - 1
    while len(stack) > 0 or cur is not None:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur.val <= predata:
                return False
            else:
                predata = cur.val
            cur = cur.right
    return True


# 递归
global prevalue
prevalue = - sys.maxsize - 1


def issearchtree(head: TreeNode):
    if head is None:
        return True
    global prevalue

    flag = issearchtree(head.left)
    if not flag:
        return False
    if head.val <= prevalue:
        return False
    else:
        prevalue = head.val

    return issearchtree(head.right)


def process(head: TreeNode):
    if head is None:
        return None, None, None

    lissearch, lminvalue, lmaxvalue = process(head.left)
    rissearch, rminvalue, rmaxvalue = process(head.right)

    minvalue = head.val
    maxvalue = head.val
    if lissearch is not None:
        minvalue = minvalue if minvalue < lminvalue else lminvalue
        maxvalue = maxvalue if maxvalue > lmaxvalue else lmaxvalue
    if rissearch is not None:
        minvalue = minvalue if minvalue < rminvalue else rminvalue
        maxvalue = maxvalue if maxvalue > rmaxvalue else rmaxvalue

    issearch = True
    if (lissearch is not None) and (not lissearch or lmaxvalue >= head.val):
        issearch = False
    if (rissearch is not None) and (not rissearch or rminvalue <= head.val):
        issearch = False
    return issearch, minvalue, maxvalue


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

    print(process(treehead))
