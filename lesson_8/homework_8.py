from collections.abc import Iterable
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по итераторам"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
names = ['Vladimir', 'Liza', 'Alex', 'Ilya', 'Kirill']
it_names = iter(names)
print(next(it_names))
print(next(it_names))
print(next(it_names))
print(next(it_names))
print(next(it_names))
####################TASK_2##############################
str_line = 'Vladimir'
it_str = iter(str_line)

print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print(next(it_str))
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по теме "Генераторы списков (List Comprehensions)"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
N = int(input())
lst = [ i ** 2 for i in range(1, N + 1)]
print(lst)
####################TASK_2##############################
new_lst = [num for num in range(-10, 11) if num % 2 == 0]
print(new_lst)
####################TASK_3##############################
names = ['Vladimir', 'Liza', 'Alex', 'Ilya', 'Kirill']
new_str_lst = [len(line) for line in names]
print(new_str_lst)
####################TASK_4##############################
lst = ["четное" if i % 2 == 0 else "нечетное" for i in range(1, 21)]
print(lst)
####################TASK_5##############################
test_lst = [12, 'str', [456]]

gen = (isinstance(obj, Iterable) for obj in test_lst)
for result in gen:
    print(result)






















