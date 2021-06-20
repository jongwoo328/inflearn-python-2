# asyncio : 비동기 I/O Coroutine 작업

# Blocking I/O
# -> 호출 된 함수가 자신의 작업이 완료될 때 까지 제어권을 가지고 있음
# Non Blocking I/O
# -> 호출된 함수가(서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# Thread 단점 : 디버깅, 자원 접근 시 레이스컨디션, 데드락 -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 (단일 스레드에서) -> Lock 관리 필요 X
# 코루틴 단점 : 사용 함수가 비동기로 구현되어이썩나, 직접 비동기로 구현해야 한다.

import asyncio
import timeit
import threading

from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

# 실행 시작 시간

start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장 (게시판성 커뮤니티)

urls = [
    "http://daum.net",
    "https://naver.com",
    "http://mlbpark.donga.com",
    "https://tistory.com",
    "https://wemakeprice.com",
]


async def fetch(url, executor):
    # 스레드명 출력
    print("Thread Name : ", threading.current_thread().getName(), "Start", url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    print("Thread Name : ", threading.current_thread().getName(), "Done", url)
    return res.read()[0:5]


async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather 에서 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print("Result : ", rst)


if __name__ == "__main__":
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())

    duration = timeit.default_timer() - start

    # 총 실행시간
    print("Total Running Time : ", duration)
