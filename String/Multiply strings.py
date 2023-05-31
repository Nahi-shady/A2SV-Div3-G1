class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def convert(txt):
            res = 0
            for i in txt:
                res = res * 10 + ord(i) - ord('0')
            return res
        return str(convert(num1)*convert(num2))