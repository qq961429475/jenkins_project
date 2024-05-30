import concurrent.futures


def my_function(number):
    print(number)
    return number


# 使用示例
numbers = [1, 2, 3, 4, 5, (11, 22)]

# 创建一个线程池执行器  
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 提交任务到线程池，并获取Future对象列表  
    futures = [executor.submit(my_function, num) for num in numbers]
    result = []
    # 遍历Future对象列表，获取结果  
    for future in concurrent.futures.as_completed(futures):
        try:
            r = future.result()
            result.append(r)
        except Exception as e:
            print(f"An error occurred in the thread: {e}")
    print(f"All threads finished: {result}")
