# 判断满二叉树
# 递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def process(head: TreeNode):
    if head is None:
        return 0, 0
    lheight, lnodes = process(head.left)
    rheight, rnodes = process(head.right)

    height = lheight + 1 if lheight > rheight else rheight + 1
    nodes = lnodes + rnodes + 1

    return height, nodes


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

    h, n = process(treehead)
    print(n == (1 << h) - 1)
