from configparser import ConfigParser

from config.filepath import config_path

config = ConfigParser()
config.read(config_path, encoding='utf-8')
