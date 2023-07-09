class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = slow = ListNode(0, head)
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                slow.next = curr.next
            else:
                slow = slow.next
            curr = curr.next
        return dummy.next
        