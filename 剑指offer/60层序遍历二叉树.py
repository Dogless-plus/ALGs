# 层序遍历二叉树
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# 思路：通过layers，基于上一层打印下一层。

class Solution:
    # 返回二维列表[[1,2],[4,5]]
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
        for layer in layers:
            ret.append([p.val for p in layer])
        return ret