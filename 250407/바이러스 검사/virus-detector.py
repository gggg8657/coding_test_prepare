N = int(input())

array = list(map(int, input().split()))

C, m = map(int, input().split())

result = 0
for i in range(N):
    res = array[i] - C
    result += 1
    if res>0:
        if res - (m * res//m) >= 0:
            result+=1
        else : result+=0
        result += res//m

print(result)