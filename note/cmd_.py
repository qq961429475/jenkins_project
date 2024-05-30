# -*- coding: utf-8 -*-
import subprocess


def kill_process(process_name):
    result = subprocess.run(f'TASKKILL /F /IM {process_name}', shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    print(result.stdout)
    print(result.stderr)


if __name__ == '__main__':
    kill_process('msed*')
    kill_process('chrome*')
