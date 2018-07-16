# 4)	Дан массив чисел.
# [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
#
# 4.1) убрать из него повторяющиеся элементы
# 4.2) вывести 3 наибольших числа из исходного массива
# 4.3) вывести индекс минимального элемента массива
# 4.4) вывести исходный массив в обратном порядке
#

def remove_same_elem(random_list):
    removed_elem_list = list(set(random_list))
    print('Список без повторяющихся элементов: ', removed_elem_list)
    return removed_elem_list

def three_biggest_digits(removed_elem_list):
    removed_elem_list.sort(reverse=True)
    three_biggest_digits_list = removed_elem_list[:3]
    print('Список из наибольших 3х чисел: ', three_biggest_digits_list)

def min_index(random_list):
    min = random_list[0]
    min_index = 0
    for i in range(len(random_list)):
        if min > random_list[i]:
            min = random_list[i]
            min_index = i
    print('Индекс минимального числа: ', min_index)

def reversed_list(random_list):
    random_list.reverse()
    print('Список в обратном порядке: ', random_list)

random_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print('Рандомный список: ', random_list)

removed_elem_list = remove_same_elem(random_list)
three_biggest_digits(removed_elem_list)
min_index(random_list)
reversed_list(random_list)