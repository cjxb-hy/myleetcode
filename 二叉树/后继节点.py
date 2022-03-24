# 寻找两个节点的最低公共祖先
# 递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def process(node: TreeNode):
    if node is None:
        return node
    if node.right is not None:
        temp = getleft(node.right)
        return temp
    else:
        parent = node.parent
        while parent is not None and parent.left != node:
            node = parent
            parent = node.parent
    return parent


def getleft(node: TreeNode):
    if node is None:
        return node

    while node.left is not None:
        node = node.left

    return node


if __name__ == '__main__':
    treehead = TreeNode(5)
    treehead.left = TreeNode(3)
    treehead.left.parent = treehead
    treehead.right = TreeNode(8)
    treehead.right.parent = treehead
    treehead.left.left = TreeNode(2)
    treehead.left.left.parent = treehead.left
    treehead.left.right = TreeNode(4)
    treehead.left.right.parent = treehead.left
    treehead.left.right.right = TreeNode(1)
    treehead.left.right.right.parent = treehead.left.right

    print(process(treehead.left.right.right).val)
