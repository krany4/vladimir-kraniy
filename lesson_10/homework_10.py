from traceback import print_tb

print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Множества в Python"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
set_1 = {1, 2, 3, 4, 5, 6}
set_1.add(1)
print(set_1)
####################TASK_2##############################
cities = ["Москва", "Питер", "Казань", "Москва", "Новосибирск", "Питер"]
unique_cities = set(cities)
print(unique_cities)
print(len(unique_cities))
####################TASK_3##############################
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers.remove(5)
numbers.discard(15)
print(numbers)
####################TASK_4##############################
line = "abrakadabra"
new_set = set(line)
print(new_set)
print(len(new_set))
####################TASK_5##############################
new_set = {}
print(new_set)
new_set.add(10)
new_set.add("hello")
new_set.add((1, 2, 3))
new_set.add([4, 5, 6])  # Нельзя добавлять список, так как он является изменяемым объектом в питоне
print(new_set)
####################TASK_6##############################
first_set = {2, 5, 6, 65, 74, 43}
second_set = {32, 4324, 74, 34, 65, 23}
print(first_set.intersection(second_set))
print(first_set.union(second_set))
print(first_set.difference(second_set))
print(second_set.difference(first_set))
print(first_set.symmetric_difference(second_set))
####################TASK_7##############################
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers & odd_numbers)
print(even_numbers | odd_numbers)
####################TASK_8##############################
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print(python_students.intersection(java_students))
print(python_students ^ java_students)
print(python_students | java_students)
####################TASK_9##############################
text1 = set("программирование")
text2 = set("автоматизация")
print(text1 & text2)
print(text1 - text2)
print(text1 ^ text2)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Множества в Python"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
first_task_set = {num ** 2 for num in range(1, 11) if num % 2 == 0}
####################TASK_2##############################
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
res_set = set()
for i in len(words):
    print(i)
####################TASK_3##############################
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
result_dict = {name: ("отлично" if grade >= 80 else "удовлетворительно")
               for name, grade in grades.items()}
print(result_dict)
####################TASK_4##############################
text = {"Python", "automation", "programming", "testing"}
result = {word: len(word) for word in text}
print(result)
####################TASK_5##############################
n = 10
nested_dict = {i: {j**2 for j in range(1, i+1)} for i in range(1, n+1)}
print(nested_dict)