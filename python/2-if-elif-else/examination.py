def run_tests(taks1, task2, task3, task4):  
    # Тесты для is_even  
    assert taks1(2) == "Четное", "Ошибка в is_even(2)"  
    assert taks1(3) == "Нечетное", "Ошибка в is_even(3)"  
      
    # Тесты для age_category  
    assert task2(10) == "Ребенок", "Ошибка в age_category(10)"  
    assert task2(15) == "Подросток", "Ошибка в age_category(15)"  
    assert task2(20) == "Взрослый", "Ошибка в age_category(20)"  
      
    # Тесты для in_range  
    assert task3(5, 1, 10) == True, "Ошибка в in_range(5, 1, 10)"  
    assert task3(0, 1, 10) == False, "Ошибка в in_range(0, 1, 10)"  
    assert task3(10, 1, 10) == True, "Ошибка в in_range(10, 1, 10)"  
      
    # Тесты для notifications  
    assert sorted(task4("NS")) == sorted(["Уведомления включены", "Звук включен"]), "Ошибка в notifications('NS')"  
    assert sorted(task4("NV")) == sorted(["Уведомления включены", "Вибрация включена"]), "Ошибка в notifications('NV')"  
    assert sorted(task4("SV")) == sorted(["Звук включен", "Вибрация включена"]), "Ошибка в notifications('SV')"  
