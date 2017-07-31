
# 二叉树中和为某一值的路径
# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# 思路：使用layer存储一层一层往下寻找。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# -*- coding:utf-8 -*-
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root : return []
        ret = []
        layer = [[root,],]
        while len(layer):
            new_layer = []
            for path in layer:
                node = path[-1]
                if not node.left and not node.right and expectNumber == sum(n.val for n in path):
                    ret.append([n.val for n in path])
                if node.left:
                    new_layer.append(path+[node.left])
                if node.right:
                    new_layer.append(path+[node.right])
            layer = new_layer
        return sorted(ret)