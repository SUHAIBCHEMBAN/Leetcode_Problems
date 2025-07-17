class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        size = len(x)
        for i in range(size // 2):
            if x[i] != x[size - i - 1]:
                return False
        return True