
// 数组中只出现一次的数字
// 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
// 思路：流过set类型。若另一题只有一个不同的数字，可以用异或xor。

import java.util.HashSet;import java.util.Set;

class Solution {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        Set <Integer> set = new HashSet<>();
        for (int x: array){
            if (set.contains(x)) set.remove(x);
            else set.add(x);
        }
        Integer [] n12 = set.toArray(new Integer[0]);
        num1[0] = n12[0];
        num2[0] = n12[1];
    }
}