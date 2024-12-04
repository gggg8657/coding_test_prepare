
from collections import defaultdict, deque


def move(atoms, N):
    # 방향 벡터 (0부터 7까지 순서대로 ↑, ↗, →, ↘, ↓, ↙, ←, ↖)
    direction_vectors = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    for atom in atoms:
        dx, dy = direction_vectors[atom[4]]
        offset = atom[3] % N  # 속도만큼 이동
        atom[0] = (atom[0] + dx * offset) % N
        atom[1] = (atom[1] + dy * offset) % N


def synthesis(atoms):
    new_atoms = []
    grid = defaultdict(list)

    # 각 위치별 원자 그룹화
    for atom in atoms:
        grid[(atom[0], atom[1])].append(atom)

    # 그룹화된 원자 처리
    for (x, y), atom_list in grid.items():
        if len(atom_list) == 1:
            new_atoms.append(atom_list[0])  # 합성 불필요
        else:
            total_mass = sum(a[2] for a in atom_list)
            total_speed = sum(a[3] for a in atom_list)
            direction_flag = all(a[4] % 2 == atom_list[0][4] % 2 for a in atom_list)
            count = len(atom_list)

            new_mass = total_mass // 5
            new_speed = total_speed // count

            if new_mass > 0:  # 질량이 0이면 소멸
                for i in range(4):
                    new_direction = i * 2 if direction_flag else i * 2 + 1
                    new_atoms.append([x, y, new_mass, new_speed, new_direction])

    return new_atoms


# 입력 처리
N, M, K = map(int, input().split())
atoms = deque()
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    atoms.append([x - 1, y - 1, m, s, d])

# 시뮬레이션 실행
for _ in range(K):
    move(atoms, N)
    atoms = deque(synthesis(list(atoms)))

# 결과 계산
print(sum(atom[2] for atom in atoms))
