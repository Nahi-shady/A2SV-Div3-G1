# Brute force
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

# Optimized

class Solution(object):
    def middleNode(self, head):
        runner = head
        while runner and runner.next:
            head = head.next
            runner = runner.next.next
        return head

        