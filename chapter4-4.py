# 해시 테이블 (hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리

# set -> 중복허용 x


# immutable Dict
from types import MappingProxyType

d = {"key": "value1"}

# Read only

d_frozen = MappingProxyType(d)

# error
# d_frozen["key2"] = "test"

s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Orange", "Kiwi"])
s3 = {3}
s4 = set()
s5 = frozenset({"Apple", "Orange", "Apple", "Orange", "Kiwi"})

s1.add("Melon")
print(s1)

# 추가 불가
# s5.add("Melon")

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터가 실행
from dis import dis

print("--------------")
print(dis("{10}"))
print("--------------")
print(dis("set([10])"))

# -> {}로 set 선언이 더 빠르다.


# Comprehending Set
from unicodedata import name

print("--------")
print({name(chr(i), "") for i in range(0, 256)})
