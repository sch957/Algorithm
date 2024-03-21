a = int(input("노드의 개수 : "))
node_list = []

for i in range(1, a + 1):
    data = int(input(f"노드 #{i}의 데이터: "))
    node_list.append(data)

print("리스트의 내용:", node_list)