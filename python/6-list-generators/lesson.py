def square_even_numbers(numbers):  
    """  
    Возвращает список квадратов четных чисел из переданного списка.  
    Пример:  
    >>> square_even_numbers([1, 2, 3, 4])  
    [4, 16]  
    """  
    pass  # Напишите код здесь  
  
# ############################################################  
  
def extract_vowels(text):  
    """  
    Возвращает список всех гласных букв в строке.  
    Пример:  
    >>> extract_vowels("hello world")  
    ['e', 'o', 'o']  
    """  
    pass  # Напишите код здесь  
  
# ############################################################  
  
def filter_short_words(words, max_length):  
    """  
    Возвращает список слов, длина которых меньше или равна max_length.  
    Пример:  
    >>> filter_short_words(["apple", "it", "ban", "cat"], 3)  
    ['it', 'ban', 'cat']  
    """  
    pass  # Напишите код здесь  
  
# ############################################################  
  
def duplicate_characters(text):  
    """  
    *** Сложное задание ***  
    Возвращает список символов, которые повторяются в строке более одного раза.  
    Пример:  
    >>> duplicate_characters("programming")  
    ['r', 'g', 'm']  
    """  
    pass  # Напишите код здесь  
  
# ############################################################  
  
# Импортируем тесты и запускаем их  
from examination import run_tests  
  
try:  
    run_tests(square_even_numbers, extract_vowels, filter_short_words, duplicate_characters)  
except AssertionError as e:  
    print(e)  