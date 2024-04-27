def multMul(M1, M2):
    result = []
    for i in range(len(M1)):
        row = []
        for j in range(len(M2[0])):
            sum = 0
            for k in range(len(M2)):
                sum += M1[i][k] * M2[k][j]
            row.append(sum)
        result.append(row)
    return result
def powerMat(x, n):             # 예제 4.9 행렬 거듭제곱 알고리즘
    if n == 1:
        return x
    elif n % 2 == 0:
        half_power = powerMat(x, n // 2)
        return multMul(half_power, half_power)
    else:
        half_power = powerMat(x, (n - 1) // 2)
        return multMul(x, multMul(half_power, half_power))
# 예제 행렬
M1 = [[1, 2], [3, 4]]           
M2 = [[5, 6], [7, 8]]
# powerMat 함수를 위한 예제 행렬
x = [[1, 1], [1, 0]]  # 피보나치 수열 계산을 위한 행렬
# 행렬 곱셈 테스트
result_mul = multMul(M1, M2)
print("행렬 곱셈 결과:")
for row in result_mul:
    print(row)
# powerMat 함수 테스트
power = 5
result_power = powerMat(x, power)
print("\n행렬 거듭제곱 결과:")
for row in result_power:
    print(row)