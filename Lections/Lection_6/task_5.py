from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = "qwerty"  # Защищенная переменная _
__top_secret = "1q2w3e4r5t6y"  # Приватная переменная __


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)
