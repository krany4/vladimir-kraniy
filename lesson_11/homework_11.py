print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Функции в Python"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
def greet(name: str) :
    print(f'Привет, {name}! Добро пожаловать!')
greet('Анна')
####################TASK_2##############################
def square(num: int) -> int:
    return num ** 2
print(square(5))
####################TASK_3##############################
def is_even(num: int) -> bool:
    if  num % 2 == 0:
        return True
    return False
print(is_even(4))
print(is_even(7))
####################TASK_4##############################
def repeat_string(text: str, times: int) -> str:
    return text * times
print(repeat_string("Python", 3))
####################TASK_5##############################
def add(a: int, b: int) -> int:
    return a + b
print(add(3, 7))
####################TASK_6##############################
def get_max(a: int, b: int, c: int) -> int:
    return max(a, b, c)
print(get_max(10, 25, 7))
####################TASK_7##############################
def calculate(a: int, b: int, operation: str):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))
####################TASK_8##############################
def reverse_string(text: str) -> str:
    return text[::-1]
print(reverse_string("Python"))
####################TASK_9##############################
def compare_strings(s1: str, s2: str, ignore_case=True, ignore_spaces=True):
    if  ignore_case :
        s1 = s1.lower()
        s2 = s2.lower()
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    return s1 == s2
####################TASK_10##############################






















