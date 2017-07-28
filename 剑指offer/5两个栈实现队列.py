#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 思路：正常push，pop时用另一个栈来倒腾，实现FIFO

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []   # instance fields
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if not self.stack1 : raise 
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ret