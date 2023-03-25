import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=17 lang=java
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> combs = new ArrayList<String>();
        if(digits.length()==0){
            return combs;
        }
        Map<Character, String> phone = new HashMap<Character,String>() {
            {
                put('2', "abc");
                put('3', "def");
                put('4', "ghi");
                put('5', "jkl");
                put('6', "mno");
                put('7', "pqrs");
                put('8', "tuv");
                put('9', "wxyz");
            }
        }; 
        back(digits, 0, combs, phone, new StringBuffer());
        return combs;
    }

    public void back(String digits, int index, List<String> combs, Map<Character, String> phone, StringBuffer com){
        if(index == digits.length()){
            combs.add(com.toString());
        }else{
            for(int i=0; i<phone.get(digits.charAt(index)).length(); i++){
                com.append(phone.get(digits.charAt(index)).charAt(i));
                back(digits, index+1, combs, phone, com);
                com.deleteCharAt(index);
            }
        }
    }
}
// @lc code=end

