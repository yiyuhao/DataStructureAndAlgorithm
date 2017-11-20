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

        if len(buildings) == 0:
            return []

        # 分段
        starts = [(building[0], building[2], index) for index, building in enumerate(buildings)]
        ends = [(building[1], building[2], index) for index, building in enumerate(buildings)]
        segment = starts + ends

        # 对分段排序
        segment = sorted(segment, key=lambda x: x[0])

        # 选出每段最高的轮廓
        hashheap = HashHeap()
        shadows = {}
        for x, height, index in segment:
            if index in hashheap:
                hashheap.remove(index)
            else:
                hashheap.add(index, height)
            shadows[x] = hashheap.max

        # 将连续的阴影拼成block, 放入最终结果
        rv = []
        block = [0, 0, 0]
        for x, height in shadows.items():
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
    b = [[2, 982, 227], [8, 517, 41], [3, 146, 173], [10, 652, 117], [9, 743, 344], [4, 995, 104], [1, 159, 123],
         [2, 535, 342], [6, 122, 57], [6, 826, 135], [9, 748, 81], [9, 865, 140], [3, 423, 332], [2, 92, 32],
         [4, 507, 252], [5, 461, 252], [1, 74, 36], [10, 835, 264], [2, 511, 206], [8, 695, 236], [4, 768, 354],
         [2, 184, 147], [10, 564, 69], [4, 490, 196], [2, 889, 241], [3, 102, 177], [2, 609, 251], [5, 443, 277],
         [7, 39, 208], [10, 939, 129], [6, 45, 94], [8, 301, 23], [3, 557, 89], [3, 772, 272], [3, 637, 16],
         [9, 134, 95], [9, 35, 27], [9, 38, 61], [3, 702, 307], [5, 633, 25], [6, 567, 142], [2, 235, 309],
         [2, 804, 84], [6, 279, 82], [7, 902, 12], [3, 671, 31], [3, 269, 293], [7, 736, 46], [2, 331, 200],
         [5, 564, 309], [8, 312, 221], [4, 129, 145], [5, 655, 298], [3, 890, 110], [5, 906, 125], [4, 960, 294],
         [1, 2, 347], [7, 270, 78], [8, 132, 348], [8, 884, 285], [10, 392, 93], [10, 230, 243], [1, 933, 119],
         [4, 54, 95], [4, 649, 81], [6, 961, 76], [8, 274, 354], [6, 218, 124], [5, 134, 347], [4, 637, 108],
         [10, 126, 319], [3, 730, 30], [2, 438, 292], [5, 342, 277], [9, 922, 270], [2, 163, 47], [4, 874, 50],
         [5, 196, 277], [10, 828, 310], [10, 121, 43], [3, 26, 93], [5, 341, 121], [9, 925, 73], [3, 715, 160],
         [3, 512, 95], [5, 631, 276], [3, 65, 288], [3, 1000, 74]]
    s.buildingOutline(buildings=b)
