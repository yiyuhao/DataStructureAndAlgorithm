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
    """插入排序 依次将每个元素插入到排序队列"""
    for i in range(1, len(lst)):
        e = lst[i]
        j = i
        # 从后往前逐个移动元素，直到找到正确位置
        while j > 0 and lst[j - 1] > e:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = e
    return lst


if __name__ == '__main__':
    l = [10, 4, 5, 3, 6, 7, 9, 0, 2, 1, 8, -2, -3, -1] * 1000
    print(insert_sort(l))
