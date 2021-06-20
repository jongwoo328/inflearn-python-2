# 시퀀스형
# 컨테이너 (Container : 서로다른 자료형[list, tuple, collections.deque, ])
# 플랫 (Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview, ])

# 가변(list, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)

# Tuple advanced
# Unpacking


x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)


# Mutable vs Immutable

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))


l *= 2
m *= 2

print(l, id(l))
print(m, id(m))


# List vs Array
# list : 융통성, 다양한 자료형, 범용적 사용
# array : 숫자기반, 리스트와 거의 호환
