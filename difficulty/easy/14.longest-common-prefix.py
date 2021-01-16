from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len1 = len(strs[0])
        if not strs:
            return ""
        for i in range(len1):
            tmp = strs[0][: i + 1]
            for j in strs:
                tmp1 = j[: i + 1]
                if tmp != tmp1:
                    return strs[0][:i]
        return strs[0]


solution = Solution()
strs = ["asfe", "asdf"]
print(solution.longestCommonPrefix(strs))
