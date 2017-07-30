
// 镜像二叉树。
// 思路： 递归求镜像。左右互换。

class TreeNode {
 int val = 0;
 TreeNode left = null;
 TreeNode right = null;

 public TreeNode(int val) {
 this.val = val;}
 }

class Solution {
    public void Mirror(TreeNode root) {
        if (root == null) return;
        Mirror(root.left);
        Mirror(root.right);
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
    }
}