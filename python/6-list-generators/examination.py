def run_tests(square_even_numbers, extract_vowels, filter_short_words, duplicate_characters):  
    # Тесты для функции square_even_numbers  
    assert square_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 16, 36], "❌ Неправильный список квадратов четных чисел"  
    assert square_even_numbers([10, 15, 20]) == [100, 400], "❌ Неправильный список квадратов четных чисел"  
    print("square_even_numbers прошел все тесты ✅")  
  
    # Тесты для функции extract_vowels  
    assert extract_vowels("hello world") == ['e', 'o', 'o'], "❌ Неправильный список гласных"  
    assert extract_vowels("Python Programming") == ['y', 'o', 'o', 'a', 'i'], "❌ Неправильный список гласных"  
    print("extract_vowels прошел все тесты ✅")  
  
    # Тесты для функции filter_short_words  
    assert filter_short_words(["apple", "it", "ban", "cat"], 3) == ['it', 'ban', 'cat'], "❌ Неправильный список коротких слов"  
    assert filter_short_words(["dog", "elephant", "ant"], 3) == ['dog', 'ant'], "❌ Неправильный список коротких слов"  
    print("filter_short_words прошел все тесты ✅")  
  
    # Тесты для функции duplicate_characters  
    assert duplicate_characters("programming") == ['r', 'g', 'm'], "❌ Неправильный список повторяющихся символов"  
    assert duplicate_characters("banana") == ['a', 'n'], "❌ Неправильный список повторяющихся символов"  
    print("duplicate_characters прошел все тесты ✅")  