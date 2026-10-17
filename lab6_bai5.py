from collections import deque


# Flood Fill bang BFS: doi mau vung lien thong 4 huong co cung mau voi pixel goc
def flood_fill_bfs(image, start_row, start_col, new_color):
    M, N = len(image), len(image[0])
    result = [row[:] for row in image]  # Khong sua anh goc
    old_color = result[start_row][start_col]

    # Mau moi trung mau cu -> khong lam gi, tranh vong lap vo han
    if old_color == new_color:
        return result

    queue = deque([(start_row, start_col)])
    result[start_row][start_col] = new_color  # To mau ngay khi dua vao queue = danh dau da tham

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Tren, Duoi, Trai, Phai
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Kiem tra bien va cung mau ban dau
            if 0 <= nr < M and 0 <= nc < N and result[nr][nc] == old_color:
                result[nr][nc] = new_color
                queue.append((nr, nc))

    return result


def print_image(img):
    for row in img:
        print("  ", row)


if __name__ == "__main__":
    image = [
        [1, 1, 1, 0, 0],
        [1, 1, 0, 0, 2],
        [1, 0, 0, 2, 2],
        [0, 0, 2, 2, 2]
    ]

    print("Anh goc:")
    print_image(image)

    print("Flood fill tu (0, 0) mau 1 -> 7:")
    print_image(flood_fill_bfs(image, 0, 0, 7))

    print("Flood fill tu (1, 4) mau 2 -> 5:")
    print_image(flood_fill_bfs(image, 1, 4, 5))

    print("Flood fill tu (0, 3) voi new_color trung mau cu (0 -> 0), khong treo:")
    print_image(flood_fill_bfs(image, 0, 3, 0))

# Phan tich do phuc tap (anh M x N):
# - Thoi gian O(M * N): moi pixel duoc dua vao queue toi da 1 lan (vi bi doi mau ngay khi vao
#   queue nen khong con trung old_color), va moi pixel chi xet 4 lan can -> 4 * M * N phep kiem tra.
# - Bo nho O(M * N): truong hop xau nhat ca anh cung mau, queue co the chua toi O(M * N) pixel
#   (thuc te BFS chi giu "duong bien" cua vung loang, co the den O(M + N) voi anh dac),
#   cong them ban sao ket qua M * N. Neu sua truc tiep tren anh thi khong can mang visited rieng.
#
# Vi sao luoi anh 2D tuong duong do thi phang bac toi da 4?
# - Moi pixel (r, c) la 1 dinh; canh noi toi (r+-1, c) va (r, c+-1) -> bac <= 4
#   (pixel o bien co bac 3, o goc co bac 2). Do do so canh E <= 2 * M * N = O(V).
# - Cac canh chi noi cac o ke nhau theo hang/cot nen co the ve do thi tren mat phang ma khong
#   co 2 canh nao cat nhau (chinh la luoi o vuong) -> do thi phang.
# - Vi E = O(V) nen BFS/DFS O(V + E) tren luoi chi la O(M * N), khong can luu ma tran ke
#   (M*N)^2 ma sinh hang xom "ngam" bang 4 vector huong.
