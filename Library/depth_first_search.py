from collections import deque, defaultdict, Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
'''for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:'''

# グラフ作成
N, Q = map(int,input().split())
G = defaultdict(list)
for i in range(1, N):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

# 深さ優先探索
def dfs(G, v):
    global time, first_order, seen, last_order
    time += 1
    first_order[v - 1] = time  # 行きがけ

    seen[v - 1] = True  # v を訪問済みにする
    # v から行ける各頂点 next_v について
    for next_v in G[v]:
        if seen[next_v - 1]:
            continue
        dfs(G, next_v)

    time += 1
    last_order[v - 1] = time  # 帰りがけ



#よくある壁ぶつかり迷路問題 ｓからtに行けるか

H, W = map(int,input().split())
field = [input() for _ in range(H)]
#print(field)
seen = [[False]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            seen[i][j] = True
        elif field[i][j] == 's':
            sy = i
            sx = j
        elif field[i][j] == 'g':
            gy = i
            gx = j
#print(sx, sy)
#print(gx, gy)
#print(seen)
def dfs(h, w):
    seen[h][w] = True

    # 四方向への分岐
    for dx, dy in dd:
        h_1 = h + dy
        w_1 = w + dx

        # 枠外や壁に当たったらスルー
        if h_1 < 0 or h_1 > H - 1 or w_1 < 0 or w_1 > W - 1:
            continue
        if field[h_1][w_1] == '#':
            continue

        # もう探索済みならスルー
        if seen[h_1][w_1]:
            continue

        dfs(h_1, w_1)

dfs(sy, sx)
if not seen[gy][gx]:
    print('No')
else:
    print('Yes')


# 島が何個連結するか
ans = 0
for i in range(H):
    for j in range(W):
        if not seen[i][j]:
            ans += 1
            dfs(i, j)
print(ans)