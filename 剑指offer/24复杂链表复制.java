
// 复杂链表复制
// 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
// 思路：利用哈希表来记录random指向。注意使用一个头结点。

import java.util.HashMap;
/*
public class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}
*/
public class Solution {
    public RandomListNode Clone(RandomListNode pHead)
    {
        if (pHead == null) return null;
        HashMap <RandomListNode,RandomListNode> map = new HashMap<>();
        RandomListNode prehead = new RandomListNode(-1);
        RandomListNode p = pHead,q=prehead;
        while ( p!=null ){
            q.next = new RandomListNode(p.label);
            q = q.next;
            map.put(p,q);
            p = p.next;
        }
        p = pHead;
        while (p != null){
            if (p.random != null) map.get(p).random = map.get(p.random);
            p = p.next;
        }
        return prehead.next;
    }
}