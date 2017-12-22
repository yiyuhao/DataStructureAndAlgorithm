class BTree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __unicode__(self):
        return self.val


def s(xianxu, zhongxu):
    """根据先序遍历与中序遍历生成二叉树"""
    root = xianxu[0]
    index = zhongxu.index(root)

    xian_left = xianxu[1:index + 1]
    xian_right = xianxu[index + 1:]

    zhong_left = zhongxu[0:index]
    zhong_right = zhongxu[index + 1:]

    left = s(xian_left, zhong_left) if xian_left != [] else None
    right = s(xian_right, zhong_right) if xian_right != [] else None

    return BTree(root, left, right)


if __name__ == '__main__':
    xianxu = [1, 2, 4, 7, 3, 5, 6, 8]
    zhongxu = [4, 7, 2, 1, 5, 3, 8, 6]
    r = s(xianxu, zhongxu)
