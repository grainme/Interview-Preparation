import heapq


pq = []

heapq.heappush(pq, (3, "task3"))
heapq.heappush(pq, (2, "task2"))
heapq.heappush(pq, (1, "task1"))

while pq:
    ele = heapq.heappop(pq)
    print(ele)
