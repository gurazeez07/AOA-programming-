import heapq

numpainted = 0

# Paint the shortest duration house first
n, m = map(int, input().split())
houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))  # add index to tuple for later sorting

# O(m log m)
houses.sort(key=lambda x: (x[0], -x[1])) # sort by start day and then reverse end day (so that the earliest end day is first in stack)

painted = []  # list of painted house indices
available = []  # heap of available unpainted houses sorted by end day

# Iterate over days, O(n)
for day in range(1, n+1):
    while houses and houses[0][0] == day:
        start, end, index = houses.pop(0)
        heapq.heappush(available, (end - start, end, index))

    while len(available) > 0:
        numpainted += 1
        duration, end, index = heapq.heappop(available)
        if end < day:
            continue
        painted.append(index)
        break

print(' '.join(map(str, painted)))

