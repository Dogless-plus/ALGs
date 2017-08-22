# coding=utf-8

#coding=utf-8
# 尝试一下可读性差和效率都差的代码

from functools import partial
from collections import Counter

distance = lambda x, y: sum(map(lambda a, b: (a - b) ** 2, x, y))
nearest_k = lambda test, train_x, k=1: list(
    zip(*
        sorted(
            map(lambda a:
                (a[0], (partial(
                    distance, y=test)(a[1]))),
                enumerate(train_x)),
            key=lambda x: x[1],
            reverse=False)))[0][:k]
predict = lambda test, train_x, train_y, k=1: sorted(
    Counter(train_y[idx] for idx in nearest_k(test, train_x, k)).items(),
    key=lambda x: x[1],
    reverse=True)[0][0]

train_xy = [((2.1, 3.0), 1.0), ((1.2, 3.3), 1.0), ((1.2, 1.5), -1.0),
            ((-1.6, 1.5), 1.0), ((1.4, 2.3,), -1.0), ((1.6, 1.7), 1.0)]
print(predict((0.3, 0.0), *zip(*train_xy), 3))
