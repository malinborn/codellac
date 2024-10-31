# Задание 1: Определение четности числа  
# Напишите функцию is_even(n), которая принимает число и возвращает "Четное", если число четное, и "Нечетное", если нечетное.  
def is_even(n):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    result = "Четное" if n % 2 == 0 else "Нечетное"
    return result
  
##################################################  
  
# Задание 2: Классификация возраста  
# Напишите функцию age_category(age), которая возвращает "Ребенок", если возраст меньше 13, "Подросток" если от 13 до 17, и "Взрослый" если 18 или больше.  
def age_category(age):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    if age < 13: 
        result = "Ребенок"
    elif age > 13 and age < 17: 
        result = "Подросток"
    else: 
        result = "Взрослый"
    return result
  
##################################################  
  
# Задание 3: Проверка диапазона  
# Напишите функцию in_range(x, start, end), которая возвращает True, если x находится между start и end (включительно), иначе False.  
def in_range(x, start, end):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    result = False
    range_numbers = list(range(start, end + 1))
    if x in range_numbers:
        result = True
    return result
  
##################################################  

# Задание 4: Уведомления
# Напишите функцию notifications(settings), которая принимает строку с настройками и выводит сообщения:
# "Уведомления включены" если 'N' присутствует в строке
# "Звук включен" если 'S' присутствует в строке
# "Вибрация включена" если 'V' присутствует в строке
def notifications(settings):
    notifications_enabled_message = "Уведомления включены"  # For N
    sound_enabled_message = "Звук включен"  # For S
    haptic_enabled_message = "Вибрация включена"  # For V
    result = list()

    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    # Собирайте ответ в list.
    # Для того чтобы добавить элемент в list — используйте метод .append(), например так:
    # result.append(haptic_enabled_message)
    # В каком порядке вы соберете list — не важно, код всё поймет

    if "N" in settings:
        result.append(notifications_enabled_message)
    if "S" in settings:
        result.append(sound_enabled_message)
    if "V" in settings: 
        result.append(haptic_enabled_message)
    
    return result

##################################################  
  
# Код ниже не трогайте
try:  
    from examination import run_tests 
    run_tests(is_even, age_category, in_range, notifications)  
    print("Все тесты пройдены!")
except AssertionError as e:  
    print(e)  