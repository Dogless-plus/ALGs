

// 二叉树的深度
// 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
// 思路：递归dfs(前中后都可以)或者层序遍历。

class Solution {
    public int TreeDepth(TreeNode root) {
        return dfs(root,0);
    }
    private int dfs(TreeNode root, int depth){
        if (root == null) return depth;
        return 1+Math.max(dfs(root.left,depth),dfs(root.right,depth));
    }
}


class Solution {
    public int TreeDepth(TreeNode root) {
        return (root == null) ?  0 :1+Math.max(TreeDepth(root.left),TreeDepth(root.right));
    }
}