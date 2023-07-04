# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

from functools import reduce

nums = [11, 12, 11, 13, 14, 12]
unique_numbers = []
for i in nums:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(f'{unique_numbers = }')

unique_numbers_1 = list(dict.fromkeys(nums))
print(f'{unique_numbers_1 = }')

unique_numbers_2 = list(set(nums))
print(f'{unique_numbers_2 = }')

unique_numbers_3 = [x for i, x in enumerate(nums) if i == nums.index(x)]
print(f'{unique_numbers_3 = }')

unique_numbers_4 = reduce(lambda l, x: l if x in l else l + [x], nums, [])
print(f'{unique_numbers_4 = }')