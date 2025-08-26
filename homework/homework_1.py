import keyword
print('=============TASK1===============')
name = 'Vladimir'
age = 23
height = 1.88
print(f'Мое имя - {name}, мой возраст - {age}, мой рост - {height}')
print('=============TASK2===============')
x = 10
print(type(x))
x = 25.5
print(type(x))
x = 'Python'
print(type(x))
print(x)
print('=============TASK3===============')
a = 7
b = a
print(a)
print(b)
a = 10
print(b)
# Переменная a начала ссылаться на другой объект(10), но переменная b все еще ссылается на старый объект(7)
print('=============TASK4==============')
x = y = z = 100
print(x, y, z)
print(id(x))
print(id(y))
print(id(z))
#Пока что id одинаковые
x, y, z = 10, 11, 13
print(x, y, z)
print(id(x))
print(id(y))
print(id(z))
#теперь id разные
print('=============TASK5==============')
a_1 = 5
b_1 = 10
a_1, b_1 = b_1, a_1
print(a_1, b_1)
print('=============TASK6==============')

# True = 12
# print = 12
# if = 56
# Нельзя называть так переменны, потому что это зарезервированные слова ЯП, которые используются для других конструкций в языке

print(keyword.kwlist)
print('=============TASK7==============')
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "test"
print(type(var1))
print('=============TASK8==============')
first_name = "Ivan"
second_name = "Ivanov"
is_married = True
is_student = True
age = 56
print(type(first_name), type(second_name), type(is_married), type(is_student), type(age))
переменная = 10
print(переменная)
#у меня почему-то работает, но по идее не должно, нельзя называть так переменные