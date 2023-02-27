#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            res.append(self.getNum(i))
        return res
    
    def getNum(self, row: int) -> List[int]:
        row_num = [1]
        row = row - 1
        if row == 0:
            return row_num
        for i in range(1, int(row/2)+1):
            row_num.append(int(row_num[i-1]*(row-i+1)/i))
        if row%2 == 1:
            return row_num + row_num[::-1]
        elif row%2 == 0:
            return row_num + row_num[len(row_num)-2::-1]


# @lc code=end

