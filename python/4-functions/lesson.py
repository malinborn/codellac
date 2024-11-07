# Сигнатуры именованных функций 

def create_dog(): 
	"""  
    Задание: воспроизведите сигнатуру этой функции.  
  
    1. Названия аргументов:  
       - Первый: имя собаки (str).  
       - Второй: возраст собаки (int).  
       - Третий: цвет шерсти (str, по умолчанию "brown").  
       - Четвертый: порода (str, по умолчанию "malinois").  
  
    2. Аннотация возвращаемого типа: str.  
    """  
	message = f"So the dog's name is {name}. "
	message += f"The dog is {age} years old. "

	if colour.lower() == "brown": 
		message += f"It has the common, would even say \"default\", {colour} fur. "
	else: 
		message += f"It has beautiful {colour} fur. "

	if breed.lower() == "malinois":
		message += f"The dog is of a famous, though \"default\" breed — {breed}!"
	else: 
		message += f"The dog is of an interesting breed: {breed}"

	return message

# ##################################################  

# Задание 1: Фильтрация списка  
# Используйте lambda-функцию для фильтрации четных чисел из списка.  
# Пример: [1, 2, 3, 4, 5, 6] -> [2, 4, 6]  
  
def filter_even_numbers(numbers: list[int, ...]) -> list[int, ...]:  
    # Напишите свою lambda-функцию и используйте встроенную функцию filter  
    pass  
  
# ##################################################  
  
# Задание 2: Маппинг строки в список длин  
# Используйте lambda-функцию для преобразования списка строк в список их длин.  
# Пример: ["apple", "banana", "cherry"] -> [5, 6, 6]  
  
def map_strings_to_lengths(strings: list[str, ...]) -> list[int, ...]:  
    # Напишите свою lambda-функцию и используйте встроенную функцию map  
    pass  
  
# ##################################################  
  
# Задание 3: Сортировка по второму элементу  
# Используйте lambda-функцию для сортировки списка кортежей по второму элементу в каждом кортеже.  
# Пример: [(1, 3), (2, 1), (3, 2)] -> [(2, 1), (3, 2), (1, 3)]  
  
def sort_tuples_by_second_element(tuples: list[tuple]) -> list[tuple, ...]:  
    # Напишите свою lambda-функцию и используйте метод sort или sorted  
    pass  
  
# ##################################################  
  
# Запускаю тесты, не трогай код ниже
from examination import run_named_function_tests, check_signature, run_lambda_tests
delimeter = "########################"
print(delimeter + " сигнатура функции " + delimeter)
run_named_function_tests(create_dog)
check_signature(create_dog)

print(delimeter + " lambda-функции " + delimeter)
try:  
    run_lambda_tests(filter_even_numbers, map_strings_to_lengths, sort_tuples_by_second_element)  
except AssertionError as e:  
    print(e)  
