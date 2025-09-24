print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Методы строк')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
s = "Python для автоматизации"
print(s.upper())
print(s.lower())
####################TASK_2##############################
msg = "абракадабра"
count = msg.count('ра')
print(count)
count2 = msg.count("а", 3)
####################TASK_3##############################
print(msg.find("ка"))
print(msg.rfind("а"))
print(msg.find("xyz"))
####################TASK_4##############################
text = "Я изучаю Java"
text = text.replace('Java', 'Python')
text = text.replace(" ", '')
print(text)
####################TASK_5##############################
line = "Python"
print(line.isalpha())
line2 = "12345"
print(line2.isdigit())
line3 = "123abc"
print(not line3.isdigit())
####################TASK_6##############################
code = "42"
print(code.rjust(5, "0"))
text_line = 'text'
print(text_line.ljust(10, '*'))
####################TASK_7##############################
fruits = "яблоко, груша, банан"
fruit_some_res = fruits.replace(',', '')
print(fruit_some_res.split())
languages = "Python;Java;C++"
print(languages.split(';'))
####################TASK_8##############################
lst1 = ["Привет", "мир", "!"]
new_line = ' '.join(lst1)
print(new_line)
fruit_lst = ["apple", "banana", "cherry"]
new_fruit_str = ', '.join(fruit_lst)
print(new_fruit_str)
####################TASK_9##############################
delet_str_1 = " Python"
print(delet_str_1.lstrip())
delet_str_2 = "Python "
print(delet_str_2.rstrip())
delet_str_3 = " Python "
print(delet_str_3.strip())
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Спецсимволы')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
text = "Hello\nPython"
print(text) #Потому что у нас есть спецсимвол \n, которые переводит все что после него на новую строчку
####################TASK_2##############################
t = "Python\tAutomation"
print(t) # \t - добавляет табуляцию
####################TASK_3##############################
path = "C:\new\test.txt" # \n - переход на новую строку \t - табуляция]
print(path)
path_new = "C:\\new\\test.txt"
print(path_new)
wine = "Марка вина \"Ягодка\""
print(wine)
####################TASK_4##############################
path = r"C:\new\test.txt"
print(path) # из-за того что у нас есть r в строке, то у нас не учитываются спецсимвлы
####################TASK_5##############################
s = "Hello\b World"
print(s) # \b - удалет символ перед собой
s = "Hello\fPython"
print(s) # \f - перевод страницы
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('Форматирование строк')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
####################TASK_1##############################
name = "Vova"
age = 23
print("Меня зовут " + str(name) + ", мне " + str(age) + " лет.") # если добавить в число без str() то будет ошибка
####################TASK_2##############################
greeting = "Привет, меня зовут {}, мне {} лет.".format(name, age)
print(greeting)
greeting_named = "Привет, меня зовут {name}, мне {age} лет.".format(name=name, age=age)
print(greeting_named)
greeting_reordered = "Привет, меня зовут {name}, мне {age} лет.".format(age=age, name=name)
print(greeting_reordered)
####################TASK_3##############################
year = 2025
city = "Penza"
print(f"Сегодня {year} год, и я живу в {city}.")
print(f"Через 5 лет будет {year + 5} год.")
####################TASK_4##############################
print(f"Дважды мой возраст: {age * 2}")
print(f"My name is : {name.upper()}")






























