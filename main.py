# -*- coding:utf-8 -*-
import concurrent
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import platform
import pytest

from common.readConfig import config
from config.filepath import config_path


def kill_process(process_name):
    if platform.system() == 'Windows':
        result = subprocess.run(f'TASKKILL /F /IM {process_name}', shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        print(result.stdout)
        print(result.stderr)


def main_run(browser_name):
    config.set('browser', 'name', browser_name)
    config.set('browser', 'headless', 'true')
    with open(config_path, 'w', encoding='utf-8') as f:
        config.write(f)
    pytest.main(
        ['-sv', '-n=2', '--alluredir', './allure-results-' + browser_name, '--clean-alluredir'])
    kill_process(f'{browser_name}*')


def open_edge_report():
    os.system(f'allure generate ./allure-results-msedge/ -o ./allure-report-msedge/ --clean')
    os.system('allure open --port 10086 allure-report-msedge')


def open_chrome_report():
    os.system(f'allure generate ./allure-results-chrome/ -o ./allure-report-chrome/ --clean')
    os.system('allure open --port 10088 allure-report-chrome')


def open_report_as_serve(features: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        feature = features
        for feature in feature:
            executor.submit(feature)


if __name__ == '__main__':
    # main_run('msedge')
    # main_run('chrome')
    # open_report_as_serve([open_edge_report, open_chrome_report])
    main_run('chrome')
    open_report_as_serve([open_chrome_report])
