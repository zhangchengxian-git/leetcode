#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        plus = True
        add_plus = False
        res = 0
        for ch in s:
            if not add_plus and ch == '-':
                plus = False
                add_plus = True
            elif not add_plus and ch == '+':
                add_plus = True
                continue
            elif ch.isdigit():
                if plus:
                    r = res*10+(ord(ch)-ord('0'))
                    if r > 2**31-1:
                        return 2**31-1
                    else:
                        res = r
                else:
                    if res*10-(ord(ch)-ord('0')) < -2**31:
                        return -2**31
                    else:
                        res = res*10-(ord(ch)-ord('0'))
                add_plus = True
            elif not ch.isdigit():
                break
        return res
'''
if __name__ == "__main__":
    so = Solution()
    print(so.myAtoi("478"))'''



# @lc code=end

