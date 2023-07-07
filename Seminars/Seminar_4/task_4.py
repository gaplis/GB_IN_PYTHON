# def bubble_sort(num_list):
#     for i in range(len(num_list)):
#         for j in range(i, len(num_list)):
#             if num_list[i] > num_list[j]:
#                 num_list[i], num_list[j] = num_list[j], num_list[i]
#
# numbers = [1, 6, 3, 8, 0, 24, 6, 5, 1, 8]
# bubble_sort(numbers)
# print(numbers)

# Функция получает на вход список чисел.
# Отсортируйте список по убыванию суммы цифр
def sum_sort(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    return summ


numbers = [12, 67, 34, 8, 128, 24, 62, 555, 12, 83]
print(sorted(numbers, key=lambda x: sum(map(int, str(x))), reverse=True))
print(sorted(numbers, key=sum_sort, reverse=True))