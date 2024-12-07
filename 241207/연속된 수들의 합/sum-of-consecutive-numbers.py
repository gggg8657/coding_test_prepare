import sys

input = sys.stdin.readline

n = int(input())

count = 0
m = 1
    
while m * (m - 1) // 2 < n:
    # n - m*(m-1)/2가 m의 배수인지 확인
    if (n - m * (m - 1) // 2) % m == 0:
        count += 1
    m += 1

print(count)
    

