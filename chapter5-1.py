# 일급 객체
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)


def factorial(n):
    """
    factorial fucntion -> n : int
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


# print(factorial(5))
# print(type(factorial))
# print(type(A))

# 변수 할당
var_func = factorial
# print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 반환가능 -> High Order Function
# map, filter, reduce

# print([var_func(i) for i in range(1, 6) if i % 2])

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성 (일반 함수 형태로)

print(reduce(lambda x, t: x + t, range(1, 11)))


# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str))  # -> True
print(callable(A))  # -> True
print(callable(list))  # -> True
print(callable(1))  # -> False


# partial 사용법 : 인수 고정 -> 콜백함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)

six = partial(five, 6)

print(six())  # -> 30

print([five(i) for i in range(1, 11)])
