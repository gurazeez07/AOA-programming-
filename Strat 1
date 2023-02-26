import sys

# Read input from standard input
n, m = map(int, input().split())
houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

# Sort houses by start day and end day
houses.sort()

# Initialize variables
painted = []
currentDay = 1

# Iterate over houses
for house in houses:
    start, end, i = house
    # If we need to wait for the next available day to paint the house
    if start > currentDay:
        currentDay = start
    # If we can paint the house on the current day
    if currentDay <= end:
        painted.append(i)
        currentDay += 1

# Output the indices of painted houses
for i in painted:
    print(i, end=' ')
print()
