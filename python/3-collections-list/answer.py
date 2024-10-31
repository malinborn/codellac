# Задание 1: Reverse List  
# Напишите функцию reverse_list(lst), которая принимает список и возвращает его в обратном порядке.  
def reverse_list(lst):  
    return lst[::-1]
  
############################################################  
  
# Задание 2: Find Maximum  
# Напишите функцию find_max(lst), которая возвращает максимальное значение в списке.  
def find_max(lst):  
    return sorted(lst)[-1];
  
############################################################  
  
# Задание 3: Append Unique to List  
# Напишите функцию append_to_list(lst, item), которая добавляет элемент item в конец списка lst,  
# только если этого элемента там еще нет.  
# Верните обновленный список
def append_to_list(lst, item):  
    if item not in lst:
        lst.append(item)
    return lst
  
############################################################  
  
# Задание 4: Concatenate Lists  
# Напишите функцию concatenate_lists(lst1, lst2), которая возвращает новый список,   
# являющийся результатом объединения lst1 и lst2.  
def concatenate_lists(lst1, lst2):  
    return lst1 + lst2
  
############################################################  
  
# Дальше код не пиши 
from examination import run_tests  
try:  
    run_tests(reverse_list, find_max, append_to_list, concatenate_lists)  
    print("✅ Тесты прошли!")
except AssertionError as e:  
    print(e)  