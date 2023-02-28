#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        if rowIndex == 0:
            return res
        for i in range(1, int(rowIndex/2)+1):
            res.append(int(res[i-1]*(rowIndex-i+1)/i))
        if rowIndex%2 == 1:
            res = res + res[len(res)-1::-1]
        else:
            res = res + res[len(res)-2::-1]
        return res
if __name__ == "__main__":
    so = Solution()
    #print(so.getRow(4))

# @lc code=end

