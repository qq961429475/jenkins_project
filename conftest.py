import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

browsers = {}
webdriver_mapping = {
    'chrome': webdriver.Chrome,
    'msedge': webdriver.Edge,
    'firefox': webdriver.Firefox,
}
# 遍历webdriver_mapping字典
for k, v in webdriver_mapping.items():
    # 检查配置中是否指定运行该浏览器
    if config.get('run_browser', k) == 'True':
        browsers[k] = v


@pytest.fixture(scope='session', params=list(browsers.keys()))
def browser(request):
    global driver
    browser_name = request.param
    WebDriver = browsers[browser_name]
    options = get_browser_options(browser_name)
    options.add_argument('start-maximized')
    if config['options']['headless'] == 'True':
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument(config.get('options', 'user-agent'))
    options.add_argument('--no-sandbox')
    driver = WebDriver(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def get_browser_options(browser_name):
    global options
    if browser_name == 'chrome':
        options = ChromeOptions()
    elif browser_name == 'msedge':
        options = EdgeOptions()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
    return options


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
    yield


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when in ('call', 'setup') and (report.skipped and not hasattr(report, 'wasxfail')) or report.failed:
        try:
            allure.step('失败截图')
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
        except Exception as e:
            print(f"截图失败: {e}")
