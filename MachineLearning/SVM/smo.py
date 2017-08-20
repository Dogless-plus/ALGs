# coding=utf-8
# todo @dogless： 增加序列化和反序列化接口
# todo @dogless:  添加更多核函数
from copy import deepcopy


class SMO:
    """ SMO模型
    """

    def __init__(self, *args, **kwargs):
        """
        :param args: 重定向到fit方法的位置参数
        :param kwargs: 重定向到fit方法的关键字参数
        """
        self._x = None  # 内部存储的训练数据或者支持向量
        self._y = None  # 内部存储的训练数据的监督值或者支持向量的监督值
        self.dimension = None  # 数据的维度
        self.shape = None  # 训练数据的形状或者支持向量的形状
        self.max_loop = None  # 最大迭代次数
        self.debugging = False  # 是否开启调试模式
        self.a = None  # 各个样本点或者支持向量的权重
        self.b = None  # bias平面偏移
        self.E = None  # 残差列表
        self.C = None  # 惩罚因子
        self.kernel = None  # 核函数的挂载入口
        self.cache_kernel = None  # 缓存核函数值加速迭代
        self.tolerance = None  # 允许继续迭代的最小差值
        self._support_vector_x = []  # 临时支持向量列表
        self._support_vector_y = []  # 临时的监督值列表
        if args or kwargs:  # 将构造器同时作为训练的入口
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

    def _linear_kernel(self, i, j):
        """ 线性核
        :param i: int 左向量
        :param j: int 右向量
        :return: float 线性核函数值
        """
        return sum(map(lambda a, b: a * b, self._x[i], self._x[j]))

    def _init_cache_kernel(self):
        """ 缓存核函数值
        """
        cache_kernel = dict()
        for i in range(self.shape[1]):
            for j in range(self.shape[1]):
                cache_kernel[(i, j)] = self.kernel(i, j)
        self.cache_kernel = cache_kernel

    def _get_residual(self, i):
        """ 计算残差
        :param i: int 第i个样本点
        :return: float 残差
        """
        y_predict = sum(self.a[j] * self._y[j] * self.cache_kernel[(j, i)]
                        for j in range(self.shape[1])) + self.b
        return y_predict - self._y[i]

    def _update_E(self):
        """ 更新残差列表
        """
        for i in range(self.shape[1]):
            self.E[i] = self._get_residual(i)

    def _is_against_kkt(self, i):
        """ 是否违背了KKT条件
        :param i: int 第i个样本点
        :return: boolean  是或者否
        """
        return (self.a[i] < self.C and self._y[i] * self.E[i] < -self.tolerance) or \
               (self.a[i] > 0 and self._y[i] * self.E[i] > self.tolerance)

    def _update(self):
        """ 单轮参数更新(单轮训练)，更新式都是书上的公式，更新a和b还有残差列表
        :return: 是否需要再一轮更新
        """
        is_updated = False
        for i in range(self.shape[1]):
            if not self._is_against_kkt(i): continue
            for j in range(self.shape[1]):
                if j == i: continue
                eta = self.cache_kernel[(j, j)] + self.cache_kernel[(i, i)] - 2 * self.cache_kernel[(i, j)]
                if eta <= 0: continue
                aj_new = self.a[j] + self._y[j] * (self.E[i] - self.E[j]) / eta
                if self._y[i] == self._y[j]:
                    L = max(0, self.a[j] + self.a[i] - self.C)
                    H = min(self.C, self.a[j] + self.a[i])
                else:
                    L = max(0, self.a[j] - self.a[i])
                    H = min(self.C, self.a[j] - self.a[i] + self.C)
                aj_new = H if aj_new > H else L if aj_new < L else aj_new
                if -0.001 < self.a[j] - aj_new < 0.001: continue
                ai_new = self.a[i] + self._y[i] * self._y[j] * (self.a[j] - aj_new)
                b_new1 = self.b - self.E[i] - self._y[i] * self.cache_kernel[(i, i)] * (ai_new - self.a[i]) - \
                         self._y[j] * self.cache_kernel[(j, i)] * (aj_new - self.a[j])
                b_new2 = self.b - self.E[j] - self._y[i] * self.cache_kernel[(i, j)] * (ai_new - self.a[i]) - \
                         self._y[j] * self.cache_kernel[(j, i)] * (aj_new - self.a[j])
                self.b = b_new1 if 0 < ai_new < self.C else b_new2 if 0 < aj_new < self.C else (b_new1 + b_new2) / 2.0
                self.a[i] = ai_new
                self.a[j] = aj_new
                self._update_E()
                is_updated = True
        return is_updated

    def _train(self):
        """ 执行多轮训练，训练不成功应该直接报错
        """
        for loop in range(self.max_loop):
            if not self._update():
                return
            if self.debugging:
                print(loop, self.a, self.b)
        raise ValueError("reach max loop limit")

    def _mk_support_vectors(self):
        """ 将内部存储压缩至支持向量
        """
        a_new = []
        for i, v in enumerate(self.a):
            if v > 0:
                self._support_vector_x.append(self._x[i])
                self._support_vector_y.append(self._y[i])
                a_new.append(v)
        # print(self.shape)
        self._x = self._support_vector_x
        self._y = self._support_vector_y
        self.a = a_new
        self.shape = self.shape[0], len(self._x)
        # print(self.shape)

    def fit(self, x, y, C=10, kernel="linear", max_loop=1000, tolerance=0.00001, debugging=False):
        """ 用外部数据拟合出一个二分类的svm
        :param x: list<tuple<float>> 相同维度的训练数据点列表
        :param y: list<float> 与x同样长度的监督值列表
        :param C: float 惩罚因子，惩罚约大意味着对outlier的容忍度越小
        :param kernel:  指定核函数名，核函数做成可插拔的。默认是线性核『linear』
        :param max_loop: 最大迭代轮数，默认1000.
        :param tolerance: 最小更新量（针对残差），默认0.00001
        :param debugging: 是否开启,若开启，将在stdout输错更多调试信息。默认关闭。
        """
        self._x = deepcopy(x)
        self._y = deepcopy(y)
        self.C = C
        self.tolerance = tolerance
        self.debugging = debugging
        self.max_loop = max_loop
        self.dimension = len(x[0])
        self._check()
        self.shape = self.dimension, len(x)
        self.a = [0.0] * self.shape[1]
        self.b = 0.0
        self.kernel = self._linear_kernel if kernel.lower() == "linear" else None  # TODO: more kernel
        self._init_cache_kernel()
        self.E = [0.0] * self.shape[1]
        self._update_E()
        self._train()
        self._mk_support_vectors()

    def predict(self, x):
        """ 预测新数据
        :param x: 待预测的数据点
        :return: 预测值 1.0 或者 -1.0
        """
        if len(x) != self.dimension: raise ValueError("length not match")
        self._x.append(x)
        y = sum(self.a[j] * self._y[j] * self.kernel(j, -1) for j in range(self.shape[1])) + self.b
        self._x.pop()
        return 1.0 if y >= 0 else -1.0


def case():
    """ 测试demo
    """

    def load_data(filename):
        with open(filename, "rt") as f:
            lines = f.readlines()
        xs, ys = [], []
        for line in lines:
            line = line.strip().split()
            xs.append(tuple(float(xi) for xi in line[:-1]))
            ys.append(float(line[-1]))
        return xs, ys

    xs, ys = load_data("train.tsv")
    smo = SMO()
    smo.fit(xs, ys, debugging=True)
    # for xi,yi in zip(xs,ys):
    #     print(smo.predict(xi),yi)


    import matplotlib
    matplotlib.use("tkagg")
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    # 绘制训练数据
    for xi, yi in zip(xs, ys):
        plt.scatter(*xi, c="r" if yi > 0 else "g", marker="s", s=50)
    # 绘制两个半平面
    import numpy as np
    x_scan = np.linspace(10, 90, 50)
    y_scan = np.linspace(10, 90, 50)
    for xi in x_scan:
        for yi in y_scan:
            z = smo.predict((xi, yi))
            print(xi, yi, z)
            plt.scatter(xi, yi, c="r" if z > 0 else "g", marker="x", s=10)
    plt.grid()
    plt.savefig("smo.png", dpi=300)
    plt.show()


if __name__ == '__main__':
    case()
