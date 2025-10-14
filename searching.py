
## Linear_Search
def linear_search(events, target_id):
   
    for i, evnts in enumerate(events):
        if evnts["id"] == target_id:
            return i
    return -1

#Binary Search
def binary_search(event_sorted, target_id):
    
    low, high = 0, len(event_sorted) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = event_sorted[mid]["id"]
        if mid_id == target_id:
            return mid
        if mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


