#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roma = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        res = 0
        if len(s) == 1:
            res = res = res + roma[s[0]]
        for i in range(1, len(s)):
            if roma[s[i-1]] < roma[s[i]]:
                res = res - roma[s[i-1]]
            else:
                res = res + roma[s[i-1]]
            if i == len(s)-1:
                res = res + roma[s[i]]
        return res
# @lc code=end

