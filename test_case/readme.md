# 修改allure title中，参数过多导致排版错误
listener.py
文件位置：Lib\site-packages\allure_pytest\listener.py （第三方包所在的LIb目录）
将下图中红色部分test_result.parameters.extend([]) 中参数改成空列表就行了