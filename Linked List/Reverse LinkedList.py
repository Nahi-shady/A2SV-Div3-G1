class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev