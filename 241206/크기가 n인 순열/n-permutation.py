# n 입력
n = int(input())

# 함수들
# print_ans()
def print_ans():
    for num in combs:
        print(num, end=' ')
    print()
# make_comb(curr_idx)
def make_comb(curr_idx):
    # 종료조건
    if curr_idx == n:
        print_ans()
        return
    # 넣어주기
    for i in range(1, n+1):
        # 방문한 곳이면
        if visited[i]:
            continue
        
        combs.append(i)
        visited[i] = True
        make_comb(curr_idx + 1)
        combs.pop()
        visited[i] = False

# 설계
# combs, visited
combs, visited = [], [False for _ in range(n+1)]

# make_comb(0)
make_comb(0)