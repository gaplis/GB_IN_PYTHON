# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = "Python (в русском языке встречаются названия пито́н или па́йтон) — высокоуровневый " \
       "язык программирования общего назначения с динамической строгой типизацией и автоматическим " \
       "управлением памятью, ориентированный на повышение производительности разработчика, " \
       "итаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. " \
       "Язык является полностью объектно-ориентированным в том плане, что всё является объектами. " \
       "Необычной особенностью языка является выделение блоков кода пробельными отступами. " \
       "Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться " \
       "к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания " \
       "скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление " \
       "памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, " \
       "таких как C или C++.".replace('—', '').replace(',', '').replace('(', '').replace(')', '').replace('.', '') \
            .lower().split()


print(f'Текст: {text}')

my_dict = {}

for i in set(text):
    my_dict.setdefault(i, text.count(i))

print(f'Словарь: {my_dict}')

res = {}

for i in range(10):
       for key in my_dict:
              if int(my_dict[key]) == max(my_dict.values()):
                     res.setdefault(key, my_dict[key])
                     my_dict.pop(key)
                     break

print(f'10 самых повторяющихся слов: {res}')