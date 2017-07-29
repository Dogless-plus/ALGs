
// 树的子结构。
// 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
// 思路：递归判断dfs。 注意边界输入，注意子结构可以是树的中部，不必尾部。

// solution1
public class Solution {
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if (root2 == null) return false;  // undefined
        if (root1 == null) return false;
        if (root1.val == root2.val && dfs_both(root1,root2)) return true; // lazy evaluation
        return HasSubtree(root1.left,root2) || HasSubtree(root1.right,root2);
    }
    
    public boolean dfs_both(TreeNode root1,TreeNode root2){
        if (root2 == null) return true;
        if (root1 == null || root1.val != root2.val) return false;
        return dfs_both(root1.left,root2.left) && dfs_both(root1.right,root2.right);
    }
}