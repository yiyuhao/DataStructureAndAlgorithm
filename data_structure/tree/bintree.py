"""
    二叉树的list实现
    表示例如:
    ['A', ['B', None, None],
          ['C', None, None]]
"""


class BinTree:
    def __init__(self, data, left=None, right=None):
        self._tree = [data, left, right]

    def __str__(self):
        return self._tree.__str__()

    def is_empty(self):
        return self._tree is None

    def root(self):
        return self._tree[0]

    def left(self):
        return self._tree[1]

    def right(self):
        return self._tree[2]


if __name__ == '__main__':
    # 嵌套调用，可以做出任意复杂的二叉树，例如
    t = BinTree(2, BinTree(4), BinTree(8))
    print(t.root(), t.left(), t.right())
