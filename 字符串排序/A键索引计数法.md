键索引计数法

思路：每个优先级设置开始位置，对于新数据更新这个开始位置。

```python
# coding =utf-8


def index_sort(data):
    values, weights = zip(*data)
    max_weight = max(weights)
    counter = [0] * (max_weight + 2)
    for value, weight in data:  # 计数器，放在后面一个位置上。每个位置对上一个优先级计数。
        counter[weight + 1] += 1
    for i in range(max_weight+1): # 在后面一位设置这一位（优先级）的上限，即后一位的开始位置
        counter[i+1] += counter[i]
    aux = [0] * len(data)
    for value, weight in data:
        aux[counter[weight]] = value  # 在可用位置处存入数据
        counter[weight] += 1  # 更新可用的开始位置
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