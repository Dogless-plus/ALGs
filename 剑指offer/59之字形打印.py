
# 之字形打印二叉树。
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
# 思路：使用layers层序遍历。每层基于上一层。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:return []
        layers = [[pRoot,],]
        while 1:
            parents = layers[-1]
            layer =[]
            for p in parents:
                if p.left:
                    layer.append(p.left)
                if p.right:
                    layer.append(p.right)
            if layer:
                layers.append(layer)
            else:
                break
        ret =[]
        for i, layer in enumerate(layers):
            if i % 2 == 0:
                ret.append([p.val for p in layer])
            else:
                ret.append([p.val for p in layer[::-1]])
        return ret