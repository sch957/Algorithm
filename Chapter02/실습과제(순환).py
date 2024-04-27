# 작성자 : 202010779 송석한
# 작성일 : 2024.04.01
# 프로그램 내용 : 순환적인 팩토리얼 알고리즘

def factorial(n) :                  # 순환적으로 구현한 factorial 함수
    if n == 1 :                     # 종료 조건
        return 1                    # 순환을 멈추는 부분
    else :                          
        return n * factorial(n-1)  # 자기 자신을 순환적으로 호출
    

print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(10))    