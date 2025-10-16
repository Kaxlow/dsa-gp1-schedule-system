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

# Function to measure search runtime in different scenarios and get results in array
def get_search_runtime():
  # Store results as an array with 5 columns for data_structure, search_algorithm, sorted_or_unsorted, num_events, runtime
  search_results = []

  # Search system with n events for the same random id using linear and binary search
  for n in (50, 500, 2500):
    events = create_random_events(n)
    # Create new instance of DynamicArray
    da = dynamic_array.DynamicArray()
    # Create new instance of LinkedList
    ll = linked_list.LinkedList()
    for event in events: 
      da.insert(event)
      ll.insert(event)

    # Random id to search for
    search_id = random.randint(1, n)

    # Sorted DynamicArray and LinkedList, in terms of id

    # Linear search on DynamicArray
    runtime_start = time.time()
    da.linear_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["dynamic array", "linear search", "sorted", n, runtime])

    # Binary search on Dynamic Array
    runtime_start = time.time()
    da.binary_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["dynamic array", "binary search", "sorted", n, runtime])

    # Linear search on LinkedList
    runtime_start = time.time()
    ll.linear_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["linked list", "linear search", "sorted", n, runtime])

    # Binary search on LinkedList
    runtime_start = time.time()
    ll.binary_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["linked list", "binary search", "sorted", n, runtime])

    # Unsorted DynamicArray and LinkedList, in terms of id

    # Create unsorted DynamicArray and LinkedList by running merge sort by date-time, breaking the order of id
    da.sort(sort_type = "merge")
    ll.sort(sort_type = "merge")

    # Linear search on DynamicArray
    runtime_start = time.time()
    da.linear_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["dynamic array", "linear search", "unsorted", n, runtime])

    # Binary search on Dynamic Array
    runtime_start = time.time()
    da.binary_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["dynamic array", "binary search", "unsorted", n, runtime])

    # Linear search on LinkedList
    runtime_start = time.time()
    ll.linear_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["linked list", "linear search", "unsorted", n, runtime])

    # Binary search on LinkedList
    runtime_start = time.time()
    ll.binary_search(search_id)
    runtime = time.time() - runtime_start
    search_results.append(["linked list", "binary search", "unsorted", n, runtime])

  return search_results

get_search_runtime()