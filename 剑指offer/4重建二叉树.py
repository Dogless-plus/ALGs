# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 思路：递归构造。每次的构造范围为 left-root,root-right。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or len(pre) == 0 or len(pre) != len(tin): return None
        if len(pre) ==1:return TreeNode(pre[0])
        root_val = pre[0]
        idx = tin.index(root_val)
        node = TreeNode(root_val)
        node.left = self.reConstructBinaryTree(pre[1:idx+1],tin[:idx])
        node.right = self.reConstructBinaryTree(pre[idx+1:],tin[idx+1:])
        return node