#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = ''.join(reversed(num1))
        num2 = ''.join(reversed(num2))
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        plus = 0
        res = ""
        i = 0
        while i < len(num1):
            add = int(num1[i]) + int(num2[i]) + plus
            plus = add // 10
            add = add % 10
            res = res + str(add)
            i += 1
        while plus != 0 and i < len(num2):
            add = int(num2[i]) + plus
            plus = add // 10
            add = add % 10
            res = res + str(add)
            i+=1
        if i < len(num2):
            res = res + num2[i: ]
        if plus == 1:
            res = res + '1'
        return ''.join(reversed(res)) 
# @lc code=end

