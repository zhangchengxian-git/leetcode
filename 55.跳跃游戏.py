#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        length = len(nums)
        if length == 1:
            return True
        for i in range(length):
            if i > far and i != 0:
                return False
            elif i == 0 and nums[i] == 0:
                return False
            far = max(far, nums[i]+i)

        return True
        


if __name__ == "__main__":
    so = Solution()
    print(so.canJump([3,2,1,0,4]))
# @lc code=end

