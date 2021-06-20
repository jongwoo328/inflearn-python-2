# 병행성 (Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도


def generator_ex1():
    print("Start")
    yield "A Point"
    print("Continue")
    yield "B Point"
    print("End")


temp = iter(generator_ex1())

print(temp)

for v in generator_ex1():
    print(v)

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp3:
    print(i)


# Generator 중요함수
# count, takewhile, filterfalse, accumulator, chain, product, groupby

import itertools

gen1 = itertools.count(1, 2.5)  # 시작값, 증가단위

# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))
# for v in gen2:
#     print(v)

gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
# for v in gen3:
#     print(v)

# 누적합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
# for v in gen4:
#     print(v)

# 연결1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
# print(list(gen5))

# 개별
gen6 = itertools.product("ABCDE", repeat=2)
# print(list(gen6))


# 그룹화
gen7 = itertools.groupby("AAAABBBCCCDDDEEE")
# print(list(gen7))
for chr, group in gen7:
    print(chr, " : ", list(group))
