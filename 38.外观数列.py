#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        scribe = '1'
        for i in range(1, n):
            j = 0
            new_scribe = ''
            while j < len(scribe):
                start = j
                end = start + 1
                while end < len(scribe) and scribe[end] == scribe[start]:
                    end += 1
                new_scribe = new_scribe + str(end-start) + scribe[start]
                j = end
            scribe = new_scribe
        return scribe
                
# @lc code=end

