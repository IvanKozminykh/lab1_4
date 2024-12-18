def count_common_elements(*lists):
    """
    Принимает на вход N списков и возвращает количество одинаковых элементов в них.

    :param lists: Переменное количество списков.
    :return: Количество общих элементов.
    """
    if not lists:
        return 0

    # Преобразуем каждый список во множество и находим их пересечение
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements &= set(lst)

    return len(common_elements)
