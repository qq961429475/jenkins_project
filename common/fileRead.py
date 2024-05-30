import os

import yaml
from jsonpath import jsonpath

from config.filepath import case_data_path


def read_yaml(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data


def load_case_data(filename):
    for root, dirs, files in os.walk(case_data_path):
        if not filename.endswith('.yaml'):
            filename = filename + '.yaml'
        with open(root + '/' + filename, 'r', encoding='utf-8') as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data


def load_ids(filename):
    data = load_case_data(filename)
    return jsonpath(data, '$..ids')


if __name__ == '__main__':
    print(load_ids('test_02'))
