import pytest

test_data_list = [i for i in range(1, 10)]


@pytest.mark.parametrize("i", test_data_list)
def test_multithreading(i, browser):
    browser.get('https://www.baidu.com')
    assert 1 == 1
