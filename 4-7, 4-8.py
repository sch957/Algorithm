def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result *= x
    return result
def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)
    

print(slow_power(2, 5)) 
print(power(2, 5))