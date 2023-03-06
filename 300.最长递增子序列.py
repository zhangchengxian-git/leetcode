#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > dp[length-1]:
                dp.append(nums[i])
                length = length+1
            else:
                dp[self.findLastSmaller(dp, 0, len(dp)-1, nums[i])] = nums[i]
        return length

    def findLastSmaller(self, dp, left, right, num) -> int:
        loc = right
        while left < right:
            mid = (left+right)//2
            if dp[mid] >= num:
                loc = mid
                right = mid
            else:
                left = mid+1
        return loc
# @lc code=end

