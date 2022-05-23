# BFS 너비 우선 탐색 - 그래프
# 입력 : 그래프 g, 탐색 시작점 start
# 출력 : start에서 출발해 연결된 꼭짓점들을 출력

def dfs(g, start):
    stack = []
    done = set()

    stack.append(start)

    done.add(start)

    while stack:
        p = stack.pop()
        print(p)
        for x in g[p]:
            if x not in done:
                stack.append(x)
                done.add(x)

g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

dfs(g, 1)
# 방향은 상관 없다
# 왼쪽으로 뽑는 방법도 있을 건데 말이지

