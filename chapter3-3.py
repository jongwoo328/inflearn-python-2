# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# named tuple

from collections import namedtuple

Point = namedtuple("Point", "x y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3, pt4)
# print(pt3.x, pt3[0])

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)


# named tuple 선언방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")
Point4 = namedtuple("Point", "x y x class", rename=True)  # default = False

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

temp_dict = {"x": 10, "y": 20}
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)


# namedtuple 메소드
temp = [52, 35]

# _make() : 새로운 객체 생성 by list
p4 = Point1._make(temp)
print(p4)


# _fields : 필드네임 확인
print(p1._fields, p2._fields)


# _asdict() : OrderdDict 반환
print(p1._asdict())


# 실 사용 실습
# 반에 20명 학생, 4 개의 반 (A, B, C, D)

Classes = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

print(numbers)
print(ranks)

# studnets
students = [Classes(rank, number) for rank in ranks for number in numbers]


# 추천
students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]


# 출력
for s in students:
    print(s)
