from configparser import ConfigParser

import pymysql

from config.filepath import db_config_path


class OperateDB:
    def __init__(self, db_name):
        # 从配置文件里读取数据库服务器IP  账号 密码.....
        config = ConfigParser()
        config.read(db_config_path)
        host = config[db_name]['host']
        port = int(config[db_name]['port'])
        user = config[db_name]['user']
        passwd = config[db_name]['passwd']
        db = config[db_name]['database']
        charset = config[db_name]['charset']
        try:
            self.con = pymysql.connect(host=host, port=port, user=user,
                                       password=passwd, database=db, charset=charset)
        except Exception as e:
            print('初始化数据库连接失败：%s' % e)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self  # 返回类的实例，以便在with块中使用

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """关闭游标和连接"""
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()

    def execute_query(self, sql, params=None):
        try:
            if params is not None:
                self.cur.execute(sql, params)

            else:
                self.cur.execute(sql)
            if sql.upper().startswith(('SELECT', 'SHOW')):
                return self.cur.fetchall()
            else:
                self.con.commit()
                return '执行成功'
        except pymysql.Error as e:
            self.con.rollback()
            print(f"An error occurred: {e}")
