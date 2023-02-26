import heapq

n, m = map(int, input().split())
houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))  # add index to tuple for later sorting

houses.sort()  # sort by start day and then end day

painted = []  # list of painted house indices
available = []  # heap of available unpainted houses sorted by end day

for day in range(1, n+1):
    while houses and houses[0][0] == day:
        _, end, index = houses.pop(0)
        heapq.heappush(available, (end, index))

    if available:
        end, index = heapq.heappop(available)
        painted.append(index)

print('\n'.join(map(str, painted)))

