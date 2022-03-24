# 微软折纸题
# 递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 序列化
def process(i: int, N: int, flag: bool):
    if i > N:
        return
    process(i + 1, N, True)
    print('凹' if flag else '凸')
    process(i + 1, N, False)


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

    process(1, 4, True)
