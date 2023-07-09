# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur= pre.next
        
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt

        pre.next.next = cur
        pre.next = node
        return dummy.next