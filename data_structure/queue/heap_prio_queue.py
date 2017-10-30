"""
    优先队列的堆实现
    时间复杂度:
        堆构建    : O(n)
        插入与弹出: O(log n)
"""


class QueueIndexOutOfRange(ValueError):
    pass


class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.build_heap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise QueueIndexOutOfRange('in peek')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e)

    def siftup(self, e):
        """
            (不断用e与其父结点的数据比较，如果e较小就交换位置，e不断上移)
            但这里是拿着e而不放入堆，这样能略微减少开销
        """
        last = len(self._elems) - 1
        elems = self._elems
        # i为最后节点，j为i的父节点
        i, j = last, (last - 1) // 2
        # 当筛选至顶点，或者e比其父节点优先
        while i > 0 and e < elems[j]:
            # 将父节点沉入i
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        # 当e找到自己位置时 或者上移完后e在最顶
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise QueueIndexOutOfRange('in dequeue')
        elems = self._elems
        e0 = elems[0]
        # 将最后一个结点放入堆顶，进行向下筛选
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        # p=parent c=children
        elems, p, c = self._elems, begin, begin * 2 + 1
        while c < end:
            # 右子 < 左子 时c选为右子(elems[c]不大于其兄弟结点的数据)
            if c + 1 < end and elems[c + 1] < elems[c]:
                c += 1
            # e下沉到正确位置时退出
            if e < elems[c]:
                break
            # c在3者中最小，上移
            elems[p] = elems[c]
            p, c = c, 2 * c + 1
        elems[p] = e

    def build_heap(self):
        end = len(self._elems)
        # 从所有分支节点(即堆的倒数第二层)遍历至顶点，逐个将该节点在所处子树上进行向下筛选
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)
