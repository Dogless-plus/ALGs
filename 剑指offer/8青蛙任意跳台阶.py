# 青蛙跳台阶方案数，任意级。
# 思路：数学归纳。插空法多个，杨辉三角，完全二项展开。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number <= 0 :return 0
        ret = 1
        for _ in range(2,number+1):
            ret *= 2
        return ret