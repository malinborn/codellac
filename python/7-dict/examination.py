# examination.py  
  
def run_tests(merge_dicts, filter_dict, invert_dict, intersect_dicts):  
    # Тесты для merge_dicts  
    assert merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}, "❌ Ошибка в merge_dicts: случай 1"  
    assert merge_dicts({}, {'a': 1}) == {'a': 1}, "❌ Ошибка в merge_dicts: случай 2"  
    assert merge_dicts({'a': 1}, {}) == {'a': 1}, "❌ Ошибка в merge_dicts: случай 3"  
    print("merge_dicts прошел все тесты ✅")  
  
    # Тесты для filter_dict  
    assert filter_dict({'a': 5, 'b': 2, 'c': 10}, 4) == {'a': 5, 'c': 10}, "❌ Ошибка в filter_dict: случай 1"  
    assert filter_dict({'a': 1, 'b': 2}, 5) == {}, "❌ Ошибка в filter_dict: случай 2"  
    assert filter_dict({}, 0) == {}, "❌ Ошибка в filter_dict: случай 3"  
    print("filter_dict прошел все тесты ✅")  
  
    # Тесты для invert_dict  
    assert invert_dict({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}, "❌ Ошибка в invert_dict: случай 1"  
    assert invert_dict({}) == {}, "❌ Ошибка в invert_dict: случай 2"  
    assert invert_dict({'key': 'value'}) == {'value': 'key'}, "❌ Ошибка в invert_dict: случай 3"  
    print("invert_dict прошел все тесты ✅")  
      
    # Тесты для intersect_dicts  
    assert intersect_dicts({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 3, 'd': 4}) == {'a': 1}, "❌ Ошибка в intersect_dicts: случай 1"  
    assert intersect_dicts({'x': 10, 'y': 20}, {'x': 10, 'y': 20, 'z': 30}) == {'x': 10, 'y': 20}, "❌ Ошибка в intersect_dicts: случай 2"  
    assert intersect_dicts({'m': 3}, {'n': 3}) == {}, "❌ Ошибка в intersect_dicts: случай 3"  
    print("intersect_dicts прошел все тесты ✅")  