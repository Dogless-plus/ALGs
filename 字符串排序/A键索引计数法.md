������������

˼·��ÿ�����ȼ����ÿ�ʼλ�ã����������ݸ��������ʼλ�á�

```python
# coding =utf-8


def index_sort(data):
    values, weights = zip(*data)
    max_weight = max(weights)
    counter = [0] * (max_weight + 2)
    for value, weight in data:  # �����������ں���һ��λ���ϡ�ÿ��λ�ö���һ�����ȼ�������
        counter[weight + 1] += 1
    for i in range(max_weight+1): # �ں���һλ������һλ�����ȼ��������ޣ�����һλ�Ŀ�ʼλ��
        counter[i+1] += counter[i]
    aux = [0] * len(data)
    for value, weight in data:
        aux[counter[weight]] = value  # �ڿ���λ�ô���������
        counter[weight] += 1  # ���¿��õĿ�ʼλ��
    print(aux)
    print(counter)


data = [('A', 2),
        ('B', 3),
        ('C', 3),
        ('D', 4),
        ('E', 1),
        ('F', 3),
        ('G', 4),
        ('H', 3),
        ('I', 1),
        ('J', 2),
        ('K', 2),
        ('L', 1),
        ('M', 2),
        ('N', 4),
        ('O', 3),
        ('P', 4),
        ('Q', 4),
        ('R', 2),
        ('S', 3),
        ('T', 4)]

index_sort(data)
```