# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# Для простоты будем использовать только положительную индексацию

def range_sum(nums, start_ind, end_ind):
    if start_ind > end_ind:
        start_ind, end_ind = end_ind, start_ind
    if end_ind + 1 >= len(nums):
        end_ind = len(nums)
    return sum(nums[i] for i in range(start_ind, end_ind))


numbers = [1, 6, 3, 8, 0, 24, 6, 5, 1, 8]
start = 7
end = 10
print(range_sum(numbers, start, end))