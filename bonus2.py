from queue import PriorityQueue

def schedule_houses(houses, n):
    # sort the houses by earliest start time, breaking ties with earliest finish time
    sorted_houses = sorted(houses, key=lambda h: (h[0], h[1]))
    # create a priority queue that prioritizes finish time
    pq = PriorityQueue()
    i = 0
    for day in range(1, n+1):
        # add unpainted houses available on or before the current day to the priority queue
        while i < len(sorted_houses) and sorted_houses[i][0] <= day:
            pq.put((sorted_houses[i][1], sorted_houses[i][2]))
            i += 1
        # select the earliest finishing house among the available unpainted houses for the current day
        if not pq.empty():
            finish_time, house_id = pq.get()
            print(f"Schedule house {house_id+1} on day {day}")
        # remove painted houses from the priority queue
        while not pq.empty() and pq.queue[0][0] <= day:
            pq.get()


if __name__ == '__main__':
    n, m = map(int, input().split())
    houses = []
    for i in range(m):
        start, end = map(int, input().split())
        houses.append((start, end, i))
    schedule_houses(houses, n)
