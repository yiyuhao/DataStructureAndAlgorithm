# coding: utf-8
class Buildings:
    def __init__(self, buildings):
        self.buildings = buildings

    @property
    def building_out_line(self):
        # 总结果
        rv = []

        # 每一段的大楼轮廓
        block = [0, 0, 0]

        # 对每一段进行遍历，如[0, 1]段, [1,2]段, ...
        for x in range(self.end):
            # 当前段最高大楼
            match = self.match(x)
            # 若x至x+1有楼
            if match:
                # 前一段无大楼(或未初始化)
                if block == [0, 0, 0]:
                    block = [x, x + 1, match[-1]]
                # 前一段大楼轮廓更矮
                elif block[-1] < match[-1]:
                    rv.append(block)
                    block = [x, x + 1, match[-1]]
                # 前段轮廓和当前同高
                elif block[-1] == match[-1]:
                    block[1] += 1
                # 前段轮廓更高
                elif block[-1] > match[-1]:
                    rv.append(block)
                    block = [x, x + 1, match[-1]]
            # x至x+1段无楼 且前段有楼
            elif block != [0, 0, 0]:
                rv.append(block)
                block = [0, 0, 0]

        # 最后的block没有被添加
        if block != [0, 0, 0]:
            rv.append(block)
        return rv

    @property
    def end(self):
        end_index = 0
        for building in self.buildings:
            if building[1] > end_index:
                end_index = building[1]
        return end_index

    def match(self, x):
        """返回x至x+1的最高楼房(或None)"""
        top_building = [0, 0, 0]
        for building in self.buildings:
            # [x, x+1] 属于building
            if x >= building[0] and x + 1 <= building[1]:
                # 获取最高的那个building
                if building[-1] > top_building[-1]:
                    top_building = building
        return top_building if top_building != [0, 0, 0] else None


class Solution:
    """
    @param: buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        # write your code here
        b = Buildings(buildings)
        return b.building_out_line


if __name__ == '__main__':
    s = Solution()
    buildings = [[1, 4, 1], [2, 4, 3], [3, 5, 5]]

    rv = s.buildingOutline(buildings)
    pass
