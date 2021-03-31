"""
Lambda Expression
"""
"""
람다 표현식 자체를 호출하기
(lambda 매개변수들 : 식)(인수들)
"""
print((lambda x: x**2)(10))  # 100

"""
람다 표현식 안에서는 변수 생성 불가
= 람다 표현식 바깥에 있는 변수 사용 가능
"""
y = 10
print((lambda x: x+y)(1))  # 11

"""
람다 표현식을 인수로 사용하기
"""
print(list(map(lambda x: x+10, [1, 2, 3])))  # [11, 12, 13]

"""
람다 표현식으로 매개 변수가 없는 함수 만들기
(lambda : x)()
(lambda : 1)()
"""
print((lambda: 1)())  # 1
