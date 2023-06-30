def transl(d: int, b: int) -> str:
    l = []
    while d > 0:
        d, f = divmod(d, b)
        l.append(str(f))
    return ''.join(l[::-1])

print(f'0b{transl(123, 2)}')
print(bin(123))
print(f'0o{transl(123, 8)}')
print(oct(123))