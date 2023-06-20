#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = [[s[0]]] #每个元素为加入当前字符后的分割可能性，如[['1','2'],['12']]
        for i in range(1, len(s)):#加入字符的下标，与s绑定
            new_res = []
            for j in range(len(res)):#被加入的分割序列，与res绑定
                add_res = res[j]
                if add_res[len(add_res)-1] != '0' and int(add_res[len(add_res)-1]+s[i])<256:
                    li = res[j][:len(res[j])-1] + [res[j][len(res[j])-1]+s[i]]
                    if len(li)<=4:
                        new_res.append(res[j][:len(res[j])-1] + [res[j][len(res[j])-1]+s[i]])
                if len(res[j] + [s[i]]) <= 4:
                    new_res.append(res[j] + [s[i]])
            res = new_res
        result = []
        for i in range(len(res)):
            if len(res[i]) == 4:
                result.append('.'.join(res[i]))
        return result

# @lc code=end

