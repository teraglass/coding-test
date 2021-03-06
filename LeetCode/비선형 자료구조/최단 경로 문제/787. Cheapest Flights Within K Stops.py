# 다익스트라 알고리즘 응용
# --> TLE 발생
import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:  # 현재 노드가 도착지라면 결과를 리턴하고 종료
                return price
            if k >= 0:
                k += 1
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1


# Runtime 100~108 풀이
# 1. weight
# -> 해당 노드를 방문했던 경로의 (price, k)를 저장
# 2. 우선순위 큐에 push하는 조건 추가
# 해당 노드 weight의 price > push할 노드의 price
# 해당 노드 weight의 k <= push할 노드의 k
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, K)] * n
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or k-1 >= weight[v][1]:
                        weight[v] = (alt, k-1)
                        heapq.heappush(Q, (alt, v, k - 1))
        return -1

# 벨만포드 변형

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0
        for _ in range(k+1):
            prevDistances = distances[:]
            for source, destination, price in flights:
                if prevDistances[source] != float('inf') and \
                prevDistances[source] + price < distances[destination]:
                    distances[destination] = prevDistances[source] + price
        if distances[dst] == float('inf'):
            return -1
        return distances[dst]