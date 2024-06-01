# -*- coding:utf-8 -*-
import os
import platform
import shutil
import subprocess
from configparser import ConfigParser


def kill_process(process_name):
    if platform.system() == 'Windows':
        result = subprocess.run(f'TASKKILL /F /IM {process_name}', shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        print(result.stdout)
        print(result.stderr)


def main(run_browser: list = None, thread_num=0, rerun_num=0, maxfail=0, headless=None, other: list = None):
    config = ConfigParser()
    config.read('config.ini')
    browser_list = ['chrome', 'msedge', 'firefox']
    for browser in browser_list:
        config.set('run_browser', browser, str(browser in run_browser))
    if headless is not None:
        config.set('options', 'headless', str(headless))
    with open('config.ini', 'w') as f:
        config.write(f)
    command = ['pytest',
               '-sv',
               '-n=' + str(thread_num),
               '--reruns=' + str(rerun_num),
               '--maxfail=' + str(maxfail),
               '--alluredir', './allure-results', '--clean-alluredir']
    if other:
        for item in other:
            command.append(item)
    subprocess.run(command)

    os.system('allure generate ./allure-results -o ./allure-report --clean')
    os.system('allure open --port 10086 ./allure-report')


if __name__ == '__main__':
    kill_process('msedge*')
    kill_process('chrome*')
    main(
        # 要测试的浏览器['chrome','msedge','firefox']
        run_browser=['chrome'],
        # 是否无头模式
        headless=True,
        # 多线程，n=线程数
        thread_num=2,
        # 失败重试次数,为0不重跑
        rerun_num=1,
        # 失败n次就停止，为0不起作用
        maxfail=5,
        # other command
        other=['./test_case/test_title.py']
    )
