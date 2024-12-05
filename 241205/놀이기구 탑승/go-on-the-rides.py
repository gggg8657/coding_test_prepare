n = int(input())
grid = [[0] * n for _ in range(n)]
like = {}
order = []
for _ in range(n * n):
    arr = list(map(int, input().split()))
    student, prefs = arr[0], arr[1:]
    like[student] = prefs
    order.append(student)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

for student in order:
    candidates = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                like_count = 0
                empty_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if in_bounds(nx, ny):
                        if grid[nx][ny] in like[student]:
                            like_count += 1
                        elif grid[nx][ny] == 0:
                            empty_count += 1
                candidates.append((-like_count, -empty_count, x, y))
    candidates.sort()
    x, y = candidates[0][2], candidates[0][3]
    grid[x][y] = student

# Calculate satisfaction
satisfaction = 0
for x in range(n):
    for y in range(n):
        student = grid[x][y]
        like_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_bounds(nx, ny):
                if grid[nx][ny] in like[student]:
                    like_count += 1
        if like_count > 0:
            satisfaction += 10 ** (like_count - 1)
print(satisfaction)