def binary_search(A, key, low, high):     # 예제 4-5
    if(low <= high):                      # 항목들이 남아 있으면(종료 조건)
        mid = (low + high) // 2           # 정수 나눗셈 // : 몫을 반환
        if key == A[mid]:                 # 탐색 성공
            return mid                    # 인덱스 반환
        elif key < A[mid] :               # 왼쪽 부분 리스트 탐색
            return binary_search(A, key, low, mid-1)
        else :                            # 오른쪽 부분 리스트 탐색
            return binary_search(A, key, mid+1, high)
    return -1                             # 탐색 실패 : -1 반환

def binary_search_iter(A, key, low, high):  #예제 4-6
    while(low <= high) :                    # 항목들이 남아 있으면(종료 조건)
        mid = (low + high) // 2             
        if(key == A[mid]):                  # 탐색 성공
            return mid                      # 인덱스 반환
        elif (key > A[mid]):                # key가 mid값보다 크면
            low = mid + 1                   # mid+1 ~ high 사이 검색
        else :                              # key가 mid의 값보다 작으면
            high = mid - 1                  # low ~ mid-1 사이 검색
    return -1                               # 탐색 실패

# 테스트

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

key = 12
print(f"{key} 탐색 (순환) -->", binary_search(arr, key, 0, len(arr)-1))
print(f"{key} 탐색 (반복) -->", binary_search_iter(arr, key, 0, len(arr)-1))


