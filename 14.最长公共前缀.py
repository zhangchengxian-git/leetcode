#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 1:
            return strs[0]
        if length == 2:
            if strs[0] == "" or strs[1] == "":
                return ""
            i = 0
            if len(strs[1]) < len(strs[0]):
                s = strs[0]
                strs[0] = strs[1]
                strs[1] = s
            for i in range(len(strs[0])):
                if strs[0][i] == strs[1][i]:
                    i += 1
                else:
                    return strs[0][:i]
            return strs[0][:i+1]
        if length>2:
            str1 = self.longestCommonPrefix(strs[: length//2])
            str2 = self.longestCommonPrefix(strs[length//2: ])
            i = 0
            if str1 == "" or strs == "":
                return ""
            if len(str1) > len(str2):
                s = str2
                str2 = str1
                str1 = s
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    i += 1
                else:
                    return str1[:i]
            return str1[:i+1]
           
if __name__ == "__main__":
    So = Solution()
    #print(So.longestCommonPrefix(["flower","flow","flight"]))
# @lc code=end

