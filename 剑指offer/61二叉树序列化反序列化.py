
# 二叉树序列化与反序列化
# 请实现两个函数，分别用来序列化和反序列化二叉树
# 思路：当做满二叉树进行层序遍历（有人喜欢用先序遍历也可以），空的地方已经层间需要分隔符。
# 注意可以运用反向调试技巧: s = "1;2,3;#,4,5,6" ; print(Solution().Serialize(Solution().Deserialize(s)))


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        if not root:return None
        layers = [[root,],]
        while 1:
            parents = layers[-1]
            layer =[]
            status = False
            for p in parents:
                if p == "#":
                    layer.append("#")
                    layer.append("#")
                    continue
                if p.left:
                    layer.append(p.left)
                    status = True
                else:
                    layer.append("#")
                if p.right:
                    layer.append(p.right)
                    status = True
                else:
                    layer.append("#")
            if status:
                layers.append(layer)
            else:
                break
        ret =[]
        for layer in layers:
            ret.append([p.val if p != "#" else "#" for p in layer])
        return ";".join(",".join(map(str,layer)) for layer in ret)

    def Deserialize(self, s):
        if not s:return None
        s = [list(si.split(",")) for si in s.split(";")]
        layers = []
        for si in s:
            layer = []
            for node in si:
                if node == '#':
                    layer.append(None)
                else:
                    layer.append(TreeNode(int(node)))
            layers.append(layer)
        for i in range(len(layers) -1):
            parent_layer = layers[i]
            child_layer = layers[i+1]
            for i,p in enumerate(parent_layer):
                if p:
                    p.left = child_layer[2*i]
                    p.right = child_layer[2*i+1]
        return layers[0][0]









/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
  int index = -1; //计数变量

    String Serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if (root == null) {
            sb.append("#,");
            return sb.toString();
        }
        sb.append(root.val + ",");
        sb.append(Serialize(root.left));
        sb.append(Serialize(root.right));
        return sb.toString();
    }

    TreeNode Deserialize(String str) {
        index++;
        String[] strr = str.split(",");
        TreeNode node = null;
        if (!strr[index].equals("#")) {
            node = new TreeNode(Integer.valueOf(strr[index]));
            node.left = Deserialize(str);
            node.right = Deserialize(str);
        }
        return node;
    }
}