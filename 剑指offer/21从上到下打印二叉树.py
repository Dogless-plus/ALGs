
# 从上到下打印二叉树
# 思路：层序遍历，一直根据当前节点添加就好了。如果到底最后节点，结束。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        if not root: return []
        nodes = [root,]
        values = []
        i = 0
        while 1:
            node = nodes[i]
            values.append(node.val)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
            if (i == len(nodes)-1) : break
            i += 1
        return values