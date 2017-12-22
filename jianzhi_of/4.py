from copy import deepcopy


def s(lst, num):
    """从左下角比较"""
    if not lst:
        return False

    while lst and lst[0]:
        if num < lst[-1][0]:
            lst.pop()
        elif num == lst[-1][0]:
            return True
        else:
            for i in range(0, len(lst)):
                del lst[i][0]
    return False

if __name__ == '__main__':
    l = [[1, 2, 4, 6],
         [2, 4, 7, 8],
         [8, 9, 10, 11],
         [9, 12, 13, 15]]

    assert s(deepcopy(l), 7) is True
    assert s(deepcopy(l), 15) is True
    assert s(deepcopy(l), 1) is True
    assert s(deepcopy(l), 4) is True

    assert s(deepcopy(l), 5) is False
    assert s(deepcopy(l), 18) is False
    assert s(deepcopy(l), 0) is False

    l = []
    assert s(deepcopy(l), 1) is False
