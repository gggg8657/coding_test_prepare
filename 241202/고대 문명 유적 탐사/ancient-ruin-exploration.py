def rotate(arr, start_row, start_col):
    # 3x3 부분 회전 (90도 시계 방향)
    return [[arr[start_row + 3 - col - 1][start_col + row] for col in range(3)] for row in range(3)]

def bfs(arr, visited, start_row, start_col, clear_flag):
    queue = [(start_row, start_col)]
    connected_cells = {(start_row, start_col)}
    count = 1
    visited[start_row][start_col] = True

    while queue:
        current_row, current_col = queue.pop(0)
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = current_row + d_row, current_col + d_col
            if (0 <= next_row < 5 and 0 <= next_col < 5 and
                not visited[next_row][next_col] and
                arr[current_row][current_col] == arr[next_row][next_col]):
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
                connected_cells.add((next_row, next_col))
                count += 1

    if count >= 3:  # 연결된 칸이 3개 이상인 경우
        if clear_flag:  # 지우기
            for row, col in connected_cells:
                arr[row][col] = 0
        return count
    return 0

def count_clear(arr, clear_flag):
    visited = [[False] * 5 for _ in range(5)]
    return sum(bfs(arr, visited, row, col, clear_flag)
               for row in range(5) for col in range(5) if not visited[row][col])

def fill_empty(arr, lst):
    for col in range(5):
        for row in range(4, -1, -1):
            if arr[row][col] == 0 and lst:
                arr[row][col] = lst.pop(0)

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
answers = []

for _ in range(K):
    best_arr, max_count = None, 0

    for rotation in range(1, 4):  # 회전 수
        for start_row in range(3):
            for start_col in range(3):
                temp_arr = [row[:] for row in arr]
                for _ in range(rotation):
                    subgrid = rotate(temp_arr, start_row, start_col)
                    for row in range(3):
                        for col in range(3):
                            temp_arr[start_row + row][start_col + col] = subgrid[row][col]
                count = count_clear(temp_arr, clear_flag=0)
                if count > max_count:
                    max_count, best_arr = count, temp_arr

    if max_count == 0:
        break

    arr = best_arr
    total_removed = 0
    while True:
        removed = count_clear(arr, clear_flag=1)
        if removed == 0:
            break
        total_removed += removed
        fill_empty(arr, lst)

    answers.append(total_removed)

print(*answers)