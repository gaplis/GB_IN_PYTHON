name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)

text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)

text = f'Меня зовут {name} и мне {age} лет'
print(text)