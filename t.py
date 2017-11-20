# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class HashHeap:
    def __init__(self):
        self.heap = [0]
        self.hash = {}

    def add(self, key, value):
        self.heap.append((key, value))
        self.hash[key] = self.heap[0] + 1
        self.heap[0] += 1
        self._siftup(self.heap[0])

    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.heap[0])
        del self.hash[self.heap[self.heap[0]][0]]
        self.heap.pop()
        self.heap[0] -= 1
        if index <= self.heap[0]:
            index = self._siftup(index)
            self._siftdown(index)

    def hasKey(self, key):
        return key in self.hash

    def max(self):
        return 0 if self.heap[0] == 0 else self.heap[1][1]

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hash[self.heap[a][0]] = a
        self.hash[self.heap[b][0]] = b

    def _siftup(self, index):
        while index != 1:
            if self.heap[index][1] <= self.heap[index // 2][1]:
                break
            self._swap(index, index // 2)
            index = index // 2
        return index

    def _siftdown(self, index):
        size = self.heap[0]
        while index < size:
            t = index
            if index * 2 <= size and self.heap[t][1] < self.heap[index * 2][1]:
                t = index * 2
            if index * 2 + 1 <= size and self.heap[t][1] < self.heap[index * 2 + 1][1]:
                t = index * 2 + 1
            if t == index:
                break
            self._swap(index, t)
            index = t
        return index


class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        if len(buildings) == 0:
            return []

        begins = [(b[0], b[2], index) for index, b in enumerate(buildings)]
        ends = [(b[1], b[2], index) for index, b in enumerate(buildings)]
        heights = sorted(begins + ends, key=lambda x: x[0])

        hashheap = HashHeap()
        y = {}
        for x, height, index in heights:
            if hashheap.hasKey(index):
                hashheap.remove(index)
            else:
                hashheap.add(index, height)
            y[x] = hashheap.max()

        temp = []
        lastX, lastY = None, None
        for x in sorted(y.keys()):
            if lastX is not None and lastY != 0:
                temp.append((lastX, x, lastY))
            lastX, lastY = x, y[x]

        results = []
        lastInterval = temp[0]
        for start, end, height in temp[1:]:
            if start == lastInterval[1] and height == lastInterval[2]:
                lastInterval = lastInterval[0], end, height
            else:
                results.append(lastInterval)
                lastInterval = (start, end, height)
        results.append(lastInterval)
        return results


if __name__ == '__main__':
    s = Solution()
    b = [(1, 7, 1),
         (3, 5, 2)]
    s.buildingOutline(buildings=b)
