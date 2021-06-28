import pytest_main
import pytest


@pytest.mark.parametrize("val, res", [(10, 100), (5, 25)]) #Распаковка кортежей в val, res
def test_1(val, res):
    assert pytest_main.square(val) == res

@pytest.mark.parametrize("a, b, result", [(5, 2, 2.5), (15, 0, "Error")])
def test_2(a, b, result):
    assert pytest_main.division(a, b) == result


def test_3_divbyzero(a=5, b=0):
    with pytest.raises(ZeroDivisionError): # ожидаем ошибку, если ошибка возникает то тест проходит.
        pytest_main.divisionbzero(a, b)

