class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = slow = ListNode(0, head)
        while head and head.next:
            if head.val != head.next.val:
                slow.next = head
                slow = head
            else:
                slow.next = head.next
            head = head.next
        return dummy.next