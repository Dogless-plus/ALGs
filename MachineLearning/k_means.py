# coding=utf-8
from copy import deepcopy
from random import sample


class Kmeans:
    """ K-means 聚类，目标是平均中心距离最小
    """

    def __init__(self, *args, **kwargs):
        self._x = None  # 内部存储的训练集
        self.dimension = None  # 训练集的维度
        self.shape = None  # 数据集形状
        self.n_clusters = None  # cluster的数量
        self.centers = None  # 聚类中心
        self._y = None  # 与self._x 一一对应的cluster id
        self._init_func = sample  # 指定初始化方案
        self.max_loop = None  # 最大迭代次数
        self.distance = self._squared_euclidean_distance  # 指定距离方案
        self.debugging = False  # 是否开启调试模式
        self.history = []  # 历史记录，仅在调试模式下追加数据
        if args or kwargs:  # 重定向初始化方法
            self.fit(*args, **kwargs)

    def _check(self):
        """ 检查数据合法性
        """
        for xi in self._x:
            if len(xi) != self.dimension:
                raise ValueError("length of x not consistent")
            [self._check_float(xii) for xii in xi]

    @staticmethod
    def _check_float(x):
        """  检查数据类型是否是浮点型
        """
        if type(x) != float:
            raise ValueError("%s not float" % x)

    def _init_clusters(self):
        """ 初始化聚类中心
        """
        centers = self._init_func(self._x, self.n_clusters)
        self.centers = {i: centers[i] for i in range(self.n_clusters)}

    def _squared_euclidean_distance(self, v1, v2):
        """ 欧式距离的平方，无须开方
        """
        return sum(map(lambda x1, x2: (x1 - x2) ** 2, v1, v2))

    def _re_cluster(self, idx):
        """ 重新分cluster
        :param idx: int, 第i个数据点
        :return: 新的clustet_id
        """
        return sorted([(self.distance(self._x[idx], center), k)
                       for k, center in self.centers.items()],
                      key=lambda x: x[0],
                      reverse=False)[0][1]  # todo:效率待优化到线性

    def get_clusters(self):
        """ 获取所有cluster
        :return: dict <int:list> 各个簇的字典
        """
        clusters = {i: [] for i in range(self.n_clusters)}  # 会不会有空的cluster，是可能的
        for x, y in zip(self._x, self._y):
            clusters[y].append(x)
        return clusters

    def _vector_center(self, vectors):
        """
        :param vectors: <list<list<float>>> 一个cluster内的所有点
        :return: list<float> 这些点的几何中心
        """
        return list(map(lambda x: sum(x) / len(x), zip(*vectors)))

    def _re_center(self):
        """
        :return: 更新所有cluster的几何中心
        """
        clusters = self.get_clusters()
        for k in clusters:
            clusters[k] = self._vector_center(clusters[k])
        self.centers = clusters

    def _train(self):
        """ 在有限迭代次数下 重新分cluster，更新各个cluster中心
        """
        loop = 0
        while 1:  # 1 is better than True
            loop += 1
            if loop > self.max_loop: break  # 出口条件1：达到迭代次数上限
            if self.debugging:
                # print(loop,self.get_clusters())
                self.history.append(self.get_clusters())
            not_re_centered = True
            for i in range(self.shape[1]):  # M步
                new_center = self._re_cluster(i)
                if self._y[i] != new_center:
                    self._y[i] = new_center
                    not_re_centered = False  # 出口条件2：这一轮没有更新中心位置，下一轮也无法更新了
            if not_re_centered: break
            self._re_center()  # E步

    def fit(self, x, n_clusters=3, max_loop=1000, debugging=False):
        """ 模型入口
        :param x: list<list<float>> 各个数据
        :param n_clusters: int 指定k个cluster
        :param max_loop: int 最大迭代次数
        :param debugging: boolean 是否开启调试模式
        """
        self._x = deepcopy(x)
        self.dimension = len(x[0])
        self.shape = self.dimension, len(x)
        self.n_clusters = n_clusters
        self.max_loop = max_loop
        self.debugging = debugging
        self._check()
        self._init_clusters()
        self._y = [0] * self.shape[1]
        self._train()

    def predict(self, xi):
        """ 预测单点分类
        :param xi: list<float> 待预测点
        :return: int cluster_id
        """
        if len(xi) != self.dimension: raise ValueError("length not match")
        return sorted([(self.distance(xi, center), k)
                       for k, center in self.centers.items()],
                      key=lambda x: x[0],
                      reverse=False)[0][1]  # todo:效率待优化到线性


def demo():
    x = [[100.0, 101.0], [102.0, 102.0], [117.3, 118.6], [-1.0, 1.2],
         [50.5, 50.7], [60.8, 60.9], [-100.0, -98.8], [-99.7, -99.2],
         [50.7, 52.8], [-2.0, -50.5], [-5.7, -10.6], [-60.6, -70.3], ]
    kmeans = Kmeans(x, n_clusters=3, debugging=True)
    # kmeans = Kmeans()
    # kmeans.fit(x,debugging=True)
    history = kmeans.history
    n_history = len(history)
    test_cases = [(-100.0, -200.0), (1.0, 5.6), (200.7, 199.9)]
    for case in test_cases:
        print(case, kmeans.predict(case))
    import matplotlib
    matplotlib.use("tkagg")
    import matplotlib.pyplot as plt
    plt.figure(figsize=(4, 3))

    for hi in range(n_history):
        plt.subplot(n_history, 1, hi + 1)
        for ci in range(3):
            data = history[hi][ci]
            if not data: continue
            xs, ys = list(zip(*data))
            plt.scatter(xs, ys, c="r" if ci == 0 else "g" if ci == 1 else "b")
            plt.grid()
    # plt.savefig("k_means.png",dpi=300)
    plt.show()
    print(history)


if __name__ == '__main__':
    demo()
