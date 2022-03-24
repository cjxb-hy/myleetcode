# 判断平衡二叉树
# 递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isbalancetree(head: TreeNode):
    if head is None:
        return True, 0
    leftbalance, leftheight = isbalancetree(head.left)
    rightbalance, rightheight = isbalancetree(head.right)

    height = leftheight + 1 if leftheight > rightheight else rightheight + 1
    isbalance = leftbalance and rightbalance and abs(leftheight - rightheight) < 2
    return isbalance, height


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

    print(isbalancetree(treehead))
