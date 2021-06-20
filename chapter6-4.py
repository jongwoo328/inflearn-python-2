# Future 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> File, Network I/O -> 동시성 활용 권장

# futures : 비동기 실행을 위한 API를 고 수준으로 작성 -> 사용하기 쉽도록 개선

# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# GIL (Global Interpreter Lock)
# 두 개 이상의 스레드가 동시에 실행 될 떄 하나의 자원을 액세스 하는 경우 -> 문제점 방지하기 위해
# 리소스 전체에 Lock -> Context Switch (문맥 교환)

# -> 멀티프로세싱 사용, CPython 사용


import os
import time

from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (Generator)


def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서를 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = "\n Result -> {} Time: {}"
    print(msg.format(list(result), end_tm))


if __name__ == "__main__":
    main()
