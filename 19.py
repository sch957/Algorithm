def min_cost_assignment(cost_matrix):
    n = len(cost_matrix)
    assignments = []

    # 각 근로자가 처리하는 각 일에 대한 비용 계산
    for worker in range(n):
        min_cost = float('inf')
        min_job = -1
        for job in range(n):
            if cost_matrix[worker][job] < min_cost:
                min_cost = cost_matrix[worker][job]
                min_job = job
        assignments.append((worker, min_job))
    
    total_cost = sum(cost_matrix[worker][job] for worker, job in assignments)
    
    return total_cost, assignments

# 간단한 입력으로 테스트
cost_matrix = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

total_cost, assignments = min_cost_assignment(cost_matrix)
print("전체 비용:", total_cost)
print("일 배정 결과:")
for worker, job in assignments:
    print("Worker", worker+1, ":", "Job", job+1)
