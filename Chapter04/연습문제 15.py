def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # 리스트를 세 부분으로 나누기
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3
        
        # 각 구간의 중간 값과 타겟 비교
        if arr[one_third] == target:
            return one_third
        elif arr[two_third] == target:
            return two_third
        elif target < arr[one_third]:
            right = one_third - 1
        elif target > arr[two_third]:
            left = two_third + 1
        else:
            left = one_third + 1
            right = two_third - 1
            
    return -1  # 탐색 실패 시 -1 반환

# 테스트
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 19
result = ternary_search(arr, target)
if result != -1:
    print(f"타겟 {target}은(는) 인덱스 {result}에 있습니다.")
else:
    print(f"타겟 {target}을(를) 찾을 수 없습니다.")
