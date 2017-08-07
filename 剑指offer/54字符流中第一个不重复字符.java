
// 字符流中第一个不重复字符。
// 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符流没有存在出现一次的字符，返回#字符。
// 思路：使用顺序队列和一个历史哈希表。插入时检查哈希表中若有则不用添加了，继续检查若队列里有则将当前值添加到哈希历史（注意不是添加前一个而是当前，先不要管前一个）。取第一个时，从头开始取检查有效性，若在哈希表中那么抛弃这个值重新取即可。
// 这里是『逆向思维』，一般的思维是从头到尾添加到哈希表，这里用从尾部添加。


import java.util.ArrayList;
import java.util.HashSet;

public class Solution {
    ArrayList <Character> array = new ArrayList<>();
    HashSet <Character> set = new HashSet<>();
    //Insert one char from stringstream
    public void Insert(char ch)
    {
        if (set.contains(ch)) return;
        for (char x: array) if (x == ch) {set.add(x);return;}
        array.add(ch);
    }
    //return the first appearence once char in current stringstream
    public char FirstAppearingOnce()
    {
        while (!array.isEmpty()){
            char x = array.get(0);
            if (set.contains(x)) array.remove(0);
            else return x;
        }
        return '#';
    }
}