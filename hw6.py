# 6)	Дан массив из словарей
# data = [ {‘name’: ‘Viktor’, ‘city’: ‘Kiev’, ‘age’: 30 },
#              {‘name’: ‘Maksim’, ‘city’: ‘Dnepr’, ‘age’: 20},
#              {‘name’: ‘Vladimir’, ‘city’: ‘Lviv’, ‘age’: 32},
#              {‘name’: ‘Andrey’, ‘city’: ‘Kiev’, ‘age’: 34},
#              {‘name’: ‘Artem’, ‘city’: ‘Dnepr’, ‘age’: 50},
#              {‘name’: ‘Dmitriy’, ‘city’: ‘Lviv’, ‘age’: 21}]
#
# 6.1) отсортировать массив из словарей по значению ключа ‘age'
# 6.2) сгруппировать данные по значению ключа 'city'
#        вывод должен быть такого вида :
#        {
#           ‘Kiev’: [ {‘name’: ‘Viktor’, ‘age’: 30 },
#                        {‘name’: ‘Andrey’, ‘age’: 34}],
#           ‘Dnepr’: [ {‘name’: ‘Maksim’, ‘age’: 20 },
#                           {‘name’: ‘Artem’, ‘age’: 50}],
#           ‘Lviv’: [ {‘name’: ‘Vladimir’, ‘age’: 32 },
#                        {‘name’: ‘Dmitriy’, ‘age’: 21}]

def sort_by_age(data):
    def sorting_by_age(elem):
        return elem['age']

    data.sort(key=sorting_by_age)
    return data

def group_by_city(data):
    groupped_data = {}
    for person in data:
        info_list = [{'name': person['name'], 'age':person['age']}]
        groupped_data[person['city']] = info_list
    return groupped_data

data = [ {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
             {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
             {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
             {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
             {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
             {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

print(sort_by_age(data))
print(group_by_city(data))

