 C.��λ�����㷨

���⣺�����ݲ��ǵȳ��ģ���ô��λ�����㷨ʧЧ��

˼·����Ȼʹ��"������������"���Ӹ�λ����λ�ȶ��ؽ��м�������ʹ��R+2�Ĵ洢������λ��1��������Щ�Ѿ���ĩβ���ַ������м�����������Щ�����Ǵ������ȡ��ڶ�ÿλ��������ʱ���൱�ڻ����˿��ŵĲ�ͬpartition��Ȼ���ڸ���partition����Ȼ��Ҫ����һλ������һ��partition�е����ݽ�С��Ӧ�ø��ò���������Ϊ�������partition�ٴ�ʹ��"������"�Ŀ����ܴ�ԶԶ�������������������ÿһλ���ǵ�ֵ������ô��������"������"��

���Ӷȣ�O(NlogN / logR)����N��С��ʱ��R�Ŀ����ͱȽϴ��ˡ�

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
            return -1  # ��ʱ��ŵ�counter��1λ��
        return ord(self.data[data_i][loc])

    def msd(self, data_lo, data_hi, loc):
        counter = [0] * (self.R + 2)  # ��������˽�еģ����ܹ�����Ȼ�ڵݹ��ʱ��Ḳ�� 
        # ��lo��hi����������
        if data_hi - data_lo < self.threshold:  # ������Сʱ���ã��ȶ��ģ���������
            return
            # self.insertion_sort()
        for i in range(data_lo, data_hi + 1):  # Ƶ�ʼ��������ŵ���һ��λ��
            idx = self.get_loc(i, loc) + 2
            counter[idx] += 1  # ע������һ��λ��
        for r in range(self.R + 1):  # ����������λ�����
            counter[r + 1] += counter[r]
        for i in range(data_lo, data_hi + 1):
            idx = self.get_loc(i, loc) + 1
            self.aux[counter[idx]] = self.data[i]  # ���ݻ���λ��ѹ�븨������
            counter[idx] += 1
        for i in range(data_lo, data_hi + 1):  # ������ȥ
            self.data[i] = self.aux[i - data_lo]  # ������ǰ���ˣ���Ϊcounter���������ͳ��data_lo��data_hi֮���
        for i in range(self.R):  # ���ƿ��ţ���locλ���ź����зֿ���ÿ��С�鰴loc+1��λ������
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