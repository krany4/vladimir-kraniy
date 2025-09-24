print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Списки')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Cat", False, [1,2,3]]
####################TASK_2##############################
print(cities[0])
print(numbers[-1])
# print(cities[10]) # ошибка - IndexError: list index out of range
####################TASK_3##############################
numbers[1] = 10
print(numbers)
mixed[-1] = "Python"
print(mixed)
####################TASK_4##############################
print(len(numbers))
print(max(numbers), min(numbers))
print(sum(numbers))
print(numbers.sort())
print(numbers.sort(reverse=True))
####################TASK_5##############################
print([1, 2, 3] + [4, 5])
lst = ["Python", "is", "awesome"]
print(lst * 3)
####################TASK_6##############################
print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)
####################TASK_7##############################
print(numbers)
numbers.pop(2)
print(numbers)
del cities[len(cities) - 1]
print(cities)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Срезы списков')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
new_cities = ["London", "Paris", "New York", "Moscow", "Berlin", "Vena"]
print(new_cities)
new_slice_cities = new_cities[:]
print(new_slice_cities)
print(new_cities is new_slice_cities)
####################TASK_2##############################
print(new_cities[1:3])
print(new_cities[2:])
print(new_cities[:3])
print(new_cities[:])
print(new_cities[-2:])
####################TASK_3##############################
print(new_cities[::2])
print(new_cities[::-1])
print(new_cities[::-2])
####################TASK_4##############################
new_cities[1:3] = ["Сочи", "Нижний Новгород"]
print(new_cities)
new_cities[::2] = ["Город", "Город", "Город"]
print(new_cities)
cities[1:3] = "Волгоград", "Омск"
print(new_cities)
####################TASK_5##############################
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)
test = ["Python", "rocks"]
print(test * 2)
####################TASK_6##############################
print([1, 2, 3] == [1, 2, 3]) # да равны
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] == [1, 2, "abc"]) # будет false
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Методы списков')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
numbers = [5, 10, 15]
numbers.append(20)
numbers.insert(1, 7)
numbers.append("Python")
print(numbers)
####################TASK_2##############################
numbers.remove(10)
print(numbers.pop())
numbers.pop(1)
numbers.clear()
print(numbers)
####################TASK_3##############################
letters = ["a", "b", "c"]
new_letters = letters.copy()
print(letters)
print(new_letters)
new_new_letters = list(letters)
print(new_new_letters)
print(letters is new_letters)
print(letters is new_new_letters)
####################TASK_4##############################
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
marks.index(5)
print(marks.index(5))
#print(marks.index(6)) - будет всегда выбрасывать ошибку
####################TASK_5##############################
nums = [8, 2, 5, 1, 7]
nums.sort()
nums.sort(reverse=True)
nums.reverse()
print(nums)
####################TASK_6##############################
cities = ["London", "Paris", "New York", "Moscow", "Berlin", "Vena"]
new_list = sorted(cities)
print(new_list)
print(cities)
cities.sort()
print(cities)
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Вложенные списки (массивы)')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
print(matrix[1])
print(matrix[2][0])
####################TASK_2##############################
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix[0] = [0, 0, 0, 0]
matrix[1][-1] = "Python"
print(matrix)








