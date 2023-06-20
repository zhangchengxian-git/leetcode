#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        a = '0'*(len(b)-len(a))+a
        plus = 0
        res = ''
        for i in range(len(a)-1, -1 ,-1):
            add = int(a[i])+int(b[i])+plus
            plus = add//2
            add = add % 2
            res = str(add) + res
        if plus==1:
            res = '1'+res
        return res
        
# @lc code=end

