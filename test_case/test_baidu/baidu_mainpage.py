import allure

from common.utils import BasePage
from config.filepath import baidu_cookie


class BaiDuMainPage(BasePage):
    url = 'https://www.baidu.com'

    def login_baidu(self):
        self.visit('https://www.baidu.com')
        self.add_cookies(baidu_cookie)

    def open_baidu_url(self):
        """打开百度首页"""
        self.visit("https://www.baidu.com")

    def search(self, keyword):
        """搜索关键字"""
        self.input("id", "kw", keyword)
        self.click_element("id", "su")

    def click_news(self):
        """点击新闻"""
        self.click_element("x", "//*[text()='新闻']")

    def click_hao123(self):
        """点击hao123"""
        self.click_element("link_text", "hao123")

    def click_map(self):
        """点击地图"""
        self.find_element("link_text", "地图").click()

    def click_video(self):
        """
        点击视频
        """
        self.click_element('x', '//*[@id="s-top-left"]/a[5]')

    def click_tieba(self):
        """点击"""
        self.click_element('x', '//*[@id="s-top-left"]/a[3]')

    @allure.step("点击翻译")
    def click_fanyi(self):
        """点击"""

        self.move_to_element('x', "//*[@name='tj_briicon']")
        self.click_element('x', '//*[@name="tj_fanyi"]')

    @allure.step("等待辅助功能")
    def wait_fuzhu(self):
        self.click_element('x', '//*[@class="aging-entry-inner"]')
        txt = self.get_text('x', '//*[@class="toast c-color-text"]')
        return txt
