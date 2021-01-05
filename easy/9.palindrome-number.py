class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit = len(str(x))
        if x >= 0:
            for i in range(digit // 2 + digit % 2):
                n1 = x // 10 ** i % 10
                n2 = x // 10 ** (digit - i - 1) % 10
                if n1 != n2:
                    return False
            return True
        return False

# test case
s = Solution()
x = 0
print(s.isPalindrome(x))
