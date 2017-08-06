
// 判断平衡二叉树
// 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
// 思路：向下传递深度，平衡需要各个子树平衡，分支的深度设为左右中的较大值。


public class Solution {
    private boolean status = true;
    public boolean IsBalanced_Solution(TreeNode root) {
        if (root == null) return true;
        dfs(root,0);
        return status;
    }
    private int dfs(TreeNode root, int depth){
        if (!status || root == null) return depth;  // fail agilely
        int left = dfs(root.left,depth) + 1;
        int right = dfs(root.right,depth) +1;
        int min = Math.min(left,right);
        int max = Math.max(left,right);
        if (max - min > 1) this.status = false;
        return max;
    }
}