def partition(A, left, right):
    pivot = A[right]  # 피벗을 리스트의 마지막 원소로 선택합니다.
    i = left - 1  # 작은 원소들의 마지막 인덱스를 나타내는 변수입니다.

    for j in range(left, right):
        if A[j] <= pivot:  # 현재 원소가 피벗보다 작거나 같으면
            i += 1  # 작은 원소들의 영역을 확장하고
            A[i], A[j] = A[j], A[i]  # 해당 원소를 작은 원소들의 영역으로 이동합니다.

    A[i + 1], A[right] = A[right], A[i + 1]  # 피벗을 작은 원소들의 영역 끝에 배치합니다.
    return i + 1  # 피벗의 최종 위치를 반환합니다.

def quick_sort(A, left, right) :
    if left < right :
        mid = partition(A,left,right)
        quick_sort(A,left, mid-1)
        quick_sort(A,mid+1,right)

data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
quick_sort(data, 0, len(data)-1)      
print("QuickSort : ", data)  