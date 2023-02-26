import heapq

n, m = map(int, input().split())

houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

houses.sort()

painted = []
currentDay = 1
pq = []

for house in houses:
    start, end, index = house
    
    if start > currentDay:
        currentDay = start
        
    if currentDay <= end and currentDay >= start:
        heapq.heappush(pq, (end-start, index))
        
    if pq:
        duration, house_index = heapq.heappop(pq)
        painted.append(house_index)
        currentDay += 1

print(len(painted))
for index in painted:
    print(index, end=' ')
