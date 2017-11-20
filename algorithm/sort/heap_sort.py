def sort(elems):
    """采用大顶堆排序"""
    def siftdown(elems, e, begin, end):
        p, c = begin, begin * 2 + 1
        while c < end:
            if c + 1 < end and elems[c + 1] > elems[c]:
                c += 1
            if e > elems[c]:
                break
            else:
                elems[p] = elems[c]
                p, c = c, c * 2 + 1
        elems[p] = e

    end = len(elems)

    # 构建堆
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)

    # 排序
    for i in range((end - 1), 0, -1):
        # 队首元素替换队尾
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)

    return elems


if __name__ == '__main__':
    l = [4, 5, 3, 6, 7, 9, 11, 0, 2, 1, 8]
    print(sort(l))
