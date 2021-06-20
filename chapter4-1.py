# 시퀀스형
# 컨테이너 (Container : 서로다른 자료형[list, tuple, collections.deque, ])
# 플랫 (Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview, ])

# 가변(list, bytearray, array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급
# Comprehending lists
chars = "+_)(*&^%$#@!"
code_list1 = []

for s in chars:
    code_list1.append(ord(s))

print(code_list1)

# comprehending lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# comprehending lists + map, filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])


# Generator 생성

import array

# Generator : 한 번에 한 개의 항목을 생성 (메모리에 유지 X)
tuple_g = (ord(s) for s in chars)
print(tuple_g)
print(next(tuple_g))

array_g = array.array("I", (ord(s) for s in chars))
print(array_g)
print(array_g.tolist())


# generator 예제
print(str(c) + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21))
# for s in (str(c) + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
#     print(s)
