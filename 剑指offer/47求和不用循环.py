
# 求和不用循环。
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 思路：用递推，短路结束。注意悬挂一个(堆区)全局量，不要悬挂一个栈区量，注意这题java不好做，改用其他语言。


# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        value = [0,]
        def apply(n):
            value[0] +=n
            n and apply(n-1)
        apply(n)
        return value[0]