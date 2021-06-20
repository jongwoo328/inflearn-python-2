# 2가지 패턴
# concurrent.futures map
# concurrent.futures wait, as_complete


import os
import time

from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
    wait,
    as_completed,
)

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (Generator)


def sum_generator(n):
    return sum(n for n in range(1, n + 1))


# wait, as_complete


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # Futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor
    with ProcessPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print(f"Scheduled for {work} : {future}")

        # # wait : 모두 완료될 때 까지 기다림
        # # 시간 제어 가능
        # result = wait(futures_list, timeout=3)
        # # 성공
        # print("Completed Tasks : " + str(result.done))
        # # 3초 후 진행중 (실패)
        # print("Pending ones after waiting for 3 seconds : " + str(result.not_done))
        # # 결과값 출력
        # print([future.result() for future in result.not_done])

        # as_completed : 완료되는 것 부터 반환
        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # 결과 확인
            print(f"Future result : {result}, Done : {done}")
            print(f"Future Cancelled : {cancelled}")
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = "\n Time: {}"
    print(msg.format(end_tm))


if __name__ == "__main__":
    main()
