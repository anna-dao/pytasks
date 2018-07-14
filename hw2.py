# 2)	Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
import random

def generate_random_even(length):
    random_list = []
    even_list = []
    for i in range(length):
        random_list.insert(i, random.randint(1, 100))
        if random_list[i] % 2 == 0:
            even_list.append(random_list[i])
    print(even_list)

generate_random_even(50)