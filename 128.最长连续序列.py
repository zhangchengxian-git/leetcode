#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                curr_num = num
                curr_length = 1
                while curr_num+1 in nums:
                    curr_num += 1
                    curr_length += 1
                
                longest = max(longest, curr_length)
        return longest
# @lc code=end

