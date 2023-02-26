
import heapq

n, m = map(int, input().split())
houses = []
for i in range(m):
    start_day, end_day = map(int, input().split())
    houses.append((start_day, end_day, i+1))

houses.sort()

painted = 0
current_day = 1
available_houses = []
for i in range(m):
    start_day, end_day, house_idx = houses[i]
    if start_day > current_day:
        current_day = start_day
        while available_houses and available_houses[0][0] < current_day:
            heapq.heappop(available_houses)
    if current_day <= end_day:
        heapq.heappush(available_houses, (end_day, house_idx))
    if available_houses:
        _, painted_house_idx = heapq.heappop(available_houses)
        painted += 1
        print(painted_house_idx)

print(painted)
