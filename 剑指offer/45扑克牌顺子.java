
// 扑克牌顺子。
// 大小王用0表示。LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。
// 思路：按大小王数量分5钟情况讨论。讨论每个元素是否相等以及最大元素减最小元素差值在4以内。


import java.util.ArrayList;
import java.util.Collections;
public class Solution {
    public boolean isContinuous(int [] numbers) {
        if (numbers.length != 5) return false;
        int king_count = 0;
        ArrayList <Integer> array = new ArrayList<>(5);
        for (int x: numbers){
            if (x == 0) {king_count++;}
            else {array.add(x);}
        }
        if (king_count == 4) return true;
        array.trimToSize();
        Collections.sort(array);
        int [] nums = new int [array.size()];
        for (int i=0 ;i < array.size();i++) nums[i] = array.get(i);
        if (king_count == 3 ) return  ( nums[0] != nums[1] && nums[1] - nums[0] <= 4) ? true : false;
        else if (king_count == 2) return (nums[0] != nums[1] && nums[1] != nums[2] && nums[2]- nums[0] <= 4) ? true :false;
        else if (king_count ==1 ) return (nums[0] != nums[1] && nums[1] != nums[2] && nums[2] != nums[3] && nums[3]- nums[0] <= 4) ? true :false;
        else if (king_count ==0 ) return (nums[0] != nums[1] && nums[1] != nums[2] && nums[2] != nums[3] &&  nums[4] != nums[3] && nums[4]- nums[0] <= 4) ? true :false;
        return false;
    }
}