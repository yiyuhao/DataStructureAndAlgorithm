class HashHeap:
    def __init__(self, heap=None, hash_=None):
        self.heap = heap or []
        self.hash = hash_ or {}

    def __contains__(self, item):
        return item in self.hash

    @property
    def length(self):
        return len(self.heap)

    def _swap(self, i, j):
        # 更新hash
        self.hash[self.heap[i][0]], self.hash[self.heap[j][0]] = j, i
        # 交换位置
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def siftup(self, index=None):
        c_index = index or self.length - 1  # child
        p_index = (c_index - 1) // 2  # parent
        while p_index >= 0:
            c_value = self.heap[c_index][1]
            p_value = self.heap[p_index][1]
            # 子上升
            if c_value > p_value:
                self._swap(c_index, p_index)
                c_index, p_index = p_index, (p_index - 1) // 2
            else:
                # 确定了位置
                break

    def siftdown(self, index=0, end=None):
        end = end or self.length - 1
        p_index = index  # parent
        c_index = p_index * 2 + 1  # child
        while c_index <= end:
            if c_index + 1 <= end:
                # 将两个子最大的那个最为c_index
                if self.heap[c_index + 1][1] > self.heap[c_index][1]:
                    c_index += 1
            # 下降
            if self.heap[c_index][1] > self.heap[p_index][1]:
                self._swap(c_index, p_index)
                p_index, c_index = c_index, c_index * 2 + 1
            else:
                break

    def add(self, index, height):
        self.heap.append((index, height))
        self.hash[index] = self.length - 1
        self.siftup()

    def remove(self, index):
        heap_position = self.hash[index]
        # 将该元素与最后元素替换
        self._swap(self.length - 1, heap_position)
        # 删除这个元素与其在hash table的记录
        del self.hash[index]
        self.heap.pop()
        # 整理堆
        self.siftdown(heap_position)

    @property
    def max(self):
        return self.heap[0][1] if self.heap else 0


class Solution:
    """
    @param: buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        # 分段
        starts = [(building[0], building[2], index) for index, building in enumerate(buildings)]
        ends = [(building[1], building[2], index) for index, building in enumerate(buildings)]
        segment = starts + ends

        # 对分段排序
        segment = sorted(segment, key=lambda x: x[0])

        # 选出每段最高的轮廓
        hashheap = HashHeap()
        shadows = []
        for x, height, index in segment:
            if index in hashheap:
                hashheap.remove(index)
            else:
                hashheap.add(index, height)
            # 每一段中每个大楼变化都进行阴影的更新
            if shadows and x == shadows[-1][0]:
                shadows[-1] = (x, hashheap.max)
            else:
                shadows.append((x, hashheap.max))

        # 将连续的阴影拼成block, 放入最终结果
        rv = []
        block = [0, 0, 0]
        for x, height in shadows:
            # 初始赋值
            if block == [0, 0, 0]:
                block = [x, x + 1, height]
            # 相同高度楼房
            elif block[-1] == height:
                block[1] = x + 1
            # 不同高度楼房，将之前的block存入rv，再重设一个block
            elif block[-1] != height:
                block[1] = x
                if block[-1] != 0:
                    rv.append(block)
                block = [x, x + 1, height]

        return rv

if __name__ == '__main__':
    s = Solution()
    b = [(1, 7, 1),
         (3, 5, 2)]
    s.buildingOutline(buildings=b)
