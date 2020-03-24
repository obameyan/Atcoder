from collections import deque, defaultdict, Counter

#よくある幅優先探索　迷路ゴールまでの最短経路問題

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = []
for i in range(R):
    field.append(input())
dist = [[-1] * C for _ in range(R)]
# print(dist)
# print(field)
# print(dist)

que = deque()
que.append([sy - 1, sx - 1])
dist[sy - 1][sx - 1] = 0
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while que:
    vy, vx = que.popleft()

    # 次に進める場所
    for i, j in dd:
        next_vy = vy + i
        next_vx = vx + j

        # 壁に当たったり、枠外ならスキップ
        if next_vy > R - 1 or next_vy < 0 or next_vx > C - 1 or next_vx < 0:
            continue
        if field[next_vy][next_vx] == '#':
            continue
        # 一回行ったことのある
        if dist[next_vy][next_vx] >= 0:
            continue

        # もしゴールにあたったら終了
        if next_vy == gy - 1 and next_vx == gx - 1:
            dist[next_vy][next_vx] = dist[vy][vx] + 1
            print(dist[gy - 1][gx - 1])
            exit()

        dist[next_vy][next_vx] = dist[vy][vx] + 1

        que.append([next_vy, next_vx])
