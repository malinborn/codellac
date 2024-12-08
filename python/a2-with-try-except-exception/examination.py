import io
from unittest.mock import patch 
from contextlib import redirect_stdout


def test_task_1_timer(cls): 
    try: 
        with cls() as timer:  
            [x for x in range(1_000_000)]
            # Тестируем, что класс Timer работает без исключений 
            assert isinstance(timer, cls), "❌ Ошибка: объект не является экземпляром Timer"
    except TypeError: 
        print("❌ Ошибка: переменная elapsed должна содержать объект time")
    except NameError:
        print("❌ Ошибка: сделай переменную elapsed_time, она там в принте написана, видишь же?")
    else: 
        print("task_1_timer тест прошел ✅")  
  
  
def test_task_2_division(func):  
    assert func(10, 2) == 5, "❌ Ошибка: 10 / 2 должно быть равно 5"  
      
    try:  
        func(10, 0)  
        assert False, "❌ Ошибка: должно было вызвать исключение о делении на ноль"  
    except ZeroDivisionError:  
        pass  # Исключение ожидается  
  
    print("task_2_division тест прошел ✅")  
  
  
def test_task_3_calculate_square_root(func):  
    with redirect_stdout(io.StringIO()):
        assert func(4) == 2, "❌ Ошибка: корень из 4 должен быть 2"  
      
    try:  
        assert func(-1) == None, "❌ Ошибка: должно было вернуть None и вывести сообщение"  
    except ValueError:  
        raise AssertionError("❌ Ошибка: не забудь обработать исключение ValueError, функция sqrt выбросит его в ответ на отрицательное значение")

    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        func(9)  # Вычисляем корень из 9
        output = fake_out.getvalue()
        assert "Вычисление завершено" in output, "❌ Ошибка: сообщение 'Вычисление завершено' не было выведено"

    print("task_3_calculate_square_root тест прошел ✅")  