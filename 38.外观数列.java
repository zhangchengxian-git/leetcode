/*
 * @lc app=leetcode.cn id=38 lang=java
 *
 * [38] 外观数列
 */

// @lc code=start
class Solution {
    public String countAndSay(int n) {
        String scribe = "1";
        for(int i=1; i<n; i++){
            StringBuffer new_scribe = new StringBuffer("");
            int j=0;
            while(j<scribe.length()){
                int start = j;
                int end = start+1;
                while(end<scribe.length() && scribe.charAt(end)==scribe.charAt(start)){
                    end += 1;
                }
                new_scribe = new_scribe.append(String.valueOf(end-start)).append(scribe.charAt(start));
                j = end;
            }
            scribe = new_scribe.toString();
        }
        return scribe;
    }
}
// @lc code=end

