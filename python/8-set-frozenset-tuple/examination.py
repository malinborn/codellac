def run_tests(combine_sets_to_tuple, count_frozenset_occurrences, has_intersection, even_and_odd_sets, analyze_user_data):  
    # Тесты для combine_sets_to_tuple  
    assert combine_sets_to_tuple({1, 2}, {3, 4}) == (1, 2, 3, 4), "❌ combine_sets_to_tuple failed"  
    assert combine_sets_to_tuple(set(), {1, 2}) == (1, 2), "❌ combine_sets_to_tuple failed"  
    print("combine_sets_to_tuple passed ✅")  
  
    # Тесты для count_frozenset_occurrences  
    assert count_frozenset_occurrences([[1, 2], [2, 1], [3, 4], [1, 2]]) == {frozenset({1, 2}): 3, frozenset({3, 4}): 1}, "❌ count_frozenset_occurrences failed"  
    assert count_frozenset_occurrences([[1], [2], [1, 2], [2, 1], [1]]) == {frozenset({1}): 2, frozenset({2}): 1, frozenset({1, 2}): 2}, "❌ count_frozenset_occurrences failed"  
    assert count_frozenset_occurrences([]) == {}, "❌ count_frozenset_occurrences failed"  
    print("count_frozenset_occurrences passed ✅")  
  
    # Тесты для has_intersection  
    assert has_intersection({1, 2}, {2, 3}) == True, "❌ has_intersection failed"  
    assert has_intersection({1, 2}, {3, 4}) == False, "❌ has_intersection failed"  
    print("has_intersection passed ✅")  
  
    # Тесты для even_and_odd_sets  
    assert even_and_odd_sets([1, 2, 3, 4]) == ({2, 4}, {1, 3}), "❌ even_and_odd_sets failed"  
    assert even_and_odd_sets([1, 3, 5]) == (set(), {1, 3, 5}), "❌ even_and_odd_sets failed"  
    print("even_and_odd_sets passed ✅")  
  
    # Тесты для analyze_user_data  
    assert analyze_user_data([  
        {'name': 'Alice', 'age': 30, 'hobbies': ['chess', 'reading']},  
        {'name': 'Bob', 'age': 25, 'hobbies': ['chess', 'gaming']},  
        {'name': 'Charlie', 'age': 30, 'hobbies': ['reading', 'gaming']}  
    ]) == (  
        {  
            frozenset({'chess', 'reading'}): ('Alice',),  
            frozenset({'chess', 'gaming'}): ('Bob',),  
            frozenset({'reading', 'gaming'}): ('Charlie',)  
        },  
        {25, 30}  
    ), "❌ analyze_user_data failed"  
    print("analyze_user_data passed ✅")  