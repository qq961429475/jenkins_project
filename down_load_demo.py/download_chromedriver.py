import os
import re
import shutil
import zipfile

import requests
import urllib3
from tqdm import tqdm

urllib3.disable_warnings()


def get_download_url():
    # 获取chromedriver下载地址
    res = requests.get('https://getwebdriver.com/chromedriver#stable')
    chrome_deriver_url = re.search(
        'https://storage.googleapis.com/chrome-for-testing-public/[0-9.]+/win64/chromedriver-win64.zip', res.text)[0]
    # 获取edgeDriver下载地址
    res = requests.get('https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/?form=MA13LH')
    edge_driver_url = re.search('https://msedgedriver.azureedge.net/[0-9.]+/edgedriver_win64.zip', res.text)[0]

    urls = [chrome_deriver_url, edge_driver_url, ]
    return urls


def download_driver_and_move(_url: str):
    _res = requests.get(
        url=_url, verify=False, allow_redirects=True, stream=True)
    filename = _url.split('/')[-1]
    print(filename, '开始下载')
    file_size = int(_res.headers['Content-Length'])
    num_bars = int(file_size / 1024)
    with open(filename, 'wb') as f:
        # f.write(_res.content)
        for chunk in tqdm(_res.iter_content(chunk_size=1024), total=num_bars, unit='KB', desc=_url.split('/')[-1],
                          leave=True):
            f.write(chunk)
    print('下载成功')
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        # 解压文件到python目录
        zip_ref.extractall(r'C:\Users\96142\AppData\Local\Programs\Python\Python312')
    if os.path.exists(r"C:\Users\96142\AppData\Local\Programs\Python\Python312\chromedriver-win64\chromedriver.exe"):
        shutil.move(r"C:\Users\96142\AppData\Local\Programs\Python\Python312\chromedriver-win64\chromedriver.exe",
                    r"C:\Users\96142\AppData\Local\Programs\Python\Python312\chromedriver.exe")
        shutil.rmtree(r"C:\Users\96142\AppData\Local\Programs\Python\Python312\chromedriver-win64")
        print('chromedriver.exe移动成功')


def download():
    _urls = get_download_url()
    for url in _urls:
        download_driver_and_move(url)


if __name__ == '__main__':
    download()
    print('下载完成')
