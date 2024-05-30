import time

import allure
import pytest

from common.fileRead import load_case_data

url = 'https://www.baidu.com'


class TestMainPage:
    @allure.feature('登录')
    @allure.story('登录--')
    @pytest.mark.parametrize('data', load_case_data('test_02'))  # 你的参数化数据加载逻辑
    def test_func(self, browser, data):
        allure.dynamic.title(data.get('title'))
        allure.dynamic.description(data['description'])
        print(data)
        with allure.step('打开百度首页'):
            browser.get(data['url'])

        time.sleep(2)
        assert 1 == 1

    @pytest.mark.smoke
    def test_func2111111111(self, browser):
        browser.get(url)
        assert 1 == 2

    @pytest.mark.smoke
    def test_func3(self, browser):
        browser.get(url)
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.smoke
    def test_func4(self, browser):
        # browser.get("https://www.baidu.com")
        browser.get("https://www.right.com.cn/")
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', 'test_title.py'])
