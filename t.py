def sort(lst):
    """采用大顶堆排序"""
    def siftdown(elems, e, begin, end):
        p, c = begin, begin * 2 + 1
        while c <= end:
            if c + 1 <= end and elems[c + 1] > elems[c]:
                c += 1
            if e < elems[c]:
                elems[p] = elems[c]
                p, c = c, c * 2 + 1
            else:
                break
        elems[p] = e

    end = len(lst) - 1
    # 构建堆
    for i in range((end - 1) // 2, -1, -1):
        siftdown(lst, lst[i], i, end)

    # 排序
    for i in range(end, 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i - 1)

    return lst


if __name__ == '__main__':
    l = [4, 5, 3, 6, 7, 9, 11, 0, 2, 1, 8]
    print(sort(l))
