import json
import os
import time

import allure
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def visit(self, url):
        """
        :param url: 输入url
        :return:
        """
        self.driver.get(url)

    def find_element(self, method, method_value):
        method = method.lower()
        if method == "id":
            return self.driver.find_element(By.ID, method_value)
        elif method == "name":
            return self.driver.find_element(By.NAME, method_value)
        elif method == "class_name" or method == "class":
            return self.driver.find_element(By.CLASS_NAME, method_value)
        elif method == "link_text" or method == 'text':
            return self.driver.find_element(By.LINK_TEXT, method_value)
        elif method == "partial_link_text":
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, method_value)
        elif method == "tag_name" or method == "tag":
            return self.driver.find_element(By.TAG_NAME, method_value)
        elif method == "xpath" or method == "x":
            return self.driver.find_element(By.XPATH, method_value)
        elif method == "css_selector" or method == "css":
            return self.driver.find_element(By.CSS_SELECTOR, method_value)

    def wait_element(self, method, method_value):
        if method == "id":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.ID, method_value),
                                                             message='等待失败')
        elif method == "name":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.NAME, method_value),
                                                             message='等待失败')
        elif method == "class_name" or method == "class":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.CLASS_NAME, method_value),
                                                             message='等待失败')
        elif method == "link_text" or method == 'text':
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.LINK_TEXT, method_value),
                                                             message='等待失败')
        elif method == "partial_link_text":
            return WebDriverWait(self.driver, 10, 0.5).until(
                lambda x: x.find_element(By.PARTIAL_LINK_TEXT, method_value), message='等待失败')
        elif method == "tag_name" or method == "tag":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.TAG_NAME, method_value),
                                                             message='等待失败')
        elif method == "xpath" or method == "x":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, method_value),
                                                             message='等待失败')

    def scroll_to_element(self, method, method_value):
        element = self.find_element(method, method_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        return self.driver.execute_script("return document.body.scrollHeight;")

    # 滚动到指定位置
    def scroll_to_position(self, position):
        self.driver.execute_script("window.scrollTo(0, {});".format(position))

    # 滚动到顶部
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    # 获取滚动条高度
    def get_scroll_height(self):
        return self.driver.execute_script("return document.body.scrollHeight;")

    def click_element(self, method, method_value):
        try:
            self.find_element(method, method_value).click()
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].click();", self.find_element(method, method_value))

    def input(self, method, method_value, text):
        self.find_element(method, method_value).send_keys(text)

    def get_text(self, method, method_value):
        return self.find_element(method, method_value).text

    def add_cookies(self, cookie_path):
        with allure.step('获取元素文本'):
            with open(cookie_path, 'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

    def move_to_element(self, method, method_value):
        element = self.find_element(method, method_value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def move_element(self, draggable_element, target_element):
        """
        :param draggable_element: 拖拽元素
        :param target_element: 目标元素
        """
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable_element, target_element).perform()

    def slide_element(self, draggable_element, xoffset, yoffset):
        """
        :param draggable_element: 拖拽元素
        :param xoffset: 横向偏移量
        :param yoffset: 纵向偏移量
        """
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(draggable_element, xoffset, yoffset).perform()

    def assert_toast_element(self, toast_message):
        try:
            xpath = '//*[text()=\'{}\']'.format(toast_message)
            toast_element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elment(By.XPATH, xpath),
                                                                      message='等待失败')
            print(toast_element.text)  # 打印toast文本
            assert toast_element.text == toast_message
            return True
        except AssertionError:
            return False

    def add_attribute(self, elementobj, attributeName, value):
        """
        封装向页面标签添加新属性的方法
        调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
        会用后面的element，attributeName和value参数进行替换
        添加新属性的JS代码语法为：element.attributeName=value
        比如input.name='test'
        """
        self.driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)

    def set_attribute(self, elementobj, attributeName, value):
        """
        封装设置页面对象的属性值的方法
        调用JS代码修改页面元素的属性值，arguments[0]~arguments[1]分别
        会用后面的element，attributeName和value参数进行替换
        """
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, attributeName,
                                   value)

    def remove_attribute(self, elementobj, attributeName):
        """
        封装删除页面属性的方法
        调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
        会用后面的element，attributeName参数进行替换
        """
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                                   elementobj, attributeName)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def switch_to_frame(self, method, method_value):
        return self.driver.switch_to.frame(self.find_element(method, method_value))

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    def switch_to_window(self, index=0):
        return self.driver.switch_to.window((self.driver.window_handles[int(index)]))

    def quit(self):
        self.driver.quit()

    def screen_shot(self, filename):
        self.driver.save_screenshot(filename)

    def assert_element_text(self, method, method_value, respect):
        try:
            assert self.get_text(method, method_value) == respect
            return True
        except AssertionError:
            return False

    def assert_url(self, respect):
        try:
            assert self.get_url() == respect
            return True
        except AssertionError:
            return False

    def assert_title(self, respect):
        try:
            assert self.get_title() == respect
            return True
        except AssertionError:
            return False

    def assert_attribute(self, method, method_value, name, respect):
        try:
            attribute_name = self.find_element(method, method_value).get_attribute(name)
            assert attribute_name == respect
            return True
        except AssertionError:
            return False

    def assert_element_exist(self, method, method_value):
        try:
            assert self.find_element(method, method_value)
            return True
        except AssertionError:
            return False

    def assert_text(self, method, method_value, expected_value):
        try:
            assert self.get_text(method, method_value) == expected_value
            return True
        except AssertionError:
            return False

    @staticmethod
    def sleep(num):
        time.sleep(num)


def tendency_data_operate():
    # 读取已备份的json文件
    f1_path = os.path.dirname(os.path.dirname(__file__)) + '/config/history-trend_bak.json'
    f2_path = os.path.dirname(os.path.dirname(__file__)) + '/allure-report/widgets/history-trend.json'

    f1 = open(f1_path, 'r+')
    f2 = open(f2_path, 'r+')
    data_bak = json.load(f1)
    data2 = json.load(f2)
    index = data_bak[0]['buildOrder']
    # 读取最新的trend数据,添加，buildOrder项
    data2[0]['buildOrder'] = index + 1
    # 向data_bak插入新数据
    data_bak.insert(0, data2[0])
    f3 = open(f1_path, 'w')
    json.dump(data_bak, f3, indent=4)
    f4 = open(f2_path, 'w')
    json.dump(data_bak, f4, indent=4)
    f1.close()
    f2.close()
    f3.close()
    f4.close()


def cookie_str_to_dict(data: str) -> dict:
    _dict = {}
    for item in data.split(';'):
        key, value = item.strip().split('=', 1)
        _dict[key] = value
    return _dict


def url_data_str_to_dict(data: str) -> dict:
    _dict = {}
    for item in data.split('&'):
        key, value = item.strip().split('=', 1)
        _dict[key] = value
    return _dict


if __name__ == '__main__':
    tendency_data_operate()
