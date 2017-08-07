
// 中序遍历的下一个节点。
// 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
// 思路：观察多种情况。发现，若有右子树，则是右子树的最左节点，若无右子树，则是父节点，且当前节点处于该父节点的左树中。

/*
public class TreeLinkNode {
    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;

    TreeLinkNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public TreeLinkNode GetNext(TreeLinkNode pNode)
    {
        if (pNode == null) return null;
        if (pNode.right != null ){ //若有右子树，则是右子树的最左节点
            TreeLinkNode node= pNode.right;
            while (node.left != null) node = node.left;
            return node;
        }
        while (pNode.next != null) { //若无右子树，则是父节点，且当前节点处于该父节点的左树中
            if (pNode.next.left == pNode) return pNode.next;
            pNode = pNode.next;
        }
        return null;
    }
}