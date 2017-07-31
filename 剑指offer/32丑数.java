
// 丑数

// 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
// 思路：三个指针前向探索取最小，都是自己的倍数。向前推进，不再取回旧值。

class Solution {
    public int GetUglyNumber_Solution(int index) {
        if (index == 0) return 0;
        if (index == 1) return 1;
        int [] dp = new int [index+1];
        dp[1] = 1;
        int i = 1 , j = 1, k=1;
        for (int m = 2; m<= index;m++){
            dp[m] = Math.min(Math.min(dp[i]*2,dp[j]*3),dp[k]*5);
            if (dp[i] * 2 == dp[m]) i++;
            if (dp[j] * 3 == dp[m]) j++;
            if (dp[k] * 5 == dp[m]) k++;
        }
        return dp[index];
    }
}