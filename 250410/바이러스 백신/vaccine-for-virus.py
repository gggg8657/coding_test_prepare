
from collections import deque
import copy
N, M = map(int, input().split())

world = []
newworld=[]
hosq = deque() #병원들 위치 기억
for _ in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:hosq.append([_,j])
        
    world.append(tmp)

newworld = copy.deepcopy(world)

combq = deque() # posq_1, posq_2 와 같은 형태로 queue를 저장
from itertools import combinations
combq= deque(combinations(hosq, M))

posq = deque() # [r_1, c_1], [r_2, c_2] ... 형태로 좌표를 저장

dr, dc = [-1,0,1,0], [0,1,0,-1]

step = 1

result=[]

ans = 0
APPENDRESULT = True
while combq:
    posq = deque(combq.popleft())
    while any(0 in row for row in world):
        tmpq=deque()
        while posq:
            r,c = posq.popleft()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<N and 0<=nc<N and world[nr][nc] == 0:
                    world[nr][nc]=step
                    tmpq.append([nr,nc])
                elif 0<=nr<N and 0<=nc<N and world[nr][nc] == 2:
                    tmpq.append([nr,nc])
                    world[nr][nc]=-1

        for item in tmpq: posq.append(item)
        step+=1

        if len(posq) <=0 and any(0 in row for row in world): 
            ans =-1
            APPENDRESULT = False
            break
    if len(combq)==0 and len(posq) == 0 and APPENDRESULT == False and len(result)==0: 
        result.append(ans)
    elif APPENDRESULT: 
        result.append(step-1)
        step =1
        world = copy.deepcopy(newworld)


    
print(min((result)))
'''
3 1
2 1 1
0 1 2
1 1 1
'''