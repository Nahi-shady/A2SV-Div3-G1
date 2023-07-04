class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def helper(node):
            if node == None:
                return ''
            return helper(node.next) + str(node.val)
        s1, s2 = int(helper(l1)), int(helper(l2))
        sum = str(s1 + s2)
        sum = sum[::-1]
        def newNode(nums):
            if len(nums) < 2:
                return ListNode(int(nums[0]))

            new = ListNode(int(nums[0]))
            new.next = newNode(nums[1:])
            return new
        return newNode(sum)