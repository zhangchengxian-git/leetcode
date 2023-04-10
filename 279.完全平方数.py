#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            min_dp = n
            for j in range(1, math.floor(i**0.5)+1):
                if min_dp > dp[i-j**2]:
                    min_dp = dp[i-j**2]
            dp.append(1+min_dp)
        return dp[n]
# @lc code=end

