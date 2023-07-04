# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
import pprint

tup = ((5, 6), 'check', -18.5, True, 11, {1, 2}, [7, 8], 2.0 + 1J, b'\x01\x01\x01', {1: 'one', 2: 'two'}, 0.5, False)

di = {}
my_di= {}

for item in tup:
    if type(item) not in di:
        di[type(item)] = []
    di[type(item)].append(item)
    my_di.setdefault(type(item), []).append(item)

pp = pprint.PrettyPrinter(depth=5)
pp.pprint(di)
print(my_di)
