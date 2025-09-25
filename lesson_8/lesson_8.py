import time
"""
Итератор нужен - чтобы последоватьельно извлекать значения, не прибегая к использоавнию интексов
    Итерируемые объекты
    строкки (str)
    списки(list)
    кортежи (tuple)
    диапозоны чисел (range)
    словари (dict)
    множества (set)

"""

number = [34, 63, 53, 93, 1, 0 ,31]
it_numbers = iter(number)
# print(it_numbers, type(it_numbers))

# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(number))

str_1 = 'Vladimir'
it_str_1 = iter(str_1)
# print(next(it_str_1))
# print(next(it_str_1))
# print(next(it_str_1))
# print(next(it_str_1))
# time.sleep(4)
# print(next(it_str_1))

for i in it_str_1:

    print(i)