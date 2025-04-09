di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

class Unit:
    def __init__(self, uid, si, sj, h, w, k):
        self.uid = uid
        self.si = si
        self.sj = sj
        self.h = h
        self.w = w
        self.k = k

    def position_after_move(self, dr):
        return self.si + di[dr], self.sj + dj[dr]

    def update_position(self, dr):
        self.si += di[dr]
        self.sj += dj[dr]

    def get_area(self, dr=None):
        # 이동 후 영역 리턴 (이동 전이면 dr=None)
        si = self.si + di[dr] if dr is not None else self.si
        sj = self.sj + dj[dr] if dr is not None else self.sj
        return si, sj, self.h, self.w

    def take_damage(self, dmg):
        self.k -= dmg

    def is_dead(self):
        return self.k <= 0

N, M, Q = map(int, input().split())
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]

units = {}
init_k = [0]*(M+1)

for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = Unit(m, si, sj, h, w, k)
    init_k[m] = k

def check_collision(a1, a2):
    si1, sj1, h1, w1 = a1
    si2, sj2, h2, w2 = a2
    return si1 <= si2 + h2 - 1 and si1 + h1 - 1 >= si2 and \
           sj1 <= sj2 + w2 - 1 and sj1 + w1 - 1 >= sj2

def push_unit(start_id, dr):
    q = [start_id]
    pset = {start_id}
    damage = [0] * (M + 1)

    while q:
        cur_id = q.pop(0)
        cur_unit = units[cur_id]
        ni, nj, h, w = cur_unit.get_area(dr)

        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    damage[cur_id] += 1

        for other_id, other_unit in units.items():
            if other_id in pset:
                continue
            if check_collision((ni, nj, h, w), other_unit.get_area()):
                q.append(other_id)
                pset.add(other_id)

    damage[start_id] = 0

    for idx in pset:
        unit = units[idx]
        if unit.k <= damage[idx]:
            del units[idx]
        else:
            unit.update_position(dr)
            unit.take_damage(damage[idx])

for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)

ans = 0
for idx, unit in units.items():
    ans += init_k[idx] - unit.k
print(ans)