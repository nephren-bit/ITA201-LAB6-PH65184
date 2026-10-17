from collections import deque


# Dem va liet ke cac thanh phan lien thong (tuong duong phan cum du lieu)
def count_and_find_components(adj_list, num_nodes):
    visited = set()
    components = []

    for start in range(num_nodes):
        if start in visited:
            continue

        # Gap dinh chua tham -> cum moi, loang BFS het cum do
        visited.add(start)
        queue = deque([start])
        component = []
        while queue:
            u = queue.popleft()
            component.append(u)
            for v in adj_list.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        components.append(sorted(component))

    return len(components), components


if __name__ == "__main__":
    # 2 cum: {0, 1} va {2, 3, 4}
    discrete_graph = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    count, comps = count_and_find_components(discrete_graph, 5)
    print("So thanh phan lien thong:", count)  # 2
    print("Danh sach cum:", comps)             # [[0, 1], [2, 3, 4]]
