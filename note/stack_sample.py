import inspect
import sys
import traceback


def get_func_name():
    """
    spect.currentframe(）返回当前的堆栈帧，
    f_back属性返回调用当前方法的方法的堆栈帧，
    f_code.co_name属性返回方法名。
    """
    return inspect.currentframe().f_back.f_code.co_name


def get_func_name_two():
    return sys._getframe().f_back.f_code.co_name


def get_func_name_three():
    """
    traceback.extract_stack(None，2）返回当前的堆栈信息，其中第一个元素是当前方法的堆栈信息,通过下标取出方法名。
    """
    return traceback.extract_stack(None, 2)[0][2]
