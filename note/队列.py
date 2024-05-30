# -*- coding: utf-8 -*-
import concurrent.futures
import queue
import time


def time_cost(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} cost {end - start}s')
        return result

    return wrapper


def fun1():
    time.sleep(1)
    print('fun1')
    return 1


def fun2():
    time.sleep(1)

    print('fun2')
    return 2


def fun3():
    time.sleep(1)

    print('fun3')
    return 3


q = queue.Queue()
q.put(fun1)
q.put(fun2)
q.put(fun3)


@time_cost
def run():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        while not q.empty():
            task = q.get()
            futures.append(executor.submit(task))
        result = []
        for future in concurrent.futures.as_completed(futures):
            result.append(future.result())
    return result


print(run())
q1 = queue.Queue()
q1.put('1')
q1.put('2')
q1.put('3')
q1.put('4')
q1.put('4')
q1.put('4')
q1.put('4')


def fun5(num):
    time.sleep(1)
    print(num)
    return num


for i in q1.queue:
    print(i)
print('**')


@time_cost
def run2():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        while not q1.empty():
            num = q1.get()
            futures.append(executor.submit(fun5, num))
        # 下面的方法能用但是是不推荐的
        # futures = [executor.submit(fun5, num) for num in q1.queue]
        result = []
        for future in concurrent.futures.as_completed(futures):
            result.append(future.result())
    return result


print(run2())
