#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        unsteal = [0, nums[1]]
        steal = [nums[0], nums[0]]
        for i in range(2, len(nums)):
            if i != len(nums)-1:
                unsteal = self.getMax(unsteal, nums[i])
                steal = self.getMax(steal, nums[i])
            else:
                unsteal = self.getMax(unsteal, nums[i])
        return max(max(unsteal), max(steal))
    
    def getMax(self, steal: List[int], num:int):
        tmp = max(steal[0]+num, steal[1])
        steal[0] = steal[1]
        steal[1] = tmp
        return steal

# @lc code=end

