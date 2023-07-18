text = 'gfdgfdgfd gfdgfdgf dgfdgfdgf dgfdgfd, gfdgdfgfdgfdgfdgfd gfdg dfgfd ggfdgfdgdf.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')