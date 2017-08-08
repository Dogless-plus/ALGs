// 机器人的运动范围
// 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
// 思路：创建网格，模拟走一走就好了。注意，只需要向下和向右走，因为左上只能更小,而且也没有障碍物。

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        self.grid = [[1 if self.is_availabe(row, col) else 0 for col in range(cols)] for row in range(rows)]
        self.count = 0
        self.dfs(0,0)
        return self.count

    def is_availabe(self, x, y):
        return sum(int(xi) for xi in str(x) + str(y)) <= self.threshold

    def dfs(self, m, n):
        if self.grid[m][n] == 1:
            self.count += 1
            self.grid[m][n] = 0
            return m < self.rows - 1 and self.dfs(m + 1, n), n < self.cols - 1 and self.dfs(m, n + 1)
        else:
            return