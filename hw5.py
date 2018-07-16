# 5)	Найти общие ключи в двух словарях:
# dict_one = { ‘a’: 1,
#                     ‘b’: 2,
#                     ‘c’: 3,
#                     ‘d’: 4 }
#
# dict_two = { ‘a’: 6,
#                     ‘b’: 7,
#                     ‘z’: 20,
#                     ‘x’: 40 }

def common_dict(dict_one, dict_two):
    set_one = set()
    set_two = set()
    for key in dict_one:
        set_one.add(key)
    for key in dict_two:
        set_two.add(key)
    common_set = set_one & set_two
    print('Общие ключи в двух словарях: ', common_set)

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'x': 20, 'z': 40}

common_dict(dict_one, dict_two)