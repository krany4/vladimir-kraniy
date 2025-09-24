print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи на input() и print()')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
print('Привет, мир!')
print(5, 10, 15)
print(10 + 25)
####################TASK_2##############################
print(1, 2, 3, sep='&')
print('Python', end=' ')
print('лучший язык')
####################TASK_3##############################
x = 3.14
y = -8
print(f'Координаты точки: x = {x}; y = {y}')
name = input('Write your name: ')
age = int(input('Write your age: '))
print(f'Имя: {name}, Возраст: {age}')
####################TASK_4##############################
name = input('Write your name: ')
print(f'Привет, {name}!')
####################TASK_5##############################
number_one = input()
number_two = input()
print(int(number_one) + int(number_two))

number = int(input())
print(number * number)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Булевые значения')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = 8 > 12
print(res ,type(res))
####################TASK_2##############################
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print(x % 3 == 0 and x % 5 == 0)
####################TASK_3##############################
y = 4.5
print(1 <= y <= 10)
print((0 <= y <= 5) or (10 <= y <= 15))
print(not (y < 5))
####################TASK_4##############################
print(True or False and False)
print(not False and True)
print(False or not True and True)
print(not (10 > 5 or 3 < 1))
####################TASK_5##############################
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))
####################TASK_6##############################
n = 15
print(n > 0)
print(n % 2 == 0)
print(n % 3 == 0)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Срезы строк')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
s = "Программирование"
print(s[0])
print(s[:-1])
print(s[2], s[-2])
####################TASK_2##############################
print(s[100]) #IndexError: string index out of range - выход за пределы длины строки
print(s[len(s) - 1])
####################TASK_3##############################
first_six_symbol = s[0:6]
print(first_six_symbol)
las_five_symbols = s[-5:]
print(las_five_symbols)
three_and_seven_symbols = s[2:7]
print(three_and_seven_symbols)
print(s[::2])
print(s[::-1])
####################TASK_4##############################
print(s[0::3])
print(s[::-2])
####################TASK_5##############################
s[0] = "п" # Строки неизменяемы
s2 = "П" + s[1:]





















