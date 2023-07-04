class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        current = head
        while current:
            nums.append(current)
            current = current.next
        mid = len(nums)//2
        return nums[mid]