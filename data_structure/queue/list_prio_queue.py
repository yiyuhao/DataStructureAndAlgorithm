"""
    基于list实现优先队列(假定使用<=比较优先级)
    时间复杂度：
        插入元素: O(n)
        其余    : O(1)
"""


class QueueIndexOutOfRange(ValueError):
    pass


class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        """通过比较找到元素的位置，再insert"""
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def dequeue(self):
        if self.is_empty():
            raise QueueIndexOutOfRange('in pop')
        return self._elems.pop()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise QueueIndexOutOfRange('in top')
        return self._elems[-1]


if __name__ == '__main__':
    queue = PrioQueue([0, 1, 2, 3, 4, 5, 6])
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
