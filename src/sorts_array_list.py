# src/sorts_array_list.py

def event_key(event):
    y, mo, d = map(int, event["date"].split("-"))
    hh, mm = map(int, event["time"].split(":"))
    return (y, mo, d, hh, mm)

#Insertion Sort
def insertion_sort_array(arr):
    for i in range(1, len(arr)):
        key_event = arr[i]
        key_val = event_key(key_event)

        j = i - 1
        while j >= 0 and event_key(arr[j]) > key_val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_event
    return arr

#Merge Sort
def merge_arrays(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if event_key(left[i]) <= event_key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort_array(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_array(arr[:mid])
    right = merge_sort_array(arr[mid:])

    return merge_arrays(left, right) 

#Quick Sort
import random

def quick_sort_array(arr):
    if len(arr) <= 1:
        return arr[:]
    
    pivot = event_key(random.choice(arr))

    less = []
    equal = []
    greater = []

    for event in arr:
        key_val = event_key(event)
        if key_val < pivot:
            less.append(event)
        elif key_val == pivot:
            equal.append(event)
        else:
            greater.append(event)

    return quick_sort_array(less) + equal + quick_sort_array(greater)

