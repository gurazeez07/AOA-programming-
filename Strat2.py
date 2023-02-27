from queue import PriorityQueue

n, m = map(int, input().split())

houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

houses.sort()

currentDay = 0
pq = PriorityQueue()

# Iterate over days
for day in range(1, n+1):
    # Add all the unpainted houses that are available on the current day to the priority queue.
    while houses and houses[0][0] == day:
        start, end, index = houses.pop(0)
        pq.put((-start, end, index))

    # Paint the house that became available the latest among the unpainted houses available on the current day.
    if not pq.empty():
        start, end, index = pq.get()
        if end < day:
            continue
        print(index)
        # currentDay += 1
