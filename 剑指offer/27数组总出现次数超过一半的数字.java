
// 数组中出现次数超过一半的数字。
// 思路：使用一个哈希表做成Counter即可。

import java.util.HashMap;
public class Solution {
    public int MoreThanHalfNum_Solution(int [] array) {
        if (array == null || array.length == 0) return 0;
        HashMap <Integer,Integer> map = new HashMap<>();
        for (int x: array){
            if (map.containsKey(x)) {map.put(x,map.get(x) +1);}
            else {map.put(x,1);}
        }
        int threshold = array.length / 2;
        for (int key : map.keySet()) if (map.get(key) > threshold) return key;
        return 0;
    }
}