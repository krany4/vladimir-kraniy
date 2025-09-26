print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по итераторам"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
fruits = {"apple": 14, "banana": 13, "cherry": 12, "orange": 11}
print(fruits)
fruits.setdefault("kiwi", 10)
print(fruits)
####################TASK_2##############################
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
for key, value in grades.items():
    if value >= 4:
        print(key)
####################TASK_3##############################
country = {"Russia": "Moscow", "France": "Paris", "Germany": "Berlin"}
user_write = input()
if user_write in country.keys():
    print(country[user_write])
else:
    print('Страна не найдена')
####################TASK_4##############################
students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
inverted_dict = {}
for key, value in students:
    inverted_dict[value] = key
print(inverted_dict)
####################TASK_5##############################
print("Пятая задача")
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
min_marks = int(input())
name_student = ''
for key, value in grades.items():
    if value >= min_marks:
        name_student = key
grades.pop(name_student)
print(grades)
####################TASK_6##############################
students = ["Анна", "Борис", "Виктор", "Галина"]
students_dict = dict.fromkeys(students, None)
for key in students_dict:
    age = int(input())
    students_dict[key] = age

print(students_dict)
####################TASK_7##############################
exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
user_write = input()
if user_write in exchange_rates:
    print(exchange_rates[user_write])
else:
    print("Неизвестная валюта")
    exchange_rates.setdefault(user_write, None)
print(exchange_rates)
####################TASK_8##############################
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Кортежи в Python"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
my_tuple = ("Test", 12, False, [1, 2, 3], {"a": 1, "b": 2})
print(my_tuple[1])
print(my_tuple[len(my_tuple) - 1])
####################TASK_2##############################
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
test_sum = 0
for num in nums:
    if num == 4:
        test_sum += 1
print(nums.index(7))
####################TASK_3##############################
lst = ["Python", "Java", "C++", "JavaScript"]
new_tuple = tuple(lst)
print("C++" in new_tuple)
####################TASK_4##############################
new_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(new_numbers[:3])
print(new_numbers[-3:])
print(new_numbers[::2])
####################TASK_5##############################
my_tuple = ([1, 2, 3], {"a": 10, "b": 20})
my_tuple[0].append(34)
print(my_tuple)
my_tuple[1].setdefault(2, 'test')
print(my_tuple)




