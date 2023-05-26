class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if "-" in x:
            x = x[1:]
            x = x + '-'
        x = int(x[::-1])
        if x <= -2**31 or x >= (2**31)-1:
            return 0
        return x