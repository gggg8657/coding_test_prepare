import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]
j=1
for col in range(n):
    i=j
    for row in range(m):
        arr[col][row] = i
        i+=n
    j+=1

# Print the transposed data
for row in arr:
    print(" ".join(map(str, row)))