B、字符串按低位排序

思路：利用**稳定的**键索引计数法进行排序，从低位到高位一位一位地排。

注意：计数桶用ASCII码的256个值就够了。一定要稳定，不然按位进行排序就可能出错了。线性复杂度。

应用：老式的卡片打孔机。车牌号排序。

```python
# coding=utf-8

class LSD:
    def __init__(self, data):
        self.data = data  # 浅引用
        self.N = len(data)
        self.S = len(data[0])
        self.R = 256  # 计数器的数量
        self.aux = [""] * self.N
        self.sort()

    def sort_one(self, position):
        counter = [0] * (self.R + 1)
        for v in self.data:  # 频率计数器，放到下一个位置
            idx = ord(v[position])
            counter[idx + 1] += 1  # 注意是下一个位置
        for r in range(self.R):  # 构造各个类的位置起点
            counter[r + 1] += counter[r]
        for i, v in enumerate(self.data):
            idx = ord(v[position])
            self.aux[counter[idx]] = v  # 根据基础位置压入辅助数组
            counter[idx] += 1
        # self.data = self.aux[:]  # 深拷贝方式
        for i in range(self.N):  # 原地方式
            self.data[i] = self.aux[i]

    def sort(self):
        for i in list(range(self.S))[::-1]:
            self.sort_one(i)
        return self


data = ["4PGC938", "2IYE230", "3CI0720", "1ICK750", "1OHV845", "4JZY524", "1ICK750",
        "3CI0720", "1OHV845", "1OHV845", "2RLA629", "2RLA629", "3ATW723"]

print(LSD(data).data)
print(data)  # 查看是否原地
```