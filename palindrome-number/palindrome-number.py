class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        n.split()
        return n == n[::-1]