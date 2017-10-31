"""
    哈夫曼树 - 使用到了基于堆实现的优先队列，可更换
"""
from data_structure.queue.heap_prio_queue import PrioQueue


class BinTreeNode:
    """二叉树"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class HTNode(BinTreeNode):
    """直接将BinTree放入优先队列，则需重写大小判断"""
    def __lt__(self, other):
        return self.data < other.data


class HuffmanPrioQueue(PrioQueue):
    @property
    def number(self):
        """队列中元素数量"""
        return len(self._elems)


def huffman_tree(weights):
    """生成哈夫曼树"""
    trees = HuffmanPrioQueue()
    # 所有元素入队
    for e in weights:
        trees.enqueue(HTNode(e))
    # 哈夫曼算法
    while trees.number > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        data = t1.data + t2.data
        trees.enqueue(HTNode(data, t1, t2))
    return trees.dequeue()
