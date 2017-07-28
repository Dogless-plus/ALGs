// 斐波那契
// 思路：使用两个缓存，使用循环而非递归。


public class Solution {
    public int Fibonacci(int n) {
        if (n <= 0 || n > 39) return 0; // undefined
        if (n == 1 || n == 2) return 1;
        int x = 1, y =1 ,tmp;
        for (int i =3 ; i <= n ;i++){
            tmp = x+y;
            x = y;
            y = tmp;
        }
        return y;
    }
}
