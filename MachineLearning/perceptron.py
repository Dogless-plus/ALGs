# coding=utf-8
# 实现原理请参考我的博客  http://dogless.farbox.com/post/github/-tong-ji-xue-xi-fang-fa-za-ji
from copy import deepcopy


class Perceptron:
    """ perceptron 感知机
    """

    def __init__(self, *args, **kwargs):
        self._x = None  # 训练集的特征向量集合x
        self._y = None  # 训练集的监督值集合y
        self.dimension = None  # 特征维度
        self.shape = None  # 训练集的形状
        self.w = None  # 权重向量
        self.learning_rate = None  # 学习步长
        self._cache_lambdaxiyi = None  # 缓存第i个数据的计算
        self.max_loop = None  # 最大尝试轮数
        self._history = []  # 记录历史的权重
        self.debugging = False
        if args:
            self.fit(*args, **kwargs)

    def _check(self):
        """ 检查数据合法性
        """
        if len(self._x) != len(self._y):
            raise ValueError("length of train_x and train_y not match")
        for xi in self._x:
            if len(xi) != self.dimension:
                raise ValueError("length of x not consistent")
            [self._check_float(xii) for xii in xi]
        [self._check_float(yi) for yi in self._y]

    @staticmethod
    def _check_float(x):
        """  检查数据类型是否是浮点型
        """
        if type(x) != float:
            raise ValueError("%s not float" % x)

    def _tail_one(self):
        """  对特征追加一维
        """
        for xi in self._x:
            xi.append(1.0)
        self.dimension += 1

    def _init_cache(self):
        """  初始化加速缓存
        """
        self._cache_lambdaxiyi = tuple(tuple(self.learning_rate * yi * xii for xii in xi)
                                       for xi, yi in zip(self._x, self._y))

    def _train(self):
        """ 执行训练过程
        """
        idx = 0
        count = 0
        loop = 0
        while 1:
            if count > self.shape[1]: break
            count += 1
            if self.debugging:  # 测试输出
                print(idx, count, self.w)
            idx = (idx + 1) % self.shape[1]  # 第i个样本点
            if idx == 0: loop += 1
            if loop >= self.max_loop: raise TimeoutError("reach max loop, may be inseparable")
            if self._is_error(idx):
                count = 0
                self._history.append(tuple(self.w))
                self._update(idx)
        self._history.append(tuple(self.w))

    def _is_error(self, idx):
        return round(self._y[idx] * self._vector_multiply(self.w, self._x[idx]), 1) <= 0.0

    @staticmethod
    def _vector_multiply(v1, v2):
        """ 向量点乘
        """
        return sum(map(lambda x1, x2: x1 * x2, v1, v2))

    @staticmethod
    def _vector_add(v1, v2):
        """ 向量求和
        """
        return list(map(lambda x1, x2: x1 + x2, v1, v2))

    def _update(self, idx):
        """ 执行权重更新操作
        :param idx:
        :return:
        """
        self.w = self._vector_add(self.w, self._cache_lambdaxiyi[idx])

    def fit(self, train_x, train_y, learning_rate=0.1, max_loop=1000, debugging=True):
        """ 输入训练数据进行训练
        :param train_x: <list<tuple<float [d]>>>  d维的训练数据集
        :param train_y: <list <float>>  1维的标签列表，与train_x一一对应
        :param learning_rate: 学习率
        :param max_loop: 最大迭代轮数
        :param debugging: 是否开启调试信息
        """
        self._x = deepcopy(train_x)  # 安全使用
        self._y = deepcopy(train_y)
        self.dimension = len(train_x[0])
        self.shape = self.dimension, len(self._y)
        self.learning_rate = learning_rate
        self.debugging = debugging
        self.max_loop = max_loop
        self._check()
        self._tail_one()
        self.w = [0.0 for _ in range(self.dimension)]
        self._init_cache()
        self._train()

    def _sign(self, x):
        return 1.0 if x >= 0 else -1.0

    def predict(self, test_x):
        """ 为测试数据预测二分类标签
        :param test_x: list< float [d]> 单个d维的测试数据
        :return: float 标签值
        """
        test_x = list(test_x)
        if len(test_x) != self.shape[0]: raise ValueError("shape not match")
        test_x.append(1.0)
        return self._sign(self._vector_multiply(self.w, test_x))


class Case:
    @classmethod
    def demo(cls):
        train_x = [[3.0, 3.0], [4.0, 3.0], [1.0, 1.0]]
        train_y = [1.0, 1.0, -1.0]
        perceptron = Perceptron(train_x, train_y, learning_rate=0.3, debugging=False)
        # perceptron = Perceptron()
        # perceptron.fit(train_x,train_y,learning_rate=0.3,debugging=False)
        test_points = [(1.0, 2.0), (-1.0, -2.0), (4.0, 4.0)]
        for point in test_points:
            print(point, perceptron.predict(point))

        # plot
        import matplotlib  # dynamic importing
        matplotlib.use("Tkagg")
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 6))
        for point, color in zip(train_x, train_y):
            plt.scatter(point[0], point[1], c="r" if color > 0 else "g", marker="s")
        axis0, axis1 = list(zip(*train_x))
        axis0_max, axis0_min, axis1_max, axis1_min = max(axis0), min(axis0), max(axis1), min(axis1)
        import numpy as np
        x_scan = np.linspace(axis0_min - 1, axis0_max + 1, 100)
        for i, w in enumerate(perceptron._history[1:]):
            y_scan = [(w[0] * xi + w[2]) / - w[1] for xi in x_scan]
            plt.plot(x_scan, y_scan, label="update_" + str(i))
        plt.ylim(axis0_min - 1, axis1_max + 1)
        plt.legend()
        plt.grid()
        plt.show()

    @classmethod
    def demo2(cls):
        train_x = [[3.0, 3.0], [4.0, 3.0], [1.0, 1.0], [4.0, 3.1]]
        train_y = [1.0, 1.0, -1.0, -1.0]
        perceptron = Perceptron()
        perceptron.fit(train_x, train_y)


if __name__ == '__main__':
    # Case.demo2()
    Case.demo()
