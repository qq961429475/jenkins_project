import logging
from logging.handlers import RotatingFileHandler

from common.readConfig import config, config_path

config.read(config_path, encoding='utf-8')
backupCount = int(config.get1('logger', 'backupCount'))
print_to_console = config.get1('logger', 'print_to_console')


def get_logger(log_path):
    """

    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s')
    # 创建一个handler，用于写入日志文件
    file_handler = RotatingFileHandler(log_path, mode='a', maxBytes=1024 * 1024 * 10, backupCount=backupCount)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # 创建一个handler，用于输出到控制台
    if print_to_console == 'True':
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger
