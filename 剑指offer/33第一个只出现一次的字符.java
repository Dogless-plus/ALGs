
// 第一个只出现一次的字符。
// 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
// 思路：访问两遍。第一遍用hashmap记录次数，第二遍找到位置。或者python中可以在字典中嵌套列表直接找哪些只有一个值的位置。而从后向前set的思路是错误的。

import java.util.HashMap;
public class Solution {
    public int FirstNotRepeatingChar(String str) {
        if (str == null || str.length() == 0) return -1;
        char [] chars = str.toCharArray();
        HashMap <Character,Integer> map = new HashMap<>();
        for (int i =0  ; i < chars.length; i++) {
            if (map.containsKey(chars[i])) map.put(chars[i],map.get(chars[i])+1);
            else map.put(chars[i],1);
        }
        for (int i =0 ; i < chars.length; i++){
            if (map.get(chars[i]) == 1) return i;
        }
        return -1;
    }
}