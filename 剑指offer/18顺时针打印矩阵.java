// 顺时针打印矩阵
// 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
// 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
// 思路：剑指offer上固然有很多种方法，巧妙的设计。下面使用的屏蔽法，依靠方向转换，可能适用性更强一些。

public ArrayList<Integer> printMatrix(int [][] matrix) {
        // Integer.MIN_VALUE is in blacklist
        ArrayList <Integer> ret = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length ==0) return ret;
        int count = 0;
        int x = 0, y = 0;
        int M = matrix.length, N = matrix[0].length;
        int direction = 0;
        while (count < M*N){
            if (matrix[x][y] != Integer.MIN_VALUE) { // 由最后的3变0引起的，状态穿透问题，需要判断一下『当前是否可用』
                // 或者也可以在判断条件里修改当前
                count++;
                ret.add(matrix[x][y]);
                matrix[x][y] = Integer.MIN_VALUE;}
            if (direction == 0) { // right
                if (y+1 < N && matrix[x][y+1] != Integer.MIN_VALUE) {y++;}
                else {direction = 1;}
            }
            if (direction == 1) { // down
                if (x+1 < M && matrix[x+1][y] != Integer.MIN_VALUE) {x++;}
                else {direction = 2;}
            }
            if (direction == 2) { // left
                if (y > 0  && matrix[x][y-1] != Integer.MIN_VALUE) {y--;}
                else {direction = 3;}
            }
            if (direction == 3) { // left
                if (x > 0  && matrix[x-1][y] != Integer.MIN_VALUE) {x--;}
                else {direction = 0;}
            }
        }
        return ret;
    }