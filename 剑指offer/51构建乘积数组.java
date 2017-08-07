// 构建乘积数组
// 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
// 思路：直接使用平方级复杂度构建即可。
// 思路2：使用两个数组存储，左扫描一遍乘出左边结果，右扫描一遍乘出右边结果。线性复杂度。

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        B = []
        if not A or len(A) ==0 :return B
        for i in range(len(A)):
            B.append(reduce(lambda a,b : a*b, A[:i]+A[i+1:]))
        return B


import java.util.ArrayList;
public class Solution {
    public int[] multiply(int[] A) {
        if (A == null || A.length <2) return null;
        int [] ret = new int [A.length];
        for (int i = 0; i< A.length ;i ++){
            int value =1;
            for (int j = 0;j< A.length;j++){
                if (i !=j ) value *= A[j];  
            }
            ret[i] = value;
        }
        return ret;
    }
}

class Solution {
    public int[] multiply(int[] A) {
        if (A == null || A.length < 2) return null;
        int[] left = new int[A.length];
        int[] right = new int[A.length];
        int tmp = 1;
        left[0] = tmp;
        for (int i = 1; i < A.length; i++) {
            tmp *= A[i - 1];
            left[i] = tmp;
        }
        tmp = 1;
        right[A.length - 1] = 1;
        for (int j = A.length - 2; j >= 0; j--) {
            tmp *= A[j + 1];
            right[j] = tmp;
        }
        for (int i = 0; i < left.length; i++) {
            left[i] *= right[i];
        }
        return left;
    }
}