import json
import time
from configparser import ConfigParser

import allure
import pytest
from selenium import webdriver

from config.filepath import config_path

# 读取配置
config = ConfigParser()
config.read(config_path, encoding='utf-8')


@pytest.fixture(scope='session')
def browser(request):
    """
        全局定义浏览器启动
    """
    global driver, options
    browser_name = config.get('browser', 'name').capitalize()
    if browser_name == 'Chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument(r'--user-data-dir=C:\Users\96142\AppData\Local\Google\Chrome\User Data')
    elif browser_name == 'Firefox':
        options = webdriver.FirefoxOptions()
    elif browser_name == 'Msedge':
        options = webdriver.EdgeOptions()
        # options.add_argument(r'--user-data-dir=C:\Users\96142\AppData\Local\Microsoft\Edge\User Data')

    # 禁用通知和密码保存弹窗
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2,
                'password_manager_enabled': False,
                'credentials_enable_service': False,
                'useAutomationExtension': False  # 去掉浏览器提示自动化黄条
            }
    }
    options.add_experimental_option('prefs', prefs)
    options_list = [
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/114.0.0.0 Safari/537.36',  # 某些网站反爬，加ua可能可规避
        '--disable-popup-blocking',  # 禁用浏览器弹窗
        '--disable-extensions', # 禁用插件
        '--disable-gpu',  # 禁用gpu
        '--disable-infobars',  # 禁用浏览器正在被自动化程序控制的提示
        '--ignore-certificate-errors-spki-list',
        '--no-sandbox',  # 禁用沙盒模式（因为权限会报错）
        'start-maximized'# gui模式下才生效
    ]
    for item in options_list:
        options.add_argument(item)

    # 等于true开启无头模式：
    if config.get('browser', 'headless') == 'true':
        options.add_argument('--headless')
        # 无头模式下才生效
        options.add_argument('--window-size=1920x1080')
    if browser_name == 'Chrome':
        driver = webdriver.Chrome(options=options)
    if browser_name == 'Msedge':
        driver = webdriver.Edge(options=options)
    if browser_name == 'Firefox':
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# 创建一个 function 范围的 fixture 关闭主窗口之外的窗口和 cookies
@pytest.fixture(scope='function', autouse=True)
def close_other_windows(browser):
    """
    关闭除了主窗口之外的其他窗口
    """
    original_window = browser.current_window_handle
    windows = browser.window_handles
    for window in windows:
        if window != original_window:
            browser.switch_to.window(window)
            browser.close()
    browser.switch_to.window(original_window)
    browser.delete_all_cookies()


def pytest_collection_modifyitems(items):
    """
    当ids用例别名乱码时,conftest里加
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    @pytest.mark.parametrize("input_title,",testdata["test_article"],ids=["新增文章"])
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    :param item:测试用例对象
    """
    outcome = yield
    # 获取调用结果的测试报告，返回一个report对象, report对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,
    # failed)
    report = outcome.get_result()
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            time.sleep(2)
            with allure.step("添加失败截图。。。"):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
