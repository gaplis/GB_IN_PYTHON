from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 202, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last'}
print(d)

mul_point = Point(2, [3, 4, 5], 6)
print(mul_point)
# d.update({mul_point: 'bad_point'}) # TypeError: unhashable type: 'list'
