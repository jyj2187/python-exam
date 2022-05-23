# 파이썬의 Queue 패키지를 사용하는 방법
from queue import Queue


def bfs(graph, start_node):
    visit = set()  # 아래 댓글에서도 지적했듯이 dictionary나 set으로 구현하는 것이 더 효율적입니다.
    q = Queue()

    q.put(start_node)

    while q.qsize() > 0:
        node = q.get()
        if node not in visit:
            visit.add(node)
            for nextNode in graph[node]:
                q.put(nextNode)
    return visit


# 기존에 사용한 visit을 딕셔너리로 사용하는 방법
def bfs2(graph, start_node):
    visit = {}
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])
    return visit
