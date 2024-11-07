def run_named_function_tests(create_dog_function):  
    try:  
        assert create_dog_function("Buddy", 3) == (  
            "So the dog's name is Buddy. "  
            "The dog is 3 years old. "  
            "It has the common, would even say \"default\", brown fur. "  
            "The dog is of a famous, though \"default\" breed — malinois!"  
        )  
        print("Test 1 passed ✅")  
    except Exception:  
        print("Test 1 failed ❌")  
  
    try:  
        assert create_dog_function("Max", 5, colour="black") == (  
            "So the dog's name is Max. "  
            "The dog is 5 years old. "  
            "It has beautiful black fur. "  
            "The dog is of a famous, though \"default\" breed — malinois!"  
        )  
        print("Test 2 passed ✅")  
    except Exception:  
        print("Test 2 failed ❌")  
  
    try:  
        assert create_dog_function("Charlie", 2, breed="labrador") == (  
            "So the dog's name is Charlie. "  
            "The dog is 2 years old. "  
            "It has the common, would even say \"default\", brown fur. "  
            "The dog is of an interesting breed: labrador"  
        )  
        print("Test 3 passed ✅")  
    except Exception:  
        print("Test 3 failed ❌")  
  
    try:  
        assert create_dog_function("Bella", 4, colour="golden", breed="retriever") == (  
            "So the dog's name is Bella. "  
            "The dog is 4 years old. "  
            "It has beautiful golden fur. "  
            "The dog is of an interesting breed: retriever"  
        )  
        print("Test 4 passed ✅")  
    except Exception:  
        print("Test 4 failed ❌")  
  
    try:  
        assert create_dog_function("Lucy", 1, colour="BROWN", breed="MALINOIS") == (  
            "So the dog's name is Lucy. "  
            "The dog is 1 years old. "  
            "It has the common, would even say \"default\", BROWN fur. "  
            "The dog is of a famous, though \"default\" breed — MALINOIS!"  
        )  
        print("Test 5 passed ✅")  
    except Exception:  
        print("Test 5 failed ❌")  
  
    try:  
        assert create_dog_function("", 0, colour="purple", breed="unicorn") == (  
            "So the dog's name is . "  
            "The dog is 0 years old. "  
            "It has beautiful purple fur. "  
            "The dog is of an interesting breed: unicorn"  
        )  
        print("Test 6 passed ✅")  
    except Exception:  
        print("Test 6 failed ❌")  


def check_signature(create_dog):
    import inspect 
    
    # Определение ожидаемой сигнатуры
    expected_signature = inspect.Signature(
        parameters=[
            inspect.Parameter("name", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=str),
            inspect.Parameter("age", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=int),
            inspect.Parameter("colour", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=str, default="brown"),
            inspect.Parameter("breed", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=str, default="malinois")
        ],
        return_annotation=str
    )
    
    # Получение реальной сигнатуры функции
    actual_signature = inspect.signature(create_dog)
    
    # Проверка совпадения
    if actual_signature == expected_signature:
        print("Сигнатура функции соответствует ожидаемой ✅")
    else:
        print("Сигнатура функции не соответствует ожидаемой ❌")
    

def run_lambda_tests(filter_even_numbers, map_strings_to_lengths, sort_tuples_by_second_element):  
    # Тесты для filter_even_numbers  
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6], "Ошибка в filter_even_numbers — должны вернуться только четные ❌"  
    assert filter_even_numbers([1, 3, 5]) == [], "Ошибка в filter_even_numbers, если список состоит из нечетных — должен вернуться пустой список ❌"  
    print("filter_even_numbers — passed ✅")
  
    # Тесты для map_strings_to_lengths  
    assert map_strings_to_lengths(["apple", "banana", "cherry"]) == [5, 6, 6], "Ошибка в map_strings_to_lengths — неверно считаешь ❌"  
    assert map_strings_to_lengths([""]) == [0], "Ошибка в map_strings_to_lengths — пустая строка должна вернуть ноль ❌"  
    print("map_strings_to_lengths — passed ✅")
  
    # Тесты для sort_tuples_by_second_element  
    assert sort_tuples_by_second_element([(1, 3), (2, 1), (3, 2)]) == [(2, 1), (3, 2), (1, 3)], "Ошибка в sort_tuples_by_second_element ❌"  
    assert sort_tuples_by_second_element([(1, 2), (2, 2), (3, 1)]) == [(3, 1), (1, 2), (2, 2)], "Ошибка в sort_tuples_by_second_element — если несколько вторых элементов равны, нужно дополнительно отсортировать по первому элементу ❌"  
    print("sort_tuples_by_second_element — passed ✅")
