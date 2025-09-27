print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Функции в Python"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
square = lambda x: x**2
print(square(5))
####################TASK_2##############################
even = lambda x: x % 2 ==0
print(even(7))
####################TASK_3##############################
def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Замыкания"')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
def multiply_by(n):
    def inner(x):
        return x * n
    return inner
times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))
####################TASK_2##############################
def counter(start=0):
    def inner():
        nonlocal start
        start += 1
        return start
    return inner

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2























