def factorial_recur(n):                 
    if n == 1: 
        return 1
    else:
        return n * factorial_recur(n - 1)

def factorial_iter(n):
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result   

# 테스트
print(factorial_recur(5)) 
print(factorial_recur(3)) 
print(factorial_recur(10)) 
print(factorial_iter(5)) 
print(factorial_iter(3)) 
print(factorial_iter(10)) 