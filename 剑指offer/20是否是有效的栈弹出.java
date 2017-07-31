// 是否是有效的栈弹出
// 思路：模拟栈的压入弹出，不行就false


import java.util.ArrayList;
import java.util.Stack;

public class Solution {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        if (pushA.length != popA.length) return false;
        Stack <Integer> stack = new Stack<>();
        int a  = 0;
        for (int x : popA){
            while ((stack.isEmpty() || stack.peek() != x )) {
                if (a < pushA.length) stack.push(pushA[a++]);
                else return false;}
            if (stack.peek() == x) stack.pop();
        }
        return true;
    }
}