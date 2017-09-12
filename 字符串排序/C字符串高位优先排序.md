 C.高位优先算法

问题：若数据不是等长的，那么低位优先算法失效。

思路：仍然使用"键索引计数法"，从高位到低位稳定地进行键索引。使用R+2的存储，其中位置1用来对那些已经到末尾的字符串进行计数，这样这些数据是处于优先。在对每位进行排序时，相当于划分了快排的不同partition，然后在各个partition中仍然需要对下一位排序，若一个partition中的数据较小，应该改用插入排序。因为若对这个partition再次使用"键索引"的开销很大，远远不如插入排序。最坏的情况是每一位都是等值键，那么总是启用"键索引"。

复杂度：O(NlogN / logR)，当N较小的时候，R的开销就比较大了。

```python
# coding=utf-8

class MSD:
    def __init__(self, data):
        self.R = 256
        self.threshold = 0
        self.data = data
        self.N = len(data)
        self.aux = [""] * self.N
        self.msd(0, self.N - 1, 0)

    def get_loc(self, data_i, loc):
        if loc >= len(self.data[data_i]):
            return -1  # 到时候放到counter的1位置
        return ord(self.data[data_i][loc])

    def msd(self, data_lo, data_hi, loc):
        counter = [0] * (self.R + 2)  # 计数器是私有的，不能共享，不然在递归的时候会覆盖 
        # 第lo到hi个数据排序
        if data_hi - data_lo < self.threshold:  # 数据量小时改用（稳定的）插入排序
            return
            # self.insertion_sort()
        for i in range(data_lo, data_hi + 1):  # 频率计数器，放到下一个位置
            idx = self.get_loc(i, loc) + 2
            counter[idx] += 1  # 注意是下一个位置
        for r in range(self.R + 1):  # 构造各个类的位置起点
            counter[r + 1] += counter[r]
        for i in range(data_lo, data_hi + 1):
            idx = self.get_loc(i, loc) + 1
            self.aux[counter[idx]] = self.data[i]  # 根据基础位置压入辅助数组
            counter[idx] += 1
        for i in range(data_lo, data_hi + 1):  # 拷贝回去
            self.data[i] = self.aux[i - data_lo]  # 数据在前面了，因为counter里的数据量统计data_lo到data_hi之间的
        for i in range(self.R):  # 类似快排，在loc位置排好了切分开，每个小组按loc+1的位置排序
            delta = counter[i + 1] - counter[i]
            if delta < 2: continue
            self.msd(data_lo + counter[i], data_lo + counter[i + 1] - 1, loc + 1)


def case():
    data = ["she", "sells", "seashells", "by", "the", "seahore",
            "the", "shells", "she", "sells", "are", "surely", "seashells"]
    MSD(data)
    print(data)


case()
```