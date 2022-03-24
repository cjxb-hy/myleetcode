# 寻找两个节点的最低公共祖先
# 递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def process(head: TreeNode, n1: TreeNode, n2: TreeNode):
    if head is None or head == n1 or head == n2:
        return head

    left = process(head.left, n1, n2)
    right = process(head.right, n1, n2)
    if left is not None and right is not None:
        return head

    return left if left is not None else right


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

    node1 = treehead.right.left.left
    node2 = treehead.right.right.right
    print(process(treehead, node1, node2).val)
