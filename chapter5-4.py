# 데코레이터 Decorator

# 장점
# 1. 중복제거, 코드간결
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통으로
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 감소 ?
# 2. 특정 기능에 한정됨 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습

import time


def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료시간
        et = time.perf_counter()
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ", ".join(repr(arg) for arg in args)
        # 결과출력
        print(f"[{et - st}] {name}({arg_str}) -> {result}")
        return result

    return perf_clocked


def time_func(seconds):
    time.sleep(seconds)


def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1(1))
print(none_deco2(1, 2, 3))

# 데코레이터 사용
print()


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


time_func(1)
sum_func(1, 2, 3, 2, 3, 2, 1)
