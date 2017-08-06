# coding=utf-8


import string
import random
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from functools import partial
from bitmap import BitMap


class BloomFilter:
    """
    基于BitMap的布隆过滤器
    """
    N_INSTANCE = 0  # 实例数量

    def __init__(self, size_byte=1 << 6, n_hash=1 << 2):
        self.size_byte = size_byte  # 字节开销
        self.size_bit = 8 * size_byte  # bit开销
        self.n_hash = n_hash  # hash函数数量
        self.bf = BitMap(self.size_byte)  # 存储
        # 通过科里化方式生成n_hash个hash函数列表
        self.hash_functions = [partial(self._hash,
                                       capacity=self.size_bit,
                                       seed=seed)
                               for seed in self._mk_primes(self.n_hash)]

        BloomFilter.N_INSTANCE += 1

    @staticmethod
    def _mk_primes(n):
        """
        制作n个素数，用于hash函数种子
        :param n: int
        :return: int []
        """
        num = 5
        ret = []
        i = 2
        while 1:
            if num % i == 0:
                num += 1
                i = 1
            if i * i > num:
                ret.append(num)
                n -= 1
                i = 1
                num += 1
                if n == 0: break
            i += 1
        return tuple(ret)

    @staticmethod
    def _hash(string, capacity, seed):
        """
        哈希函数.注意这个hash函数效果是很差的，实际使用应该考虑其他hash函数。
        :param string: str,待输入的数据
        :param capacity: int, Bitmap的bit容量（待绑定）
        :param seed: int, hash函数种子，建议为素数(待绑定)
        :return: int, hashcode
        """
        ret = 0
        for si in string:
            ret += seed * ret + ord(si)
        return (capacity - 1) & ret

    def _get_codes(self, a_string):
        """
        取得k个hashcode
        :param a_string: str, 待哈希的数据
        :return: k-dim int tuple
        """
        return tuple(f(a_string) for f in self.hash_functions)

    def put(self, a_string):
        """
        添加一个历史数据
        :param a_string: str,单个数据
        :return: raise or success
        """
        self.bf.put_batch(self._get_codes(a_string))
        return "success"

    def put_batch(self, strings):
        """
        添加多个历史数据
        :param strings: <iterable<str>> 数据集合
        """
        [self.put(a_string) for a_string in strings]

    def contains(self, a_string):
        """
        查询数据是否在历史数据中
        :param a_string: str, 待查询数据
        :return: boolean, True or False
        """
        for code in self._get_codes(a_string):
            if not self.bf.contains(code):
                return False
        return True

    def __contains__(self, a_string):
        """
        为contains函数支持in语法
        """
        return self.contains(a_string)

    def get_load(self):
        """
        查看bitmap的负载（覆盖率）
        :return: float, 负载
        """
        return sum(1 if self.bf.contains(i) else 0
                   for i in range(self.bf.limit_min, self.bf.limit_max + 1)) / float(self.size_bit)

    def show_bf(self):
        """
        查看实际存储情况
        :return: void -> stdout
        """
        self.bf.show()

    @classmethod
    def test(cls):
        """
        可用性自我测试
        :return: void -> raise or success
        """
        m = BloomFilter()
        m.put("xyzd")
        m.put("")
        m.put("uuu")
        m.put("uu1")
        assert m.contains("xy") is False
        assert m.contains("tz") is False
        assert "tz" not in m
        assert "uuu" in m
        print("it works")


class CrossValidation:
    """
    布隆过滤器的分析
    """

    def __init__(self):
        pass

    @staticmethod
    def mk_sample(n=1000):
        """
        制作数据样本
        :param n: int， 数据个数
        :return: 随机数据元组
        """
        return tuple("".join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 100)))
                     for _ in range(n))

    def load_with_put(self, n_bf_byte=128, n_hash=3, n_sample=2000):
        """
        获取不同添加个数下的负载
        :param n_bf_byte: int, 字节开销
        :param n_hash:
        :param n_sample: int, 添加数量上限
        :return: <list<2-dim tuple>>
        """
        bf = BloomFilter(n_bf_byte, n_hash)
        sample = self.mk_sample(n_sample)
        record = []
        for i, sa in enumerate(sample):
            bf.put(sa)
            record.append((i, bf.get_load()))
        return record

    def plt_load_with_put(self):
        """
        绘制负载-数量的分析结果
        :return: void -> file
        """
        params = [(1 << nn_byte, n_hash, 2000) for n_hash in range(1, 8, 2) for nn_byte in range(6, 11, 2)]
        plt.figure()
        for param in params:
            print(param)
            plt.plot(*zip(*self.load_with_put(*param)), label=param.__str__())
        plt.legend()
        plt.grid()
        plt.xlabel("n_add")
        plt.ylabel("load")
        plt.savefig("load_with_put.png", dpi=300)
        plt.show(block=True)

    @staticmethod
    def false_positive(n, data, rates=(9.6, 14.4)):
        """
        输错False Positive误判率
        :param n: int, 训练数据量
        :param data: <list<int>>, 所有数据
        :param rates: m/n, 容量与数据比
        :return: <dict<float:float>>, 不同容量比下的误判率
        """
        if 2 * n > len(data):
            raise ValueError("data is not enough")
        data_train = data[:n]
        data_test = data[n:]
        ret = {}
        for rate in rates:
            m = int(round((n * rate)))
            k = int(round(0.707 * rate) + 1)
            n_byte = m // 8 + 1
            bf = BloomFilter(n_byte, k)
            bf.put_batch(data_train)
            fn = sum(1 if bf.contains(data_i) else 0 for data_i in data_test)
            ret[rate] = float(fn) / len(data_test)
        return ret

    def plt_fasle_positive(self):
        """
        [TODO]BoolmFilter里的hash函数效果是很差的，需要更换
        :return:
        """
        sample = self.mk_sample(312)
        print(self.false_positive(20, sample))


if __name__ == '__main__':
    CrossValidation().plt_load_with_put()
    # CrossValidation().plt_fasle_positive()
