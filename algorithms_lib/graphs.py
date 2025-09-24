from typing import List, Dict, Tuple
import heapq
from collections import deque
def bfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    q = deque([start]); seen = {start}; order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v); q.append(v)
    return order
def dijkstra(n: int, edges: List[Tuple[int,int,int]], src: int) -> List[float]:
    g = [[] for _ in range(n)]
    for u, v, w in edges: g[u].append((v,w))
    dist = [float('inf')]*n; dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
def topo_sort_kahn(n: int, edges: List[Tuple[int,int]]) -> List[int]:
    indeg = [0]*n; g = [[] for _ in range(n)]
    from collections import deque
    for u, v in edges: g[u].append(v); indeg[v]+=1
    q = deque([i for i in range(n) if indeg[i]==0]); order=[]
    while q:
        u = q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return order if len(order)==n else []
