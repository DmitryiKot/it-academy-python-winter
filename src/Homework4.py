import random

"""
Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами
были числа от 1 до 20, а значениями кубы этих чисел.
"""
print({abc: abc ** 3 for abc in range(1, 21)})

# -----------------------------------------------------------------------------

"""
Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""
lst = [el for el in range(1, 11)]
random_lst = [random.choice(lst) for el in range(10)]
print(lst, random_lst)
print(len(set(lst).intersection(set(random_lst))))

"""
Даны два списка чисел. Посчитайте, сколько различных чисел входит только
в один из этих списков
"""
print(len(set(lst).symmetric_difference(set(random_lst))))

# -----------------------------------------------------------------------------
"""
Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько различных
слов содержится в этом тексте.
"""
inp_str = input().split()
print(len(inp_str), inp_str)

# -----------------------------------------------------------------------------
"""
Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa    
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""
countries = {}
lst_of_cities = []
for name in range(int(input('Countries: '))):
    country, *cities = input('country and cities: ').split()
    countries[country] = cities
for count_cities in range(int(input('count cities: '))):
    lst_of_cities.append(input('city: '))
    for key, value in countries.items():
        if lst_of_cities[count_cities] in value:
            print(key)

# -----------------------------------------------------------------------------
"""
Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N
чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник. Пример:
    3          - N количество школьников
2          - M1 количество языков первого школьника
Russian    - языки первого школьника
English
3          - M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
"""
students = [{input('lang: ') for j in range(int(input('count lang: ')))}
            for i in range(int(input('students: ')))]
known_everyone, known_someone = set.intersection(*students), \
                                set.union(*students)
print(len(known_everyone), *sorted(known_everyone), sep='\n')
print(len(known_someone), *sorted(known_someone), sep='\n')

# -----------------------------------------------------------------------------

"""
Оглянемся назад
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

a = 64
b = 48
while b != 0:
    a, b = b, a % b
print(a)
