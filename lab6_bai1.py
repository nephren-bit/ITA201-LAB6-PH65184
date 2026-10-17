# Xay dung Ma tran ke va Danh sach ke cho do thi vo huong
def build_graph_representations(num_nodes, edges):
    # 1. Khoi tao
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    adj_list = {i: [] for i in range(num_nodes)}

    # 2. Dien thong tin canh
    for u, v in edges:
        # Ma tran ke (doi xung)
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
        # Danh sach ke
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_matrix, adj_list


if __name__ == "__main__":
    num_nodes = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    matrix, adj_list = build_graph_representations(num_nodes, edges)

    print("Ma tran ke (Adjacency Matrix):")
    for row in matrix:
        print(row)
    print("Danh sach ke (Adjacency List):")
    print(adj_list)
    # Ky vong: [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
    #          {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

# Nhan xet: Ma tran ke ton O(N^2) bo nho nhung kiem tra canh (u, v) trong O(1);
# Danh sach ke chi ton O(N + E), phu hop voi mang xa hoi thua (moi nguoi it ban so voi N).
