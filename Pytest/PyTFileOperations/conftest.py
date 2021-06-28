import pytest

@pytest.fixture(autouse=True)
def clean(): # Выдкрили закрили файл або підготували вміст файлу для проведення тесту
    f = open('base.txt', 'w')
    f.close()
    data = ['1\n', '2\n', '3\n', '4\n', '5']
    f = open('base.txt', 'a')
    for i in range(len(data)):
        f.write(data[i])
    f.close()
    print('done')
