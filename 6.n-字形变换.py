#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows==1:
            return s
        res = ''
        left = 2*numRows-2
        right = 0
        for i in range(numRows):
            if(left == 2*numRows-2):
                j = 0
                while j<len(s):
                    res = res+s[j]
                    j = j+left
                left = left-2
                right = 2*numRows-2-left
            elif(right == 2*numRows-2):
                j = numRows-1
                while j<len(s):
                    res = res+s[j]
                    j = j+right
            else:
                up = True
                j = i
                while j <len(s):
                    res = res + s[j]
                    if up:
                        up = False
                        j = j+left
                    elif not up:
                        up = True
                        j = j+right
                left = left-2
                right = right+2
        return res
                




# @lc code=end

