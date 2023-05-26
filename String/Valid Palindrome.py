class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = "".join(c for c in s if c.isalnum()).lower()

        if cleaned_s == cleaned_s[::-1]:
            return True
        return False