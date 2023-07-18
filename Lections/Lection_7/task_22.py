text = ['gfdgfdgfd gfdgfdgf dgfdgfdgf dgfdgfd, gfdgdfgfdgfdgfdgfd gfdg dfgfd ggfdgfdgdf.',
        'fdsfdsf fefwf wfw gfwfffdsf vcdscsdcc cs gdgdgvfdgwfvsdvsvs ?',
        'fdsgdsgfds 3h5herhrebna ggr gr geegaw ger g h hrthhtrhtthrhtth?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.
