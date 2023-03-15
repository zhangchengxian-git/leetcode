#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        max_length = 0
        char_set = set()
        length = 0
        while left < len(s)-max_length and right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                length += 1
                right += 1
            else:
                if max_length < length:
                    max_length = length
                length -= 1
                char_set.remove(s[left])
                left += 1
        if max_length < length:
            max_length = length
        return max_length

# @lc code=end

