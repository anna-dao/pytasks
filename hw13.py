# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
#
# def my_func(a):
#         return a * 7

def is_remainder_decorator(my_func):
    def wrapper(a):
        my_func(a)
        result = 100 % a
        if result == 0:
            print("We are OK!")
        else:
            print("Bad news guys, we got {%.2f}" %(result))
    return wrapper

@is_remainder_decorator
def my_func(a):
    return a * 7

my_func(7)
my_func(100)