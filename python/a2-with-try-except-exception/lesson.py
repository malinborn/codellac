class Timer:  
    """  
    Задание 1: Реализуйте класс Timer, который будет использоваться для измерения времени выполнения кода.  
    Класс должен реализовывать дандер-методы __enter__ и __exit__.  
    При использовании оператора with, __enter__ должен сохранять текущее время, а __exit__ должен  
    вычислять и выводить затраченное время.  
  
    Пример использования:  
    with Timer() as t:  
        # Код, время выполнения которого нужно измерить  
        sum(range(1000000))  
      
    :return: None  
    """  
    import time  

    def __enter__(self):  
        # тут должен быть ваш код 

        # а дальше не трогай
        return self  
  
    def __exit__(self, exc_type, exc_value, traceback):  
        # тут должен быть ваш код

        # а дальше не трогай
        print(f"Затраченное время: {elapsed_time:.6f} секунд")  
        return False  # Обработка исключений не нужна  
  
  
######################################################################  
  
def task_2_division(a, b):  
    """  
    Задание 2: Напишите функцию, которая выполняет деление двух чисел.  
    Если делитель равен нулю, функция должна выбрасывать исключение ZeroDivisionError с сообщением "Деление на ноль".  
      
    :param a: делимое  
    :param b: делитель  
    :return: результат деления  
    """  
    pass  # Здесь будет ваш код  


######################################################################  
  
def task_3_calculate_square_root(value):  
    """  
    Задание 3: Напишите функцию, которая вычисляет квадратный корень числа.  
    Используйте конструкцию try-except-else-finally.  
    Если переданное значение отрицательное, функция должна вернуть None  
    В блоке finally отобразите сообщение "Вычисление завершено".  
  
    :param value: число для вычисления квадратного корня  
    :return: квадратный корень числа  
    """ 
    pass  # Здесь будет ваш код  
  
  
######################################################################  
  
# Импорт тестов  
from examination import (  
    test_task_1_timer,  
    test_task_2_division,  
    test_task_3_calculate_square_root,  
)  
  
if __name__ == "__main__":  
    try:  
        # Тестирование других заданий  
        test_task_1_timer(Timer)  
        test_task_2_division(task_2_division)  
        test_task_3_calculate_square_root(task_3_calculate_square_root)  
    except AssertionError as e:  
        print(e)  