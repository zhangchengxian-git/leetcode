#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0 
        dp = [1]
        for i in range(len(s)):
            res = 0
            if s[i] != '0':
                res = res + dp[i]
            if i != 0 and s[i-1] != '0' and int(s[i-1:i+1])<27:
                res = res + dp[i-1]
            dp.append(res)
        return dp[len(s)]
if __name__ == "__main__":
    so = Solution()
    print(so.numDecodings("2611055971756562"))

# @lc code=end

