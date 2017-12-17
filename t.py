def heap_sort(lst):

    if not isinstance(lst, list):
        raise TypeError('params is allowed to be list only')

    def siftdown(lst, e, begin, end):
        p, c = begin, begin * 2 + 1

        while c <= end:
            if c + 1 <= end and lst[c + 1] > lst[c]:
                c += 1
            if e <= lst[c]:
                lst[p] = lst[c]
                p, c = c, c * 2 + 1
            else:
                break
        lst[p] = e

    end = len(lst) - 1

    # build heap
    for i in range((end - 1) // 2, -1, -1):
        siftdown(lst, lst[i], i, end)

    # sort
    for i in range(end, 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i - 1)

    return lst
