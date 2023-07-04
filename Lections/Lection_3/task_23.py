pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')

data = [3254, 234235235, 53534552, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')