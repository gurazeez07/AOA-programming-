import heapq

# Paint earliest ending house first
def strat4(n, m, houses):
    pq = []  # priority queue to store unpainted houses available on a day
    painted = [0] * m  # array to store painted houses
    output = []  # list of house indices to paint
    
    houses.sort(key=lambda x: (x[0], -x[1]))  # sort by start day and then reverse end day (so that the earliest end day is first in stack)

    for i in range(1, n+1):
        # Add all the unpainted houses that are available on the current day to the priority queue.
        while houses and houses[0][0] <= i:
            start, end, index = houses.pop(0)
            if not painted[index]:
                # push end first so it sorts by end date    
                heapq.heappush(pq, (end, start, index))  # push the unpainted house into the priority queue
        
        # Paint the house that will stop being available the earliest among the unpainted houses available on the current day.
        while not len(pq) == 0:
            end, start, index = heapq.heappop(pq)
            if end < i:
                continue
            print(index + 1, end=' ')
            break
    
    # Print the output list of house indices.
    for index in output:
        print(index+1, end=' ')  # house indices are 1-based
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    houses = []
    for i in range(m):
        start, end = map(int, input().split())
        houses.append((start, end, i))
    strat4(n, m, houses)
