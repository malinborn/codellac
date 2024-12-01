import csv  
import json  
import pickle  
import os  
from dataclasses import dataclass


@dataclass  
class Student:  
    name: str  
    age: int  
    grades: list[int] 

  
def generate_test_csv(file_path: str) -> None:  
    """  
    Генерирует CSV файл с тестовыми данными для первого задания.  
    """  
    data = [  
        {'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]},  
        {'name': 'Bob', 'age': 22, 'grades': [78, 81, 80]},  
        {'name': 'Charlie', 'age': 19, 'grades': [92, 95, 90]}  
    ]  
  
    # Запись в CSV файл  
    with open(file_path, mode='w', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow(['name', 'age', 'grades'])  # Заголовки колонок  
        for student in data:  
            writer.writerow([student['name'], student['age'], json.dumps(student['grades'])])  
  
def test_tasks(task_1, task_2, task_3, task_4, task_5):  
    # Пример тестов для task_1  
    result = task_1('students.csv')  
    assert isinstance(result, list), "❌ task1: Результат должен быть списком."  
    assert len(result) > 0, "❌ task1: Список не должен быть пустым."  
    assert all(isinstance(item, dict) for item in result), "❌ task1: Все элементы должны быть словарями."  
    print("task_1_read_csv ✅")  
  
    # Пример тестов для task_2  
    task_2([{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}], 'students.json')  
    if not os.path.exists('students.json'):  
        open('students.json', 'w').close()  # Создаем файл если он не существует  
    try:
        with open('students.json', 'r') as f:  
            data = json.load(f)  
    except json.decoder.JSONDecodeError: 
        data = dict()
    assert isinstance(data, list), "❌ task 2: Данные в JSON должны были быть записаны списком."  
    assert len(data) > 0, "❌ task 2: Список в JSON не должен быть пустым."  
    assert data[0]["name"].lower() == "Alice".lower(), "❌ task 2: Что-то не так с именем" 
    assert data[0]["age"] == 20, "❌ task 2: Что-то не так с возрастом" 
    assert data[0]["grades"] == [90, 85, 88], "❌ task 2: Что-то не так с оценками"  
    print("task_2_write_json ✅")  
  
    # Пример тестов для task_3  
    open("students.pickle", "wb").close()
    task_3([Student("Alice", 20, [90, 85, 88]), Student("Bob", 22, [2, 2, 8])], "students.pickle")  
    if not os.path.exists('students.pickle'):  
        open('students.pickle', 'wb').close()  # Создаем файл если он не существует  
    with open('students.pickle', 'rb') as f:  
        try:
            data = pickle.load(f)  
        except EOFError:
            data = None
    assert isinstance(data, list), "❌ task 3: Данные в pickle должны быть списком."  
    assert len(data) > 0, "❌ task 3: Список в pickle не должен быть пустым."  
    assert data[0].name.lower() == "Alice".lower(), "❌ task 3: Что-то не то с именем у Alice"  
    assert data[1].age == 22, "❌ task 3: Что-то не то с возрастом у Bob"  
    assert set(data[1].grades) == set([2, 2, 8]), "❌ task 3: Что-то не то с оценками у Bob"  
    print("task_3_pickle_data ✅")  
  
    # Пример тестов для task_4  
    
    try:
        result = task_4('students.pickle')
    except EOFError:
            data = None  
    assert isinstance(result, list), "❌ task 4: Результат должен быть списком."  
    assert len(result) > 0, "❌ task 4: Список не должен быть пустым."  
    assert result[0].name.lower() == "Alice".lower(), "❌ task 4: Что-то не то с именем у Alice"  
    assert result[1].age == 22, "❌ task 4: Что-то не то с возрастом у Bob"  
    assert set(result[1].grades) == set([2, 2, 8]), "❌ task 4: Что-то не то с оценками у Bob"  
    print("task_4_load_pickle ✅")  
  
    # Пример тестов для task_5  
    task_5([{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]}], 'students.txt')  
    if not os.path.exists('students.txt'):  
        open('students.txt', 'w').close()  # Создаем файл если он не существует  
    with open('students.txt', 'r') as f:  
        data = f.readlines()  
        # print(data)
    assert len(data) > 0, "❌ task 5: Файл students.txt не должен быть пустым."  
    assert "Alice".lower() in data[0].lower(), "❌ task 5: Имя 'Alice' должно быть в первой строке."  
    assert "Age: 20".lower() in data[0].lower(), "❌ task 5: Возраст '20' должен быть в первой строке."  
    assert "Grades: [90, 85, 88]".lower() in data[0].lower(), "❌ task 5: Оценки должны быть в первой строке."  
    open('students.txt', 'w').close()

    hard_test_data = [{'name': 'Alice', 'age': 20, 'grades': [90, 85, 88]},
        {'dog': 'da.', 'cat': 'net.', 'bim': 'BAM'}]
    task_5(hard_test_data, 'students.txt') 
    with open('students.txt', 'r') as f:  
        data = f.readlines()  
    assert len(data) > 0, "❌ task 5: Файл students.txt не должен быть пустым."  
    assert "Alice".lower() in data[0].lower(), "❌ task 5: Имя 'Alice' должно быть в первой строке."  
    assert "Age: 20".lower() in data[0].lower(), "❌ task 5: Возраст '20' должен быть в первой строке."  
    assert "Grades: [90, 85, 88]".lower() in data[0].lower(), "❌ task 5: Оценки должны быть в первой строке."  
    
    assert "dog".lower() in data[1].lower(), f"❌ task 5: дог не да, поправь: {hard_test_data}"  
    assert "cat: net.".lower() in data[1].lower(), f"❌ task 5: кот не нет, поправь: {hard_test_data}"  
    assert "bim: BAM".lower() in data[1].lower(), f"❌ task 5: бим не БАМ, поправь: {hard_test_data}"  
    print("task_5_write_txt ✅")  