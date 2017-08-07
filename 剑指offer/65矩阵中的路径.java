
// 矩阵中的路径
// 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
// 思路，遇到合适的位置进行dfs寻找，到达字符串末尾即成功，每次使用一个临时空间来屏蔽已经访问过的路径。注意重新初始化。

class Solution {
    private char[] matirx = null;
    private int rows;
    private int cols;
    private char[] str = null;
    private int[] grid = null; // 用于搜索的临时空间,用于屏蔽路径

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
        if (str == null || str.length == 0) return true;
        if (matrix == null || rows <= 0 || cols <= 0 || str.length > rows * cols) return false;
        this.matirx = matrix;
        this.rows = rows;
        this.cols = cols;
        this.str = str;
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                if (matrix[cord_2_line(i, j)] == str[0]) {
                    this.grid = null; // 重新初始化临时空间
                    this.grid = new int[matrix.length];
                    if (dfs(i, j, 0)) return true;
                }
        return false;
    }

    private int cord_2_line(int i, int j) {
        return i * this.cols + j;
    }

    private boolean dfs(int i, int j, int k) { // 至顶向底传递已遍历长度
        if (k >= str.length) return true;
        if (i < 0 || j < 0 || i >= rows || j >= cols ||
                this.grid[cord_2_line(i, j)] == 1 || this.matirx[cord_2_line(i, j)] != str[k]) return false;
        this.grid[cord_2_line(i, j)] = 1;
        return dfs(i - 1, j, k + 1) || dfs(i + 1, j, k + 1) || dfs(i, j - 1, k + 1) || dfs(i, j + 1, k + 1);
    }
}