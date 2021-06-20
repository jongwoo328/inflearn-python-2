# Special Method (Magic Method)
# 클래스안에 정의 가능한 Built-in method

# print(dir(int))

n = 10

# print(n + 100)
# print(n.__add__(100))
# print(n.__bool__(), bool(n))
# print(n * 100, n.__mul__(100))

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit : {self._name} {self._price}"

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, x):
        if self._price <= x._price:
            return True
        return False

    def __ge__(self, x):
        if self._price >= x._price:
            return True
        return False


# 인스턴스 생성
f1 = Fruit("orange", 7500)
f2 = Fruit("banana", 3000)

print(f1 + f2)
print(f1 >= f2)
print(f1 <= f2)
print(f1 - f2)
print(f1, f2)
