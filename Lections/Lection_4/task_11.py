def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


def standart_arg(arg):
    """Пример обычной функции"""
    print(arg)


standart_arg(42)
standart_arg(arg=42)


def pos_only_arg(arg, /):
    """Пример только позиционной функции"""
    print(arg)


pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

def kwd_only_arg(*, arg):
    """Пример только ключевой функции"""
    print(arg)

# kwd_only_arg(42) # TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
kwd_only_arg(arg=42)