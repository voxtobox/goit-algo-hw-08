import heapq

def connect_raw(list):
    total = 0
    
    while len(list) > 1:
        one = list.pop()
        two = list.pop()
        sum = one + two
        total += sum
        list.append(sum)
    
    return total

def connect_sorted(list):
    total = 0
    list.sort(reverse=True)
    
    while len(list) > 1:
        one = list.pop()
        two = list.pop()
        sum = one + two
        total += sum
        list.append(sum)
    
    return total

def connect(list):
    heapq.heapify(list)
    total = 0
    while len(list) > 1:
        one = heapq.heappop(list)
        two = heapq.heappop(list)
        sum = one + two
        total += sum
        heapq.heappush(list, sum)
    
    return total

cabbles = [4, 10, 3, 17, 5, 1, 12, 20]

print('raw: ', connect_raw(cabbles.copy()))
print('sorted: ', connect_sorted(cabbles.copy()))
print('heap: ', connect(cabbles.copy()))