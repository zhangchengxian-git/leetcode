#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        num_dict = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
        for i in range(len(digits)):
            if i == 0:
                res = res + num_dict[digits[0]]
            else:
                while len(res[0]) == i:
                    tmp = res.pop(0)
                    for ch in num_dict[digits[i]]:
                        res.append(tmp+ch)
        return res
# @lc code=end

