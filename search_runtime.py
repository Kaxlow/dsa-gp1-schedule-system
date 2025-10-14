import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import time
import random
from searching import linear_search, binary_search


def merge_sort_by_id(events):
    if len(events) <= 1:
        return events

    mid = len(events) // 2
    left = merge_sort_by_id(events[:mid])
    right = merge_sort_by_id(events[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["id"] <= right[j]["id"]:
            merged += [left[i]]  
            i += 1
        else:
            merged += [right[j]]
            j += 1
    while i < len(left):
        merged += [left[i]]
        i += 1
    while j < len(right):
        merged += [right[j]]
        j += 1
    return merged


def generate_events(n):
    return [{"id": i} for i in range(n)]


sizes = [100, 1000, 5000, 50000]

for n in sizes:
    events = generate_events(n)
    random.shuffle(events)  # keep this; not restricted

 
    sorted_events = merge_sort_by_id(events)
    target_id = random.randint(0, n - 1)

    repeats = 100  # average over many runs

    start = time.perf_counter()
    for _ in range(repeats):
        linear_search(events, target_id)
    linear_time = (time.perf_counter() - start) / repeats


    start = time.perf_counter()
    for _ in range(repeats):
        binary_search(sorted_events, target_id)
    binary_time = (time.perf_counter() - start) / repeats

    print(f"n={n:6d} | Linear={linear_time*1000:.6f} ms | Binary={binary_time*1000:.6f} ms")

