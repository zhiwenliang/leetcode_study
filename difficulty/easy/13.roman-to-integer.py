class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        length = len(s)
        i = 0
        while i < length - 1:
            if (
                (s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"))
                or (s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"))
                or (s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"))
            ):
                num = num - map[s[i]]
                i += 1
            else:
                num += map[s[i]]
                i += 1
        num += map[s[length - 1]]
        return num


class Solution1:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += map[char]
        return number


solution = Solution1()
s = "III"
print(solution.romanToInt(s))
