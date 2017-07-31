
// 二叉树构造双向链表
// 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
// 思路：leaf和realroot都设为最左端。使用中序遍历构造。


class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }
}

TreeNode leaf = null;
    TreeNode realroot = null;

    public TreeNode Convert(TreeNode pRootOfTree) {
        dfs(pRootOfTree);
        return realroot;
    }

    public void dfs(TreeNode root) {
        if (root == null) return;
        dfs(root.left);
        if (leaf == null) {
            leaf = root;
            realroot = root;
        } else {
            leaf.right = root;
            root.left = leaf;
            leaf = root;
        }
        dfs(root.right);
    }