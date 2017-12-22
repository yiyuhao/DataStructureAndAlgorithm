
class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def __init__(self):
        self.lst = []

    def sortList(self, head):
        # write your code here
        if head is None:
            return None

        # trans to lst
        p = head
        while p:
            self.lst.append(p.val)
            p = p.next

        # sort
        self.quick_sort()

        self.lst.reverse()

        # trans to llist
        llist = ListNode(None)

        p = llist
        for i, val in enumerate(self.lst):
            p.val = val
            if i < len(self.lst) - 1:
                p.next = ListNode(None)
                p = p.next
            else:
                p.next = None

        return llist

    def quick_sort(self):

        def q_sort(lst, begin, end):
            """|R|  <R  i|  >= R |j  ???  |"""
            if begin >= end:
                return
            r = lst[begin]
            i, j = begin, begin + 1

            while j <= end:
                if lst[i] < r:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
                j += 1

            lst[begin], lst[i] = lst[i], lst[begin]

            q_sort(lst, begin, i - 1)
            q_sort(lst, i + 1, end)

        q_sort(self.lst, 0, len(self.lst) - 1)
