# 青蛙跳台阶，可跳1级或2级。求方案数
# 思路：这一级是从上一级或者上二级过来。是斐波那契
# 另一题：跳三级，也是一样的。缓存三个值。
# 另一题：可以跳任意级。那么考虑1 - n-1种插空法。有 2 的n-1次方中，恰好是第n-1层的杨辉三角求和，即二项完全展开。


def jumpFloor(self, number):
    if number <= 0: return 0
    if number == 1: return 1
    x = y = 1
    for _ in range(2, number + 1):
        x, y = y, x + y
    return y