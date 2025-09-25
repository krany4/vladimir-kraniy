print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по уроку "Цикл while"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
N = int(input())
i = 1
while i < N + 1:
    print(i)
    i+=1
####################TASK_2##############################
N = int(input())
sum_N_number = 0
i = 1
while i < N + 1:
    if  i % 2 == 0:
        sum_N_number += i
    i += 1

print(sum_N_number)
####################TASK_3##############################
N = int(input())
count = 0
while N > 0:
    N //= 10
    count += 1
print(count)
####################TASK_4##############################
N = int(input())
big_number = 0
while N > 0:
    res = N % 10
    if  big_number < res:
        big_number = res
    N //= 10
####################TASK_5##############################
while True:
    if input() == "qwerty123":
        print('Доступ разрешен')
        break
    else:
        print('Неверный пароль')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по уроку "Операторы break, continue и else в цикле while""')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
        break
    else:
        i += 1
else:
    print("Четное число не найдено")
####################TASK_2##############################
numbers = int(input())
sum_positive_number = 0
while numbers:
    if  numbers == 0:
        break
    if numbers > 0:
        sum_positive_number += numbers
    else:
        numbers = int(input())
        continue
####################TASK_3##############################
a = int(input())
b = int(input())

current = a
while current <= b:
    if current % 2 == 0:
        current += 1
        continue
    print(current)
    current += 1
####################TASK_4##############################
N = int(input("Введите число: "))

if N < 2:
    print("Число не является простым")
else:
    i = 2
    while i < N:
        if N % i == 0:
            print("Число не простое")
            break
        i += 1
    else:
        print("Число простое")
####################TASK_5##############################
bit_n = None
while True:
    s = input()

    if s == "":
        break

    n = int(s)

    if n == 0:
        break

    if bit_n is None or n > bit_n:
        bit_n = n

if bit_n is not None:
    print(bit_n)
else:
    print("Числа не вводились")
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Задачи по уроку "Цикл for в Python – основы и применение')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
test_line = input()
for line in reversed(test_line):
    print(line)
####################TASK_2##############################
list_number = [1, 2, 3, 4, 5]
for i in range(len(list_number)):
    if list_number[i] % 2 == 0:
        list_number[i] = 0

print(list_number)
####################TASK_3##############################
powers = []
N = int(input())
for i in range(0, N + 1):
    print(f'Двойка в степени {i} = {2 ** i}')
    powers.append(2 ** i)
print(powers)
####################TASK_4##############################
A = int(input())
B = int(input())
K = int(input())
for i in range(A, B + 1, K):
    print(i)






























