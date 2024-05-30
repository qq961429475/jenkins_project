import unittest

from ddt import ddt, data, unpack, file_data


@ddt
class Test(unittest.TestCase):
    @file_data('../data/test_01.yaml')
    # 设置入口参数名字与数据参数命名相同即可
    def test_data(self, url, input, click, expected, case_name):
        print(url, input, click, expected, case_name)

    @file_data('../data/test_01.yaml')
    def test_data2(self, **kwargs):
        print(kwargs)
        # 结果为{'url': 'https://www.baidu.com', 'input': ['id', 'kw', '你好'], 'click': ['id', 'su'], 'expected': '百度一下，你就知道', 'case_name': '正确的用例断言'}
        print(*kwargs)
        # 结果为 url input click expected case_name
        print(*kwargs['input'])
        # 结果为 id kw 你好1111111

    @data(1, 2, 5, 3, 4, )  # 数据  （5条运行5次）
    def test1(self, a):  # a 用来接收data数据
        print(a)

    @data([1, 2, 3])
    def test2(self, a):  # a用来接收data数据
        print(a)

    @data({'name': 'zs', 'age': 18})
    def test3(self, a):  # a用来接收data数据
        print(a)

    @data({'name': 'zs', 'age': 18}, {'name': 'zs1', 'age': 20})
    @unpack
    def test4(self, name, age):  # a用来接收data数据
        # data为value的一条数据
        print(name, age)


if __name__ == '__main__':
    unittest.main()
