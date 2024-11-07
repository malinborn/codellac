def run_for_tests(join_long_strings, double_even_numbers, above_average):  
    # Тесты для join_long_strings  
    assert join_long_strings(["hello", "hi", "yes", "world"]) == "hello world", "❌ join_long_strings не работает правильно"  
    assert join_long_strings(["a", "b", "c", "de", "fg"]) == "", "❌ join_long_strings не работает правильно"  
    print("join_long_strings tests passed ✅")  
  
    # Тесты для double_even_numbers  
    assert double_even_numbers([1, 2, 3, 4]) == [1, 4, 3, 8], "❌ double_even_numbers не работает правильно"  
    assert double_even_numbers([0, 5, 6, 7]) == [0, 5, 12, 7], "❌ double_even_numbers не работает правильно"  
    print("double_even_numbers tests passed ✅")  
  
    # Тесты для above_average  
    assert above_average([1, 3, 5, 7]) == [5, 7], "❌ above_average не работает правильно"  
    assert above_average([10, 20, 30, 40]) == [30, 40], "❌ above_average не работает правильно"  
    print("above_average tests passed ✅")  

def run_while_tests(sum_numbers_while, sum_digits_to_single, is_palindrome_while):  
    # Тесты для функции sum_numbers_while  
    assert sum_numbers_while(5) == 15, "❌ Ошибка в sum_numbers_while: 5"  
    assert sum_numbers_while(0) == 0, "❌ Ошибка в sum_numbers_while: 0"  
    assert sum_numbers_while(1) == 1, "❌ Ошибка в sum_numbers_while: 1"  
    print("sum_numbers_while ✅")  
  
    # Тесты для функции sum_digits_to_single
    assert sum_digits_to_single(9875) == 2, "❌ Ошибка в sum_digits_to_single: 9875"
    assert sum_digits_to_single(123) == 6, "❌ Ошибка в sum_digits_to_single: 123"
    assert sum_digits_to_single(9) == 9, "❌ Ошибка в sum_digits_to_single: 9"
    assert sum_digits_to_single(0) == 0, "❌ Ошибка в sum_digits_to_single: 0"
    print("sum_digits_to_single ✅")
  
    # Тесты для функции is_palindrome_while
    assert is_palindrome_while("A man a plan a canal Panama") == True, "❌ Ошибка в is_palindrome_while: 'A man a plan a canal Panama'"
    assert is_palindrome_while("racecar") == True, "❌ Ошибка в is_palindrome_while: 'racecar'"
    assert is_palindrome_while("hello") == False, "❌ Ошибка в is_palindrome_while: 'hello'"
    assert is_palindrome_while("") == True, "❌ Ошибка в is_palindrome_while: ''"
    print("is_palindrome_while ✅")