import sys
# import time

# start timer
# start = time.time()
paintedHouses = 0

# Get input from file // command line??
n, m = map(int, input().split())
houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

# Sort houses by earliest start date
houses.sort()

painted = []
currentDay = 1

# Iterate over houses
for house in houses:
    start, end, i = house
    # If we need to wait for the next free day to paint
    if start > currentDay:
        currentDay = start
    # If can paint the house today
    if currentDay <= end:
        print(i, end=' ')
        currentDay += 1

# Print time taken

# Output the indices of painted houses
# for i in painted:
#     print(i, end=' ')
# print()
