
//请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

public class Solution {
    public String replaceSpace(StringBuffer str) {
        StringBuilder sb = new StringBuilder();
        for (char x :str.toString().toCharArray()) sb.append((x == ' ')? "%20":x);
        return sb.toString();
    }
}