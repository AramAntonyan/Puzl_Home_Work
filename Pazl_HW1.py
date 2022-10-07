#Вам дали два подсолнуха
#нужно 'good seeds' положить в мешок, а 'rotten and empty seeds' в ведро использовать цикл for and while.
#и подсчитайте сколько у вас семян в ведре и в мешке использовать метод


flower1 = ['g','r','r','g','g','g','g','g','r','r','g','g','g','g','r','g','g','e','r','r','e','g','g','g','g','r','r','r','g','e']
flower2 = ['g','g','g','r','g','g','e','r','r','e','g','g','g','g','r','r','r','g','e']

a = flower1 + flower2
a_good = []
a_bad = []
for i in a:
    if i == 'g':
        a_good.append(i)
    else:
        a_bad.append(i)
print((a_good), len(a_good))
print((a_bad), len(a_bad))

             








# Задача 1.1

# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка

# friends =["Tom", "Mike", "Kevin", "Karen", "Karen","Karen", "Jane"]  #1
# print(type(friends))
# print(type(friends[0]))
# print(friends[0])
# friends.append("Donald")                             #2
# print(friends)

# friends.insert(3, 3)
# print(friends)

# friends.append([0])                                #4
# print(friends)

# friends.insert(2, ("Sara", "Rich"))                  #5
# print(friends)
# print(type(friends[2]))

# print(friends[2])                                    #6

# friends.pop(3)                                         #7
# print(friends)

# friends =["Tom", "Mike", "Kevin", "Karen", "Karen","Karen", "Jane"]
# for i in friends:

# 8. Найти число повторений элемента списка

# Create a GITHUB.com account.


# Задача 1.2
monthConversions = {"Jan": "January", "Feb": "February", "Mar": "March", 
"Apr": "April",
"May": "May",
"Jun": "June",
"Jul": "July",
"Aug": "August",
"Sep": "September",
"Oct": "October",
"Nov": "November",
"Dec": "December"}

# monthConversions['Year'] = 2022        #2
# print(monthConversions)
# print(monthConversions)
# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением типа int 
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

monthConversions[tuple('Moon')] = list('Earth')     #3
print(monthConversions)

# print(monthConversions.get('Dec'))      #4

# del monthConversions["Apr"]                #5
# print(monthConversions)

# print(monthConversions.keys())         #66