# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = "Просто текст на Русском языке"
dict_iter = iter({c: ord(c) for c in set(text)}.items())
print(*[next(dict_iter) for _ in range(5)], sep="\n")