# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def change_var(var_dict: dict):
    vars_to_change = [k for k in var_dict if len(k) > 1 and k[-1] == 's']
    for k in vars_to_change:
        var_dict[k[:-1]] = var_dict[k]
        var_dict[k] = None


aaa = 123
bbs = 'Test'
some = 'teeeest'
s = 567
var_s = 1

all_var = globals()
print(f"{aaa = }\n{bbs = }\n{some = }\n{s = }\n{var_s = }\n{all_var = }\n")

change_var(all_var)
print(f"{aaa = }\n{bbs = }\n{some = }\n{s = }\n{var_s = }\n{all_var = }\n")
print(f"{bb = }\n{var_ = }\n")
