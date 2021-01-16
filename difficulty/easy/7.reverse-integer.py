class Solution:
    def reverse(self, x: int) -> int:
        digit = len(str(abs(x)))
        tmp = 0
        for i in range(digit):
            tmp = tmp + (abs(x) // 10 ** (i) % 10) * 10 ** (digit - i - 1)
        tmp = tmp if x >= 0 else -1 * tmp
        if tmp > 2 ** 31 - 1 or tmp < -(2 ** 31):
            return 0
        return tmp


class Solution1:
    def reverse(self, x: int) -> int:
        digit = len(str(abs(x)))
        tmp = ""
        tmp1 = str(abs(x))
        for i in range(digit):
            tmp = tmp + tmp1[digit - i - 1]
        tmp = int(tmp) if x >= 0 else -1 * int(tmp)
        if tmp > 2 ** 31 - 1 or tmp < -(2 ** 31):
            return 0
        return tmp


class Solution2:
    def reverse(self, x):
        if x == 0:
            s = 0
        elif x > 0:
            s = 1
        else:
            s = -1
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)


# test case
s = Solution2()
print(s.reverse(123))
