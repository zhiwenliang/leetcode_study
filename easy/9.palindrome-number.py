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


class SolutionA:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = 1
        digit = 1
        while x / tmp >= 10:
            tmp *= 10
            digit += 1
        for i in range(digit // 2 + digit % 2):
            n1 = x // 10 ** i % 10
            n2 = x // 10 ** (digit - i - 1) % 10
            if n1 != n2:
                return False
        return True


class Solution1:
    def isPalindrome(self, x):
        if x < 0:
            return False
        ranger = 1
        while x // ranger >= 10:
            ranger *= 10
        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            x = (x % ranger) // 10
            ranger /= 100
        return True


class Solution2:
    def isPalindrome(self, x):
        if x < 0:
            return False
        tmp = str(x)
        if tmp == tmp[::-1]:
            return True
        return False


# test case
s = Solution1()
x = 12
print(s.isPalindrome(x))
