# coding=utf-8

from copy import deepcopy


class NaiveBayes:
    def __init__(self):
        self._x = None  # 内部存储的训练集特征x
        self._y = None  # 内部存储训练集标签y
        self.dimension = None  # 特征维度
        self.shape = None  # 训练数据x的形状
        self._tags = None  # 可选的tag类别
        self._condition_probability = None  # 条件概率 # {feature_idx:{tag_y:{feature_value:probability}}}
        self._prior_probability = None  # 先验概率  # {y:probability}
        self._feature_value_sets = None  # 每个特征的取值范围 # {feature_idx:{values set}}
        pass

    def _check(self):
        """ 检查数据合法性，不符合条件就raise
        """
        if len(self._y) != self.shape[1]:
            raise ValueError("length of x and y not match")
        for i, xi in enumerate(self._x):
            if len(xi) != self.dimension:
                raise ValueError("data_%s:%s not much the dimension" % (i, xi))

    def _mk_feature_map(self):
        """ 构建先验概率字典，以及条件概率字典
        """
        features = list(zip(*self._x))
        self._prior_probability = {tag: 0.0 for tag in self._tags}  # {y:probability}
        self._condition_probability = {}  # {feature_idx:{tag_y:{feature_value:probability}}}
        self._feature_value_sets = {}  # {feature_idx:{values set}}
        for i, feature in enumerate(features):
            feature_value_set = set(feature)
            self._feature_value_sets[i] = feature_value_set
            # 拉普拉斯平滑
            y_dict = {tag: {v: 1.0 for v in feature_value_set} for tag in self._tags}
            for xi, yi in zip(feature, self._y):
                y_dict[yi][xi] += 1
            for tag in self._tags:
                tag_dict = y_dict[tag]  # shallow copy
                s = float(sum(tag_dict.values()))
                for key in tag_dict:
                    tag_dict[key] /= s
            self._condition_probability[i] = y_dict
        for yi in self._y:
            self._prior_probability[yi] += 1
        for key in self._prior_probability:
            self._prior_probability[key] /= self.shape[1]

    def fit(self, x, y):
        """ 拟合数据
        :param x: list<d-dimension obj tuple>训练数据集的特征
        :param y: list<obj>训练数据集的监督值
        """
        self._x = deepcopy(x)
        self._y = deepcopy(y)
        self.dimension = len(self._x[0])
        self.shape = self.dimension, len(self._x)
        self._check()
        self._tags = list(set(self._y))
        self._mk_feature_map()

    def _get_post_probability(self, x, tag):
        """ 计算后验概率
        :param x: tuple< obj> 测试数据样本点
        :param tag: obj 监督标签
        :return: float 后验概率
        """
        value = self._prior_probability[tag]
        for i in range(self.dimension):
            if x[i] not in self._feature_value_sets[i]: raise ValueError("not such value")
            value *= self._condition_probability[i][tag][x[i]]
        return value

    def predict(self, x):
        """ 输出预测标签
        :param x: tuple< obj> 测试数据样本点
        :return: obj 监督标签
        """
        if len(x) != self.dimension: raise ValueError("length not match")
        max_tag, max_post = self._tags[0], -1.0
        for tag, post in [(tag, self._get_post_probability(x, tag)) for tag in self._tags]:
            if post > max_post:
                max_tag = tag
                max_post = post
        return max_tag


def case():
    """ 测试用例
    :return:
    """
    import pandas as pd
    filename = "train2.csv"
    df = pd.read_csv(filename,
                     header=0,
                     encoding="utf-8",
                     sep=",").as_matrix()
    xs, ys = [], []
    for line in df:
        xs.append(tuple(line[:-1]))
        ys.append(line[-1])
    nb = NaiveBayes()
    nb.fit(xs, ys)
    print(nb.predict((1, 1, 3, 4)))
    print(nb.predict((1, 1, 2, 4)))


if __name__ == '__main__':
    case()
