#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = nums[0]
        maxSub = nums[0]
        for i in range(1, len(nums)):
            if dp > 0:
                dp = dp + nums[i]
            else:
                dp = nums[i]
            if dp > maxSub:
                maxSub = dp
        return maxSub


# @lc code=end

