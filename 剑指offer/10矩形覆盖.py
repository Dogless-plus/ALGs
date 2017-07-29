
# 2n矩形覆盖 
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 思路：数学归纳法。斐波那契，由前两个推导。

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number <= 0: return  0 # undefined
        elif number < 3: return number
        x, y = 1, 2
        for _ in range(3, number+1):
            x, y = y, x+y
        return y