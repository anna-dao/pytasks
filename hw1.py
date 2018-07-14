# 1)	Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}


def generate_dict(keys):
    square_key_dict = {}
    keys_length = (len(keys)) + 1
    for key in range(keys[0], keys_length):
        square_key_dict[key] = key * key
    print('Словарь из ключей в квадрате: ', square_key_dict)

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generate_dict(keys)