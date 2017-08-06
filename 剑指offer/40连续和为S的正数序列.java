// 连续和为S的正数序列
// 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
// 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
// 思路：利用等差和整除关系。 s = (m+n)(m-n+1)/2

import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        if (sum <= 0) return null;
        ArrayList <ArrayList<Integer>> ret = new ArrayList<>();
        int sum2 = sum*2;
        for (int n = 1 ; n * n <= sum2 ;n++){
            if (sum2 % n != 0) continue;
            int m = sum2 / n;
            if ((m+n -1) %2 == 1 || (m-n +1)%2 ==1 ) continue;
            int a = (m+n-1) / 2;
            int b = (m-n+1) /2;
            if (a == b) continue;
            ArrayList <Integer> layer = new ArrayList<>();
            for (int i = b ; i<= a; i++) layer.add(i);
            ret.add(layer);
        }
        ArrayList <ArrayList<Integer>> ret2 = new ArrayList<>();
        for (int i = ret.size()-1; i > -1;i--) ret2.add(ret.get(i));
        return ret2;
    }
}