def test_average(x, y, z, average):  
    assert (x + y + z) / 3 == 8, "мухлюешь, не трогай переменные x, y, z"  
    assert average == 8, "Ошибка в вычислении среднего арифметического"  
  
def test_info(name, age, info):  
    assert info == f"Меня зовут {name}. Мне {age} лет.", "Ошибка в формате строки info"  
  
def test_string_methods(sentence, student_sentence):  
    assert student_sentence == sentence.title(), f"Должно получиться \"{sentence.title()}\", а у тебя \"{student_sentence}\""  
  
def test_number_conversion(number_str, number):  
    assert number == int(number_str), "Ошибка в преобразовании строки в число"  

def test_firazology(is_fixed: bool):
    assert is_fixed, "Не понимаю, тебе что, нужен X6-й?"
