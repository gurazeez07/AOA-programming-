n, m = map(int, input().split())

# paint houses that become available the latest first
houses = []
for i in range(m):
    start, end = map(int, input().split())
    houses.append((start, end, i+1))

# O(m log m)
houses.sort(key=lambda x: (x[0], -x[1])) # sort by start day and then reverse end day (so that the earliest end day is first in stack)

currentDay = 0
stack = []


# Iterate over days, O(n)
for day in range(1, n+1):
    # Add all the unpainted houses that are available on the current day to the priority queue.
    while houses and houses[0][0] == day:
        start, end, index = houses.pop(0)
        stack.append((start, end, index))

    # Paint the house that became available the latest among the unpainted houses available on the current day.
    while not len(stack) == 0:
        start, end, index = stack.pop()
        if end < day:
            continue
        print(index)
        break
        # currentDay += 1
