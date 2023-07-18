text = ['gfdgfdgfd gfdgfdgf dgfdgfdgf dgfdgfd, gfdgdfgfdgfdgfdgfd gfdg dfgfd ggfdgfdgdf.',
        'fdsfdsf fefwf wfw gfwfffdsf vcdscsdcc cs gdgdgvfdgwfvsdvsvs ?',
        'fdsgdsgfds 3h5herhrebna ggr gr geegaw ger g h hrthhtrhtthrhtth?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')