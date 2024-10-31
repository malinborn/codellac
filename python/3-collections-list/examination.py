def run_tests(reverse_list, find_max, append_to_list, concatenate_lists):  
    # Тесты для reverse_list  
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1], "Ошибка: функция reverse_list работает неправильно."  
    assert reverse_list([]) == [], "Ошибка: функция reverse_list должна возвращать пустой список для пустого входа."  
    assert reverse_list([1]) == [1], "Ошибка: функция reverse_list должна корректно обрабатывать списки с одним элементом."  
  
    # Тесты для find_max  
    assert find_max([1, 2, 3, 4, 5]) == 5, "Ошибка: функция find_max не нашла максимальное значение."  
    assert find_max([-1, -2, -3, -4]) == -1, "Ошибка: функция find_max не работает с отрицательными числами."  
    assert find_max([5]) == 5, "Ошибка: функция find_max должна возвращать единственный элемент для списков с одним элементом."  

    # Тесты для append_to_list  
    assert append_to_list([1, 2, 3], 4) == [1, 2, 3, 4], "Ошибка: функция append_to_list должна добавлять элемент, если его нет в списке."  
    assert append_to_list([1, 2, 3], 3) == [1, 2, 3], "Ошибка: функция append_to_list не должна добавлять элемент, если он уже есть в списке."  
    assert append_to_list([], 'a') == ['a'], "Ошибка: функция append_to_list не работает с пустым списком."  
  
    # Тесты для concatenate_lists  
    assert concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4], "Ошибка: функция concatenate_lists неправильно объединяет списки."  
    assert concatenate_lists([], [1, 2]) == [1, 2], "Ошибка: функция concatenate_lists должна корректно обрабатывать пустой первый список."  
    assert concatenate_lists([1, 2], []) == [1, 2], "Ошибка: функция concatenate_lists должна корректно обрабатывать пустой второй список."  