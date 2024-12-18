import pytest
from lib import count_common_elements

def test_count_common_elements():
    # Тест 1: Общие элементы в нескольких списках
    assert count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]) == 1

    # Тест 2: Полное совпадение списков
    assert count_common_elements([1, 2], [1, 2], [1, 2]) == 2

    # Тест 3: Нет общих элементов
    assert count_common_elements([1, 2], [3, 4], [5, 6]) == 0

    # Тест 4: Один список передан
    assert count_common_elements([1, 2, 3]) == 3

    # Тест 5: Пустой список
    assert count_common_elements([]) == 0

    # Тест 6: Несколько пустых списков
    assert count_common_elements([], [], []) == 0

    # Тест 7: Списки с одинаковыми элементами, но разной длины
    assert count_common_elements([1, 2, 3], [1, 2], [1]) == 1

    # Тест 8: Списки с разными типами данных
    assert count_common_elements([1, 'a', 3.5], ['a', 3.5, 4], [3.5, 'a']) == 2

    # Тест 9: Нет аргументов
    assert count_common_elements() == 0

if __name__ == "__main__":
    pytest.main()
