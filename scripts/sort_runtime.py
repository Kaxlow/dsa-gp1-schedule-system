# Import libraries
import numpy as np
from datetime import datetime, timedelta
import time
import random
from py_classes_ken import dynamic_array, linked_list

# Function for generating random date from 2025-10-15 to 2026-06-30
def date_random():
  date_random = (
      datetime(year = 2025, month = 10, day = 15) +
      timedelta(days = random.randint(0, (datetime(year = 2026, month = 6, day = 30) -
                                                   datetime(year = 2025, month = 10, day = 15)
                                                   ).days
                                               )))
  return date_random.strftime("%Y-%m-%d")

# Function for generating random time in HH:mm format
def time_start_random():
  HH = random.randint(0, 20)
  mm = random.randint(0, 59)
  time_start = f"{HH:02d}:{mm:02d}"
  # time_end is anywhere from 1 to 3 hours after time_start
  time_end = f"{(HH + random.randint(1, 3)):02d}:{mm:02d}"
  return time_start, time_end

# Function for generating random location from list of 20 distinct locations
def location_random():
  locations = ["ECCE 100", "ECCE 200", "ECCE 300", "ECCE 400", "ECCE 500", "LM 100", "LM 200", "LM 300", "LM 400", "LM 500", "AB 100", "AB 200", "AB 300", "AB 400", "AB 500", "FF 100", "FF 200", "FF 300", "FF 400", "FF 500"]
  return random.choice(locations)

# Generate n random events
def create_random_events(n):
  events = []
  for i in range(n):
    events.append({
        "id": i + 1,
        "title": "Event " + str(i + 1) + " Title.",
        "date": date_random(),
        "time_start": time_start_random()[0],
        "time_end": time_start_random()[1],
        "location": location_random()
    })
  return events

# Function to measure sort runtime in different scenarios and get results in array
def get_sort_runtime():
  # Store results as an array with 4 columns for data_structure, sort_algorithm, num_events, runtime
  sort_results = []

  # Sort n random events by date-time. For each n, measure runtime in seconds for insertion sort, merge sort, and quick sort
  # Skip n = 5000 and n = 50000 as it is too large for computer to complete running
  for n in (50, 500, 2500):
    events = create_random_events(n)
    # Create new instance of DynamicArray
    da = dynamic_array.DynamicArray()
    # Create new instance of LinkedList
    ll = linked_list.LinkedList()
    for event in events: 
      da.insert(event)
      ll.insert(event)

    # Insertion sort on dynamic array
    da_insertion_sort = da
    runtime_start = time.time()
    da_insertion_sort.sort(sort_type = "insertion")
    runtime = time.time() - runtime_start
    sort_results.append(["dynamic array", "insertion sort", n, runtime])

    # Insertion sort on linked list
    ll_insertion_sort = ll
    runtime_start = time.time()
    ll_insertion_sort.sort(sort_type = "insertion")
    runtime = time.time() - runtime_start
    sort_results.append(["linked list", "insertion sort", n, runtime])

    # Merge sort on dynamic array
    da_merge_sort = da
    runtime_start = time.time()
    da_merge_sort.sort(sort_type = "merge")
    runtime = time.time() - runtime_start
    sort_results.append(["dynamic array", "merge sort", n, runtime])

    # Merge sort on linked list
    ll_merge_sort = ll
    runtime_start = time.time()
    ll_merge_sort.sort(sort_type = "merge")
    runtime = time.time() - runtime_start
    sort_results.append(["linked list", "merge sort", n, runtime])

    # Quick sort on dynamic array
    da_quick_sort = da
    runtime_start = time.time()
    da_quick_sort.sort(sort_type = "quick")
    runtime = time.time() - runtime_start
    sort_results.append(["dynamic array", "quick sort", n, runtime])

    # Quick sort on linked list
    ll_quick_sort = ll
    runtime_start = time.time()
    ll_quick_sort.sort(sort_type = "quick")
    runtime = time.time() - runtime_start
    sort_results.append(["linked list", "quick sort", n, runtime])

  return sort_results

get_sort_runtime()