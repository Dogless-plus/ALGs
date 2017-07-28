
//题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
//每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
//思路：从左下角开始，大向上，小向下走。注意空边界。

public class Solution {
    public boolean Find(int target, int [][] array) {
        if (array == null || array.length == 0) return false;
        int M = array.length;
        int N = array[0].length;
        if (N ==0)return false;
        if (target < array[0][0] || target > array[M-1][N-1]) return false;
        int m = M-1, n = 0;
        while (m>=0 && n < N) {
//            System.out.println("in:"+m+","+n+"target:"+target+",current:"+array[m][n]);
            if (target == array[m][n]) return true; // success agilely
            else if (target > array[m][n]) n++;
            else m--;
        }
        return false;
    }
}