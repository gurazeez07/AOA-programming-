from queue import PriorityQueue
import sys

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())

houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

houses.sort()

painted = 0
currentDay = 1
pq = PriorityQueue()

for house in houses:
    start, end, index = house
    if start > currentDay:
        currentDay = start
        while not pq.empty() and pq.queue[0][0] < currentDay:
            pq.get()
    if currentDay <= end and currentDay >= start:
        pq.put((-end, index))
    if not pq.empty():
        _, index = pq.get()
        painted += 1
        currentDay += 1
        print(index)