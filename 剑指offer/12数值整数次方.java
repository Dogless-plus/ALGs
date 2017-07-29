
// 数值整数次方
// 思路：注意特殊边界未定义。注意有负整数的情况。注意java中的浮点型默认是double而不是float，和其他很多语言是不一样的。


public double Power(double base, int exponent) {
        if (base == 0) return 0.0; // undefined
        if (base == 1 || exponent ==0) return 1.0 ;
        boolean is_negative = false;
        if (exponent < 0) {
            is_negative = true ;
            exponent = (-1) * exponent;
        }
        double value = 1.0;
        for (int i = 1 ; i <= exponent ; i++) value *= base;
        if (is_negative) value = 1.0 / value ; // value wont be 0.0
        return value;
    }