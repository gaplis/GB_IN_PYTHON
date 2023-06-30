import sys

data = [10, 15.57, 'Hi', '45', True, '45', 1.0 + 0j, b'\x00\x00\x00']
for i, item in enumerate(data, start=1):
    print(f'№ = {i}; Value = {item}; ID = {id(item)}; Size = {sys.getsizeof(item)}; Hash = {hash(item)}')
    if isinstance(item, int):
        print('True')
    if isinstance(item, str):
        print('True')