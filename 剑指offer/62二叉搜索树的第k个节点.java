// 二叉搜索树的第k个节点
// 给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
// 思路：BST满足左小右大，使用中序遍历即可。注意悬挂全局计数器和全局返回，并且敏捷成功。

class Solution {
    int k = 0;
    TreeNode ret = null;
    TreeNode KthNode(TreeNode pRoot, int k) {
        this.k = k - 1;
        dfs(pRoot);
        return ret;
    }

    private void dfs(TreeNode root) {
        if (root == null || ret != null) return; // success agiley
        dfs(root.left);
        if (k == 0) {
            ret = root;
        }
        k--;
        dfs(root.right);
    }
}