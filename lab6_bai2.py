from collections import deque


# BFS tim duong di ngan nhat (so canh) tren do thi khong trong so
def bfs_shortest_path(adj_list, start_node):
    visited = set([start_node])
    dist = {start_node: 0}
    queue = deque([start_node])
    traversal_order = []

    while queue:
        u = queue.popleft()
        traversal_order.append(u)

        # Duyet qua cac hang xom
        for v in adj_list[u]:
            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                queue.append(v)

    return traversal_order, dist


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    order, distances = bfs_shortest_path(graph, 0)
    print("Thu tu duyet BFS:", order)          # [0, 1, 2, 3]
    print("Khoang cach tu dinh 0:", distances)  # {0: 0, 1: 1, 2: 1, 3: 2}
