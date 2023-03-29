#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if ' ' not in s:
            return len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return len(s[i+1: ])
# @lc code=end

