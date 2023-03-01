#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        unstone = 0
        stone = nums[0]
        for i in range(1, len(nums)):
            tep = unstone
            unstone = max(unstone, stone)
            stone = tep + nums[i]
        return max(unstone, stone)'''
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            tmp = max(dp[0]+nums[i], dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
        return max(dp[0], dp[1])
        
        
# @lc code=end

