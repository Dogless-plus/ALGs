B���ַ�������λ����

˼·������**�ȶ���**�������������������򣬴ӵ�λ����λһλһλ���š�

ע�⣺����Ͱ��ASCII���256��ֵ�͹��ˡ�һ��Ҫ�ȶ�����Ȼ��λ��������Ϳ��ܳ����ˡ����Ը��Ӷȡ�

Ӧ�ã���ʽ�Ŀ�Ƭ��׻������ƺ�����

```python
# coding=utf-8

class LSD:
    def __init__(self, data):
        self.data = data  # ǳ����
        self.N = len(data)
        self.S = len(data[0])
        self.R = 256  # ������������
        self.aux = [""] * self.N
        self.sort()

    def sort_one(self, position):
        counter = [0] * (self.R + 1)
        for v in self.data:  # Ƶ�ʼ��������ŵ���һ��λ��
            idx = ord(v[position])
            counter[idx + 1] += 1  # ע������һ��λ��
        for r in range(self.R):  # ����������λ�����
            counter[r + 1] += counter[r]
        for i, v in enumerate(self.data):
            idx = ord(v[position])
            self.aux[counter[idx]] = v  # ���ݻ���λ��ѹ�븨������
            counter[idx] += 1
        # self.data = self.aux[:]  # �����ʽ
        for i in range(self.N):  # ԭ�ط�ʽ
            self.data[i] = self.aux[i]

    def sort(self):
        for i in list(range(self.S))[::-1]:
            self.sort_one(i)
        return self


data = ["4PGC938", "2IYE230", "3CI0720", "1ICK750", "1OHV845", "4JZY524", "1ICK750",
        "3CI0720", "1OHV845", "1OHV845", "2RLA629", "2RLA629", "3ATW723"]

print(LSD(data).data)
print(data)  # �鿴�Ƿ�ԭ��
```