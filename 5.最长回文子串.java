import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        int max_length = 1;
        String max_str = String.valueOf(s.charAt(0));
        Boolean[][] dp = new Boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
            if (i != s.length() - 1 && s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                max_length = 2;
                max_str = s.substring(i, i + 2);
            }else if(i != s.length() - 1 ){
                dp[i][i+1] = false;
            }
        }

        for (int i = 2; i < s.length(); i++) {
            for (int row = 0; row < s.length() - i; row++) {
                if (s.charAt(row) == s.charAt(i + row) && dp[row + 1][i + row - 1]) {
                    dp[row][i + row] = true;
                    max_length = i + 1;
                    max_str = s.substring(row, i + row + 1);
                }else{
                    dp[row][i + row] = false;
                }
            }

        }
        return max_str;

    }
}
// @lc code=end
