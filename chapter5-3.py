# 외부에서 호출된 함수의 변수 값, 상태(레퍼런스) 복사 후 저장 -> 나중에 접근가능

# Closure 사용
def closure_ex1():
    # Free variable : 자유변수
    series = []

    def averager(v):
        series.append(v)
        print(f"inner >> {series} / {len(series)}")
        return sum(series) / len(series)

    # 함수 자체를 실행하지 않고 반환
    return averager


avg_closure1 = closure_ex1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(20))

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)

# 잘못된 클로저 사용


def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외

# 아래는 동작함
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(10))
