
# n个自然数中1的个数
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
# 思路1：遍历
# 思路2：
# 我们从低位到高位求每位1出现的次数，累加求和即可
# 例如：求0~abcde中1的个数，现在我们求c这一位中1出现的次数，其他位雷同
# 有两部分组成
#   第一部分：ab * 100，表示当ab这两位在0~ab-1范围内时，de可以从0~99取值
#   第二部分：如果c>1时，当ab为ab时1的个数为0~99
#           如果c=1时，当ab为ab时1的个数为de + 1
#           如果c<0时，当ab为ab是1的个数为0


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(n+1):
            print(str(n))
            count += str(i).count("1")
        return count


public class Solution {
    public int NumberOf1Between1AndN_Solution(int n) {
        int count = 0;
        int base = 1;
        while (n >= base){
            count += n / (base * 10) * base;
            if (n % (base * 10) / base > 1) count += base;
            else if (n % (base * 10) / base == 1) count += (n % base) + 1;
            base *= 10;
        }
        return count;
    }
}