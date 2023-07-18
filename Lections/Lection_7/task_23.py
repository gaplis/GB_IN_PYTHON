last = before = 0
text = ['gfdgfdgfd gfdgfdgf dgfdgfdgf dgfdgfd, gfdgdfgfdgfdgfdgfd gfdg dfgfd ggfdgfdgdf.',
        'fdsfdsf fefwf wfw gfwfffdsf vcdscsdcc cs gdgdgvfdgwfvsdvsvs ?',
        'fdsgdsgfds 3h5herhrebna ggr gr geegaw ger g h hrthhtrhtthrhtth?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))