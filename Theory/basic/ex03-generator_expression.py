"""
# Generator Expression
= generator object를 간결하게 만들 수 있다.
= comprehension과 유사하다.
= generator comprehension과 유사하다.
"""

ge = (x for x in range(10))
print(ge)  # <generator object <genexpr> at 0x01D4BB50>

ge = (n*n for n in range(1001))
print(ge)  # <generator object <genexpr> at 0x01D4BB50>

# 10개 출력
for i in range(10):
    value = next(ge)
    print(value)

# 나머지 모두 출력
for x in ge:
    print(x)

"""
Generator 함수 - 추가 공부 필요
"""
