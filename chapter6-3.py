# 병행성 (Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# 코루틴 (Coroutine)

# yield, send : 메인 <-> 서브
# thread : os가 관리, CPU 코어에서 실시간, 시분할 비동기작업 -> 멀티스레드
# 코루틴 : 단일(single) 스레드, 스택을 기반으로 동작하는 비동기 작업
# def -> async, yield -> await

# 코루틴 제어, 상태저장, 양방향 전송
# 서브루틴 : 메인 루틴에서 호출 -> 서브루틴에서 수행 (흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# -> thread에 비해 오버헤드 감소

# thread : 싱글 스레드 -> 멀티 스레드 -> 공유자원 -> 교착상태, 코딩 복잡, 컨텍스트 스위칭 비용발생, 자원소비 가능성 증가

# 코루틴 ex1
def coroutine1():
    print(">>> coroutine started")
    i = yield
    print(f">>> cotourine received : {i}")


# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()
print(cr1)
print(type(cr1))

# yield 지점까지 서브루틴 수행
# next(cr1)

# send() 기본 전달값 None
# 값 전송
# cr1.send(100)

# 잘못된 사용
# yield 에서 멈춘 후 send 해야함
# cr2 = coroutine1()
# cr2.send()


# 코루틴 ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPEND : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print(f">>> coroutine started : {x}")
    y = yield x
    print(f">>> coroutine received : {y}")
    z = yield x + y
    print(f">>> coroutine received : {z}")


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))
print(cr3.send(100))

print()
print()


# 코루틴 ex3
# StopIteration 자동처리 (>=3.5 -> await)


def generator1():
    for x in "AB":
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()


def generator2():
    yield from "AB"
    yield from range(1, 4)


t3 = generator2()
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))
