# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

nums = [11, 12, 11, 13, 14, 12, 18, 17, 18]
print(nums)
new_nums = [i for i in nums if nums.count(i) != 2]
count = 2

for num in set(nums):
    if nums.count(num) == count:
        for _ in range(count):
            nums.remove(num)

print(nums)
print(new_nums)