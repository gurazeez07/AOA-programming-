import heapq

def strat4(n, m, houses):
    pq = []  # priority queue to store unpainted houses available on a day
    painted = [0] * m  # array to store painted houses
    output = []  # list of house indices to paint
    
    for i in range(1, n+1):
        # Add all the unpainted houses that are available on the current day to the priority queue.
        while houses and houses[0][0] <= i:
            start, end, index = houses.pop(0)
            if not painted[index]:
                heapq.heappush(pq, (end, index))  # push the unpainted house into the priority queue
        
        # Paint the house that will stop being available the earliest among the unpainted houses available on the current day.
        if pq:
            end, index = heapq.heappop(pq)
            painted[index] = 1
            output.append(index)
    
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
