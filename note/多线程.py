# -*- coding: utf-8 -*-
import queue
import threading

s = ['1', '2', '2', '2', '2']


# for i in s:
#     t = threading.Thread(target=print, args=(i,))
#     t.start()


class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args

    def run(self):
        return self.target(*self.args)

    def result(self):
        return self.target(*self.args)


def p(i):
    print(i)
    return i


t_l = []
for i in s:
    t = MyThread(target=p, args=(i,))
    t_l.append(t.run())
    t.start()
p(t_l)


class ReturnValueThread(threading.Thread):
    def __init__(self, target, args=(), daemon=False):
        super().__init__(daemon=daemon)
        self.target = target
        self.args = args
        self.result_queue = queue.Queue()

    def run(self):
        try:
            result = self.target(*self.args)
        except Exception as e:
            self.result_queue.put(e)
        else:
            self.result_queue.put(result)

    def get_result(self, block=True, timeout=None):
        return self.result_queue.get(block=block, timeout=timeout)


def my_function(number):
    print(f"Processing {number}")
    return f"Result for {number}"


# 假设我们想要处理一系列的数字
numbers = [1, 2, 3, 4, 5]

# 创建线程列表
threads = []

# 创建并启动线程
for number in numbers:
    thread = ReturnValueThread(target=my_function, args=(number,))
    thread.start()
    threads.append(thread)

# 等待所有线程结束（可选，因为设置了daemon=True，主线程退出时它们会自动结束）
result1 = []
for t in threads:
    t.join()
    result1.append(t.get_result())

print('result', result1)
