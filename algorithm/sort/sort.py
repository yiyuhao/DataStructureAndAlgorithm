from functools import wraps
import time


def timer(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        end = time.time()
        print('Total time running {f}: {time}s'.format(f=f.__name__, time=str(end - start)))
        return rv

    return decorator


@timer
def insert_sort(lst):
    """插入排序 O(n²) 稳定 依次将每个元素插入到排序队列"""
    for i in range(1, len(lst)):
        e = lst[i]
        j = i
        # 从后往前逐个移动元素，直到找到正确位置
        while j > 0 and lst[j - 1] > e:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = e


@timer
def select_sort(lst):
    """直接选择排序 O(n²) 不稳定 交换最小元素与已排序段末尾元素"""
    for i in range(len(lst) - 1):
        # k是已知最小元素的位置
        k = i
        for j in range(i, len(lst)):
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]


@timer
def bubble_sort(lst):
    """冒泡排序 O(n²)"""
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                found = True
        if not found:
            break


@timer
def bubble_sort2(lst):
    """
        先从左到右冒泡一次，再从右到左冒泡一次, ...
        时间复杂度与冒泡相同，但具有了适应性
    """

    def get_index(length):
        """
            如length=99
            yield 0,99, 98,0, 1,98, 97,1, ... 49,50
            用于遍历列表：先从0-99, 再从98-0, ..."""
        start = 0
        end = length
        while start < end:
            yield start
            yield end
            end -= 1
            if start < end:
                yield end
                yield start
            start += 1

    switch = True
    for i in get_index(len(lst) - 1):
        # 得到如start=0, end=99
        if switch:
            start = i
        else:
            end = i
            # 变量bubble记录是否进行过排序，
            bubble = False

            # 从左到右冒泡一次
            if start < end:
                # 进行一次从start到end的冒泡
                for j in range(start, end + 1):
                    if j + 1 <= end and lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        bubble = True
            # 从右到左冒泡一次
            else:
                for j in range(start, end - 1, -1):
                    if j - 1 >= end and lst[j - 1] > lst[j]:
                        lst[j], lst[j - 1] = lst[j - 1], lst[j]
                        bubble = True

            # 若bubble=False代表已排序好，需提前结束循环
            if not bubble:
                break
        switch = not switch


if __name__ == '__main__':
    # l = [4, 5, 3, 6, 7, 9, 0, 2, 1, 8] * 300

    l = [i for i in range(3000)]
    l.append(-100)
    bubble_sort(l)
    print(l)

    l = [i for i in range(3000)]
    l.append(-100)
    bubble_sort2(l)
    print(l)
