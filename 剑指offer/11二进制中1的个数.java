
// 二进制表示中1的个数
// 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
// 思路： 利用位操作，不断消去1。


public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        while (n != 0){
            n = n&(n-1);  //消掉末尾的1，数数消的次数
            count ++ ;
        }
        return count;
    }
}
