class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        val = list(s)
        for i in spaces:
            val[i] = ' ' + val[i]
        return ''.join(val)