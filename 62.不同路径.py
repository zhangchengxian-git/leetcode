#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[0][0] = 1
                else:
                    path = 0
                    if i != 0:
                        path += res[i-1][j]
                    if j != 0:
                        path += res[i][j-1]
                    res[i][j] = path
        return res[m-1][n-1]

                    
# @lc code=end

