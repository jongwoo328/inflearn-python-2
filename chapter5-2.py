# 파이썬 변수 범위 (scope)

# ex1
def func_v1(a):
    print(a)
    print(b)


# ex2
b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)

# ex3
c = 30


# def func_v3(a):
#     print(a)
#     print(c)
#     c = 40


# func_v3(10)


# Closure 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태 (Dead Lock)
# 메모리를 공유하지않고 메시지 전달로 처리
# 클로저는 공유하되, 변경되지 않음 (Immutable, Read only) -> 함수형 프로그래밍
# 클로저는 불변 자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100
print(a + 100)
print(a + 1000)

# 결과누적(함수 사용)
print(sum(range(1, 11)))

# 클래스 이용
class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print(f"inner >> {self._series} / {len(self._series)}")
        return sum(self._series) / len(self._series)


averager_cls = Averager()
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(123))
