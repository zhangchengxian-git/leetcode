#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
# @lc code=end

