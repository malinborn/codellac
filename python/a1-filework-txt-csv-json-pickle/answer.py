import csv  
import json  
import pickle  
import os
from examination import Student
  

def task_1_read_csv(file_path: str) -> list[dict[str, any]]:  
    """  
    Задание 1: Прочитать данные из CSV файла и вернуть их в виде списка словарей.  
    Каждый словарь должен представлять одну строку, где ключи - это заголовки колонок.  
      
    Пример входных данных:  
    'students.csv' (содержит колонки: name, age, grades)  
      
    Ожидаемый результат:  
    [{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]},   
     {'name': 'Bob', 'age': 22, 'grades': [78, 81, 80]}]  
    """  
    with open(file_path, "r") as fp: 
        return [x for x in csv.DictReader(fp)]
  
  
############################################################  
  
  
def task_2_write_json(data: list[dict[str, any]], file_path: str) -> None:  
    """  
    Задание 2: Записать данные в JSON файл.  
      
    Пример входных данных:  
    data = [{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}]  
      
    Ожидается, что данные будут записаны в файл 'students.json'.  
    """  
    with open(file_path, "w") as fp: 
        json.dump(data, fp)
  
  
############################################################  
  
  
def task_3_pickle_data(data: list[Student], file_path: str) -> None:  
    """  
    Задание 3: Сериализовать данные с помощью модуля pickle и записать в файл.  
      
    Пример входных данных:  
    data = [
        Student(name='Alice', age=20, grades=[90, 85, 88]),
        Student(name='Bob', age=22, grades=[2, 2, 8]) 
    ]
      
    Ожидается, что данные будут записаны в файл 'students.pickle'.  
    """  
    with open(file_path, "wb") as fp:
        pickle.dump(data, fp)
  
  
############################################################  
  
  
def task_4_load_pickle(file_path: str) -> list[Student]:  
    """  
    Задание 4: Десериализовать данные из pickle файла и вернуть их.  
      
    Пример входных данных:  
    'students.pickle'  
      
    Ожидаемый результат:  
    [{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}]  
    """  
    with open(file_path, "rb") as fp:
        return pickle.load(fp)
  
  
############################################################  
  
  
def task_5_write_txt(data: list[dict[str, any]], file_path: str) -> None:  
    """  
    * [Не обязательное] Задание 5: Записать данные в текстовый файл.  
      
    Пример входных данных:  
    data = [{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}]  
    Если передано несколько словарей, они должны записать в файл
    строки друг за другом. 
    При этом, ключи могут быть разными
      
    Ожидается, что данные будут записаны в файл 'students.txt' в формате:  
    Name: Alice, Age: 20, Grades: [90, 85, 88]  
    """  
    with open(file_path, "w") as fp: 
        result = ""
        for dict_i in data:
            chains = []
            for key in dict_i:
                chains.append(f"{key}: {dict_i[key]}")
            result += f'{", ".join(chains)}\n'
        fp.write(result) 
  
  
############################################################  
# Код ниже не трогай
############################################################  
  
from examination import test_tasks, generate_test_csv

if not os.path.exists('students.csv'):  
    generate_test_csv('students.csv')  
  
try:   
    test_tasks(task_1_read_csv, task_2_write_json, task_3_pickle_data, task_4_load_pickle, task_5_write_txt)  
except AssertionError as e:  
    print(e)  