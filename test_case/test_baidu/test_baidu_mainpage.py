# -*- coding: utf-8 -*-
import time

import pytest

from test_case.test_baidu.baidu_mainpage import BaiDuMainPage


class TestDemo:
    def test_search111111111111(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.search("selenium")
        assert 1 == 1

    def test_search111111111111111111(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.search("selenium1111111111111111111")
        assert 1 == 1

    def test_click_tieba(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_tieba()
        assert 1 == 1

    l = [i for i in range(20, 30)]

    @pytest.mark.parametrize('data', l)
    def test_click_fanyi(self, browser, data):
        print(data)
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        assert 1 == 1

    def test_wait(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    def test_click_fanyi1(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        assert 1 == 1

    def test_click_fanyi2(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        assert 1 == 1

    def test_click_fanyi3(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        time.sleep(5)
        assert 1 == 1

    def test_click_fanyi4(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        time.sleep(5)
        assert 1 == 1

    def test_click_fanyi5(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        time.sleep(5)
        assert 1 == 1

    def test_click_fanyi6(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        assert 1 == 1

    def test_click_fanyi7(self, browser):
        driver = BaiDuMainPage(browser)
        driver.visit('https://www.baidu.com')
        driver.click_fanyi()
        assert 1 == 1

    def test_wait1(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    def test_wait2(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    def test_wait3(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    def test_wait4(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    def test_wait5(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        driver.wait_fuzhu()
        assert 1 == 1

    @pytest.mark.smoke
    def test_wait6(self, browser):
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        txt = driver.wait_fuzhu()
        assert txt == '辅助模式'

    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @pytest.mark.parametrize('data', l1)
    def test_wait7(self, browser, data):
        print(data)
        driver = BaiDuMainPage(browser)
        driver.login_baidu()
        txt = driver.wait_fuzhu()
        assert txt == '辅助模式1'
