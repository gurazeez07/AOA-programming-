from queue import PriorityQueue
import sys

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())

houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

houses.sort(key=lambda x: x[0], reverse=True)

painted = 0
currentDay = 1
index = 0
# addedOne = False

while (currentDay < n) & (len(houses) > 0):
    if index >= len(houses):
        currentDay += 1
        index = 0

    house = houses[index]
    start, end, i = house

    # increment if not at right start yet
    if start > currentDay:
        index += 1
        continue
    if end < currentDay:
        houses.remove(house)
        continue
        # currentDay = start

    # if can paint the house today
    if currentDay <= end and currentDay >= start:
        print(house[2])
        houses.remove(house)
        index = 0
        currentDay += 1
        continue
    else:
        index += 1
        currentDay += 1
    # if index == len(houses):
    #     break
    
