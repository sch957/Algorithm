# 작성자 : 202010779 송석한
# 작성일 : 2024.04.01
# 프로그램 내용 : 반복적인 팩토리얼 알고리즘

def factorial(n) :              # 반복 구조로 구현한 factorial 함수
    result = 1
    for k in range(n, 0, -1):   # k: n, n-1, ....., 2, 1
        result = result * k     # 기본 연산
    return result   

print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(10))