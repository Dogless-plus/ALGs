
// 不用加减乘除做加法。
// 思路：异或求和，按位与左移做carry。注意值的覆盖问题。

public int Add(int num1,int num2) {
        while (num2 != 0){
            int sum = num1 ^ num2;
            num2 = (num1 & num2)  <<1;
            num1 = sum;
        }
        return num1;
    }