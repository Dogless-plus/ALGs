
// 数组中和为sum的两个数字
// 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
// 对应每个测试案例，输出两个数，小的先输出。
// 思路：前后两个指针夹逼，因为『共振原理』或者『大数定理』，外侧的乘机小。如果是另一个题，无序的Two Sums那题那么可以用一个O(1)的set或者hashmap来查找。


import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList <Integer> ret = new ArrayList<>(2);
        if (array == null || array.length < 2)return ret;
        int left = 0, right = array.length-1;
        while (left < right){
            int tmp = array[left] + array[right];
            if (tmp == sum) {ret.add(array[left]);ret.add(array[right]);return ret;}
            else if (tmp > sum) right--;
            else left ++;
        }
        return ret;
    }
}