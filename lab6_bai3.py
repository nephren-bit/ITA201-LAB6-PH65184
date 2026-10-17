# DFS de quy: di sau nhat theo 1 nhanh roi quay lui
def dfs_traversal(adj_list, start_node):
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in adj_list[u]:
            if v not in visited:
                dfs(v)

    dfs(start_node)
    return order


# Phat hien chu trinh trong do thi vo huong: gap dinh ke da tham ma khong phai cha -> co chu trinh
def has_cycle_undirected(adj_list, num_nodes):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in adj_list[u]:
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    # Duyet moi dinh de xu ly do thi nhieu thanh phan lien thong
    for node in range(num_nodes):
        if node not in visited and dfs(node, -1):
            return True
    return False


if __name__ == "__main__":
    graph_with_cycle = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}  # Tam giac 0-1-2-0
    graph_tree = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}          # Cay 0-1-3, 0-2

    print("DFS tren graph_tree tu dinh 0:", dfs_traversal(graph_tree, 0))  # [0, 1, 3, 2]
    print("graph_with_cycle co chu trinh:", has_cycle_undirected(graph_with_cycle, 4))  # True
    print("graph_tree co chu trinh:", has_cycle_undirected(graph_tree, 4))              # False
