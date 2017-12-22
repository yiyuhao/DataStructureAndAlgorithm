class Solution:

    def __init__(self):
        self.result = []
        self.lst_len = 0

    def combine(self, lst, k):
        self.lst_len = len(lst)
        self.dfs(lst, k, 0)
        return self.result

    def dfs(self, lst, k, begin, temp=list()):
        if len(temp) < k:
            for i in range(begin, self.lst_len):
                temp.append(lst[i])
                self.dfs(lst, k, i + 1, temp)
                temp.pop()
        else:
            self.result.append(temp.copy())

if __name__ == '__main__':
    s = Solution()
    r = s.combine([1, 2, 3, 4, 5], 3)
    assert r == [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5],
                 [3, 4, 5]]
