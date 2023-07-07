class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        length, end = 1, head
        while end.next:
            end = end.next
            length += 1
        k = k % length
        if k == 0:
            return head
        curr = head
        for i in range(length -1 -k):
            curr = curr.next
        temp = curr.next
        curr.next = None
        end.next = head

        return temp





