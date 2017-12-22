def quick_sort(lst):
    def qsort(lst, begin, end):
        """|R|  <R  i|  >=R   |j  ???  |"""
        if begin >= end:
            return

        r = lst[begin]
        i, j = begin, begin + 1
        while j <= end:
            if lst[j] < r:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
            j += 1

        lst[begin], lst[i] = lst[i], lst[begin]

        qsort(lst, begin, i - 1)
        qsort(lst, i + 1, end)

    qsort(lst, 0, len(lst) - 1)

    return lst


if __name__ == '__main__':
    a = quick_sort([2, 5, 1, -1, -3, 8, 22, 100, 32])
    pass
