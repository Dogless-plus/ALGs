
# 是否BST后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 思路：最后一个节点是根节点。分成两块，递归判断。


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence: return False
        return self.very(sequence)
        
    def very(self,sequence):
        if not sequence or len(sequence) <= 2:return True
        root = sequence[-1]
        split = 0
        for i in range(len(sequence)-1,-1,-1):
            split = i
            if (sequence[split] < root): break
        for v in sequence[:split]:
            if v > root:
                return False
        return self.very(sequence[:split+1]) \
               and self.very(sequence[split+1:len(sequence)-1])