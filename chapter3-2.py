# 클래스 예제2
# 벡터 (x, y)


class Vector:
    def __init__(self, *args):
        """
        Create a vector, example: v = Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        Return the vector informations
        """
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """
        Return the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector instance 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))

if v3:
    print(True)
else:
    print(False)
