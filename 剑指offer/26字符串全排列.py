# 字符串全排列。
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 思路：移动层级添加。立方复杂度。

class Solution:
    def Permutation(self, ss):
        if not ss or len(ss) == 1: return ss
        layers = [[ss[0]],]
        for s in ss[1:]:
            new_layers = []
            for layer in layers:
                for i in range(len(layer)+1):
                    new_layers.append(layer[:i]+[s,]+layer[i:])
            layers = new_layers
        layers = ["".join(layer) for layer in layers]
        return sorted(set(layers))