#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        tmp = []
        for i in range(len(s)):
            if s[i] in '([{':
                tmp.append(s[i])
            elif s[i] == ')' and tmp != []:
                    last = tmp.pop()
                    if last != '(':
                        return False
            elif s[i] == ']' and tmp != []:
                    last = tmp.pop()
                    if last != '[':
                        return False
            elif s[i] == '}' and tmp != []:
                    last = tmp.pop()
                    if last != '{':
                        return False
            else:
                 return False
        if tmp == []:
            return True
        else:
            return False
# @lc code=end

