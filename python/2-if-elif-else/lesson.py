# Задание 1: Определение четности числа  
# Напишите функцию is_even(n), которая принимает число и возвращает "Четное", если число четное, и "Нечетное", если нечетное.  
def is_even(n):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    result = None 
    return result
  
##################################################  
  
# Задание 2: Классификация возраста  
# Напишите функцию age_category(age), которая возвращает "Ребенок", если возраст меньше 13, "Подросток" если от 13 до 17, и "Взрослый" если 18 или больше.  
def age_category(age):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    result = None
    return result
  
##################################################  
  
# Задание 3: Проверка диапазона  
# Напишите функцию in_range(x, start, end), которая возвращает True, если x находится между start и end (включительно), иначе False.  
def in_range(x, start, end):  
    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    result = None
    return result
  
##################################################  

# Задание 4: Уведомления
# Напишите функцию notifications(settings), которая принимает строку с настройками и выводит сообщения:
# "Уведомления включены" если 'N' присутствует в строке
# "Звук включен" если 'S' присутствует в строке
# "Вибрация включена" если 'V' присутствует в строке
def notifications(settings):
    notifications_enabled_message = "Уведомления включены"
    sound_enabled_message = "Звук включен"
    haptic_enabled_message = "Вибрация включена"
    result = list()

    # TODO: Напишите ваш код здесь, в переменную result поместите ответ
    # Собирайте ответ в list.
    # Для того чтобы добавить элемент в list — используйте метод .append(), например так:
    # result.append(haptic_enabled_message)
    # В каком порядке вы соберете list — не важно, код всё поймет
    
    return result

##################################################  
  
# Код ниже не трогайте
try:  
    from examination import run_tests 
    run_tests(is_even, age_category, in_range, notifications)  
except AssertionError as e:  
    print(e)  