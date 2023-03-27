#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_return = self.sub(needle)
        haystack_index = 0
        needle_index = 0
        while(haystack_index<len(haystack)):
            if haystack[haystack_index] == needle[needle_index]:
                haystack_index += 1
                needle_index += 1
            elif needle_index == 0:
                haystack_index += 1
            else:
                needle_index = needle_return[needle_index-1]
            if needle_index == len(needle):
                return haystack_index - len(needle)
        return -1
            
    def sub(self, needle: str) -> List[int]:
        if str == '':
            return []
        res = [0]
        k = 0
        for i in range(1, len(needle)):
            while k > 0 and needle[k] != needle[i]:
                k = res[k-1]
            if needle[k] == needle[i]:
                k += 1
            res.append(k)
        return res

if __name__ == "__main__":
    so = Solution()
    print(so.strStr("adcadcaddcadde", "adcadde"))
# @lc code=end

