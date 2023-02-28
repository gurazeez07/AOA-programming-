from queue import PriorityQueue

n, m = 0, 0

def schedule_houses(houses):
    # sort the houses by earliest start time, breaking ties with earliest finish time
    sorted_houses = sorted(houses, key=lambda h: (h[0], h[1]))
    # create a priority queue that prioritizes finish time if the day is 0
    pq = PriorityQueue()
    day = 1
    for house in sorted_houses:
        if house[0] >= day:
            # if the house is available on or after the current day, add it to the priority queue
            pq.put((house[1], house))
        if not pq.empty():
            # if there are available houses, print the one with the earliest finish time
            earliest_finish_time, earliest_finish_house = pq.get()
            print(f"Schedule house {earliest_finish_house['id']} on day {day}")
            day += 1
            if earliest_finish_house[1] > earliest_finish_time:
                # if the house is not available for the full duration, add it back to the priority queue
                pq.put((earliest_finish_house[1], earliest_finish_house))


if __name__ == '__main__':
    n, m = map(int, input().split())
    houses = []
    for i in range(m):
        start, end = map(int, input().split())
        houses.append((start, end, i))
    schedule_houses(houses)
