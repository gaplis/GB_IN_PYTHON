from random import randint


def check_positions(positions: list):
    for row, col in positions:
        r, c = row, col
        while r < 8 or c < 8:
            if (r + 1, c + 1) in positions:
                return False
            r += 1
            c += 1
        r, c = row, col
        while 0 <= r < 8 or 0 <= c < 8:
            if (r + 1, c - 1) in positions:
                return False
            r += 1
            c -= 1
    return positions


def random_positions():
    positions = []
    for i in range(8):
        while True:
            rand = i, randint(0, 7)
            if len(positions) > 0:
                for item in positions:
                    if rand[1] == item[1]:
                        break
                else:
                    positions.append(rand)
                    break
            else:
                positions.append(rand)
                break
    return positions


def generate_all():
    result = []
    numbers_a = [i for i in range(8)]
    for a in numbers_a:
        numbers_b = numbers_a[:]
        numbers_b.remove(a)
        for b in numbers_b:
            variants = [(0, a), (1, b)]
            if b == a + 1 or b == a - 1:
                continue
            if check_positions(variants):
                numbers_c = numbers_b[:]
                numbers_c.remove(b)
                for c in numbers_c:
                    variants = [(0, a), (1, b), (2, c)]
                    if c == b + 1 or c == b - 1:
                        continue
                    if check_positions(variants):
                        numbers_d = numbers_c[:]
                        numbers_d.remove(c)
                        for d in numbers_d:
                            variants = [(0, a), (1, b), (2, c), (3, d)]
                            if d == c + 1 or d == c - 1:
                                continue
                            if check_positions(variants):
                                numbers_e = numbers_d[:]
                                numbers_e.remove(d)
                                for e in numbers_e:
                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e)]
                                    if e == d + 1 or e == d - 1:
                                        continue
                                    if check_positions(variants):
                                        numbers_f = numbers_e[:]
                                        numbers_f.remove(e)
                                        for f in numbers_f:
                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f)]
                                            if f == e + 1 or f == e - 1:
                                                continue
                                            if check_positions(variants):
                                                numbers_g = numbers_f[:]
                                                numbers_g.remove(f)
                                                for g in numbers_g:
                                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f), (6, g)]
                                                    if g == f + 1 or g == f - 1:
                                                        continue
                                                    if check_positions(variants):
                                                        numbers_h = numbers_g[:]
                                                        numbers_h.remove(g)
                                                        for h in numbers_h:
                                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f),
                                                                        (6, g), (7, h)]
                                                            if h == g + 1 or h == g - 1:
                                                                continue
                                                            if check_positions(variants):
                                                                result.append(variants)
    return result
