"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(nums):
    result = []
    for num in nums:
        k = 0
        for i in range(2, num + 1):
            if num % i == 0:
                k += 1
        if k == 1:
            result.append(num)        
        else:
            pass
    return result 


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == "odd":
        return [i for i in nums if i % 2 != 0]
    if filter_type == "even": 
        return [i for i in nums if i % 2 == 0]
    if filter_type == "prime":
        return is_prime(nums)