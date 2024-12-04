#TODO [1] : mov per sec
#TODO [2] : if in block more than two 합성 in each block
# 같은 칸에 있는 원자들은, 각각의 질량과 속력을 모두 합한 하나의 원자로 합쳐짐.
# if 합쳐짐 -> 네개로 나누고 (if 속력 질량 방향 나누는 기준)
# 나누어진 원자들은 모두 해당 칸에 위치하고
#TODO [3] : 속력 질량 방향 나누는 기준 1. 질량 = 합쳐진거 / 5,
# 속력 = 합쳐진거 / 합쳐진 원자의 개수,
# 방향 = 상하좌우||대각로 합쳐짐 -> 상하좌우 || 잡탕 -> 대각
# 소수점 아래 수 날림 == (// or int 처리)
# 질량이 0 이면 소멸
# 이동 과정 중에 원자가 만나는 경우는 합성으로 고려하지 않음. -> 1턴 이후 합성해야됨

import sys

def synthesis(arr):
    new_list=[]
    while arr:
        i = 0
        syntar = []
        new_atom = [0]*6 # in new atom there is flag in address 4 if flag is 0 상하좌우, else 대각선 in new atom
        x, y = arr[i][0], arr[i][1]  # src x,y
        tmp = arr[i][4]%2
        syntar.append(arr[i])
        for tar in range(i+1, len(arr)):
            if x == arr[tar][0] and y == arr[tar][1]:
                # print("synthesis target occur")
                syntar.append(arr[tar])
                new_atom[0] = arr[i][0] #syn pos
                new_atom[1] = arr[i][1]
        for srcs in syntar:
            new_atom[2]+=srcs[2] #syn mass
            new_atom[3]+=srcs[3] #syn spedd
            if srcs[4]%2 != tmp: new_atom[4] =1 #syn direction flag if different from before
            new_atom[5] +=1
        new_list.append(new_atom)
        for a in syntar:
            arr.pop(arr.index(a))
        i+=1
    return new_list,arr
                    #srcs[4]

                    #나눠지는 원자 방향 정해줘야겠네
import copy
def divide(newt, arr):
    while newt:
        new = newt[0]
        tmp =[0]*5
        size = new[2]//5
        speed = new[3] // new[5]
        if size<=0:
            newt.pop(newt.index(new))
        else :
            for _ in range(4):
                tmp[0] = new[0]
                tmp[1] = new[1]
                tmp[2] = size
                tmp[3] = speed
                if new[4] ==1 : tmp[4] = _*2+1
                else : tmp[4] = _*2
                x = copy.deepcopy(tmp)
                arr.append(x)
            newt.pop(newt.index(new))
    return arr

def move(arr):
    for atom in arr:
        if atom[4]==0:
            atom[0] -= 1*atom[3]
        elif atom[4]==1:
            atom[0]-=1*atom[3]
            atom[1] += 1*atom[3]
        elif atom[4]==2:
            atom[1] += 1*atom[3]
        elif atom[4]==3:
            atom[0] += 1*atom[3]
            atom[1] += 1*atom[3]
        elif atom[4]==4:
            atom[0] += 1*atom[3]
        elif atom[4]==5:
            atom[0] += 1*atom[3]
            atom[1] -= 1*atom[3]
        elif atom[4]==6:
            atom[1] -= 1*atom[3]
        elif atom[4]==7:
            atom[0] -= 1*atom[3]
            atom[1] -= 1*atom[3]
        if N<=atom[0] or atom[0]<0:
            atom[0] -=N
        if N<=atom[0] or atom[0]<0:
            atom[1] -=N
    return arr

input = sys.stdin.readline

N, M, K = map(int, input().split())
# n : arr_size, m : atom_cnt, k : ex_time

arr = [[0]*N for _ in range(N)]

info = []
for _ in range(M):
    info.append(list(map(int, input().split())))
    # arr[info[_][0]][info[_][1]]

    # x , y : pos, m : 질량, s : 속력, d : 방향  0부터 7까지 순서대로 ↑, ↗, →, ↘, ↓, ↙, ←, ↖
#좌표로만 이동

# print(info)

for _ in range(K):
    if M == 1: break
    info = move(info)
    # print(info)
    new_atom, arr = synthesis(info)
    # print(info)
    info = divide(new_atom, info)
    # print(info)


ans = 0
for _ in info:
    ans += _[2]
print(ans)

