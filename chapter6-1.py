# 병행성 (Concurrency)
# Iterator, Generator

# 파이썬 반복가능한 타입
# collections, text, list, dict, set, tuple, ... : iterable

t = "ABCD"

# print(dir(t))

w = iter(t)
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
print(hasattr(t, "__iter__"))


from collections import abc

print(isinstance(t, abc.Iterable))


# next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("Stop Iteration.")
        self._idx += 1
        return word

    def __repr__(self):
        return f"WordSplit({self._text})"


wi = WordSplitter("Do today what you could do tommorrow")
print(wi)

# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> generator 사용 권장
# 2. 단위실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리조각 사용
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터

    def __repr__(self):
        return f"WordSplitGenerator({self._text})"


wg = WordSplitGenerator("Do today what you could do tommorrow")
wt = iter(wg)

next(wt)
next(wt)
next(wt)
next(wt)
next(wt)
next(wt)
next(wt)
next(wt)
