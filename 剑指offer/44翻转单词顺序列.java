
// 翻转单词顺序列
// 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
// 思路：分割，翻转。注意，java中的split函数不支持像python一样的多空格自动处理,需要先trim一下。


public class Solution {
    public String ReverseSentence(String str) {
        if (str == null || str.trim().length() <2) return str;
        String [] sp = str.split(" ");
        StringBuilder sb = new StringBuilder(sp.length);
        for (int i = sp.length -1 ;i >=0 ;i--){
            sb.append(sp[i]);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}