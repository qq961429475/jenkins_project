from pathlib import Path

# 项目根路径
project_root = Path(__file__).parent.parent

#
config_path = project_root / 'config' / 'config.ini'
# 用例数据路径
case_data_path = project_root / 'test_case' / 'data'
# 百度cookie
baidu_cookie = project_root / 'data' / 'baidu_cookies.json'
# DB配置路径
db_config_path = project_root / 'config' / 'db.ini'
