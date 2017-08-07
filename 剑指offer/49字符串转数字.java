
// 字符串转数字
// 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
// 思路，考虑正负号，考虑去掉正负号之后的长度，考虑每位是否可转。python有ord函数，chr函数。

public int StrToInt(String str) {
        if (str == null || str.length() ==0) return 0;
        char [] ss = str.toCharArray();
        int flag = 1;
        boolean status = false;
        if (ss[0] == '+') {ss[0] = '0';status = true;}
        else if (ss[0] == '-'){ss[0] = '0'; flag = -1; status =true;}
        if (status && ss.length == 1) return 0;
        int i = ss.length -1 ;
        int base = 1;
        int ret = 0;
        while (0 <= i){
            int v = ss[i] - '0';
            if ( v > 9 || v < 0) return 0;
            ret += base * v;
            base *= 10;
            i--;
        }
        return flag * ret;
    }