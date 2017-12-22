class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def s(head):
    p = head
    stack = []
    rv = []
    while p is not None:
        stack.append(p.val)
        p = p.next

    while stack:
        rv.append(stack.pop())

    return rv


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    assert s(head) == [5, 4, 3, 2, 1]
    assert s(None) == []
