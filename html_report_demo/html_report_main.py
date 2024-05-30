import pathlib
from datetime import datetime

from XTestRunner import HTMLTestRunner


class Env:
    now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    report_name = pathlib.Path.cwd() / 'report' / f'report_{now}.html'


# verbosity：报告的详细程度，只有0、1、2 ，2为最详细
if __name__ == '__main__':
    # env = Env()
    # suit = unittest.defaultTestLoader.discover(start_dir='../html_report_demo', pattern='test*', )
    # report = env.report_name
    # with open(report, "wb") as f:
    #     runner = HTMLTestRunner(stream=f, verbosity=2, title="XXX自动化测试报告", tester='gaofei',
    #                             description="欢迎关注公众号：大森玩测试", language='zh-CN')
    #
    #     runner.run(suit)
    runner = HTMLTestRunner()
    # runner.send_email(
    #     to='wuggfox@foxmail.com',
    #     user="wuggfox@foxmail.com",
    #     password="zxcvbnm123.",
    #     # password="gqqzbwyedhjpbeef",
    #     host="smtp.qq.com",
    #     attachments=r'C:\Users\96142\Desktop\TestProject\html_report_demo\report\report_2024-05-15_19_03_39.html',
    #     ssl=False,
    #     port=465
    # )
