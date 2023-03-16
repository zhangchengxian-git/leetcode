#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        max_str = s[0]
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i!=len(s)-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                max_length = 2
                max_str = s[i: i+2]
        for i in range(2, len(s)):
            if i+1 > max_length:
                for row in range(len(s)-i):
                    if s[row] == s[i+row] and dp[row+1][i+row-1]:
                        dp[row][i+row] = True
                        max_length = i+1
                        max_str = s[row: i+row+1]
        return max_str
if __name__ == "__main__":
    so = Solution()
    print(so.longestPalindrome('caba'))
# @lc code=end

