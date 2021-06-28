# для цього файлу модифікуєм конфіг щоб робота відбувалася саме в цій дерикторії, або тест проходив тільки
# з допомогою однієї функції!!!
import main_prog as mp
import pytest

@pytest.mark.parametrize("file", [('base.txt'),])
def test_1(file):
    assert mp.open_and_modyfy(file) == ['1\n', '2\n', '3\n', '4\n', '5']

def test_2():
    assert mp.open_and_modyfy('base.txt') == ['1\n', '2\n', '3\n', '4\n', '5']