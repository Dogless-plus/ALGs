
// 包含min函数的栈
// 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
// 思路：压入一个元组或者使用一个辅助栈来存储min信息。

import java.util.Stack;

public class Solution {
    class Pair{
        Pair(int a, int b){
            this.value = a;this.min =b;}
        int value;
        int min;
    }
    Stack <Pair> stack = new Stack<>();

    public void push(int node) {
        int min = (stack.isEmpty()) ? node : Math.min(stack.peek().min,node);
        stack.push(new Pair(node,min));
    }

    public void pop() {
        if (!stack.isEmpty()) stack.pop();
        else System.out.println("null pop"); // undefined
    }

    public int top() {
        return stack.peek().value;
    }

    public int min() {
        return stack.peek().min;
    }
}