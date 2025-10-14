# Import modules
from datetime import datetime, time
import pytest
import json

# Import DynamicArray class
from py_classes_ken import dynamic_array

# Creeate an instance of DynamicArray
da = dynamic_array.DynamicArray()

# Insert 5 events which are not necessarily in any order
with open("tests/random_events_5.json") as f:
  new_events = json.load(f)
for event in new_events:
  da.insert(event)

# Pytest on operations

# Sort operations

# Insertion sort by date and time
def test_insertion_sort():
  assert da.insertion_sort() == da._collection

# Insertion sort by id
def test_insertion_sort_id():
  assert da.insertion_sort(sort_by = "id") == da._collection

# Merge sort by date and time
def test_merge_sort():
  assert da.merge_sort() == da._collection

# Merge sort by id
def test_merge_sort_id():
  assert da.merge_sort(sort_by = "id") == da._collection

# Quick sort by date and time
def test_quick_sort():
  assert da.quick_sort() == da._collection

# Quick sort by date and time
def test_quick_sort_id():
  assert da.quick_sort(sort_by = "id") == da._collection

# Search operations

# Run two tests each for linear search and binary search
# Test 1: Search for event ID 1 which exists, expected to return the event
# Test 2: Search for event ID 6 which does not exist, expected to return None
@pytest.mark.parametrize("id, expected", [
  (1, {
    "id": 1,
    "title": "Synchronized demand-driven framework",
    "date": "2025-10-30",
    "time_start": "07:00",
    "time_end": "09:00",
    "location": "Library C220"
  }),
  (6, 
   None
   )
  ]
)
class TestSearchById:
  # Linear search by event ID
  def test_linear_search(self, id, expected):
    assert da.linear_search(id) == expected

  # Binary search by event ID
  def test_binary_search(self, id, expected):
    # First sort the array by event ID
    assert da.binary_search(id) == expected

# Conflict detection operation

# Create new events to test conflict detection
# event_1 should cause no conflict
event_1 = {
    "id": 6,
    "title": "An Introduction to Symbiosis",
    "date": "2025-10-29",
    "time_start": "10:00",
    "time_end": "12:00",
    "location": "East Wing 440"
  }

# event_2 should conflict with another event
event_2 = {
    "id": 7,
    "title": "Dissection of High-Speed Wireless Networks",
    "date": "2025-10-30",
    "time_start": "15:00",
    "time_end": "17:00",
    "location": "Library C220"
  }

def test_conflict_detect():
  assert da.conflict_detect(event_1) == False
  assert da.conflict_detect(event_2) == True

# Insert operation

# Insert event_1 and event_2 from above
# event_1 should be inserted successfully
# event_2 should fail to insert due to conflict
# Create event_3 to test with insert
# event_3 should fail to insert due to duplicate id
event_3 = {
    "id": 5,
    "title": "Writing to Your Audience",
    "date": "2025-10-25",
    "time_start": "10:00",
    "time_end": "12:00",
    "location": "Library C250"
  }

@pytest.mark.parametrize("new_event, expected", [
  (event_1, f"Event ID 6: \"An Introduction to Symbiosis\" has been inserted into the array."),
  (event_2, "Error: There is already another existing event scheduled for the same date, time, and location."),
  (event_3, "Error: Event ID already exists.")
]
)
def test_insert(new_event, expected):
  assert da.insert(new_event) == expected

# Search-by-id operation

# Run two tests each for linear search and binary search
# Test 1: Search for event ID 3 which exists, expected to return the event's details
# Test 2: Search for event ID 7 which does not exist, expected to return error: Event ID not found
# Finally, test with an invalid search_method argument, which should return the error: search_method must be "linear" or "binary"
@pytest.mark.parametrize("event_id, search_method, expected", [
  (3, "linear", f"Event ID 3 pertains to:\nTitle: Decentralized actuating software\nDate: 2025-10-29\nStart Time: 08:15\nEnd Time: 09:30\nLocation: Library C250"),
  (3, "binary", f"Event ID 3 pertains to:\nTitle: Decentralized actuating software\nDate: 2025-10-29\nStart Time: 08:15\nEnd Time: 09:30\nLocation: Library C250"),
  (7, "linear", "Error: Event ID not found."),
  (7, "binary", "Error: Event ID not found."),
  (2, "colinear", "Error: search_method must be \"linear\" or \"binary\".")
]
)
def test_search_by_id(event_id, search_method, expected):
  assert da.search_by_id(event_id, search_method) == expected

# List-all operation
# Expected to return all 5 events in the array
def test_list_all():
  assert da.list_all() == "Event ID: 1\nTitle: Synchronized demand-driven framework\nDate: 2025-10-30\nStart Time: 07:00\nEnd Time: 09:00\nLocation: Library C220\n\nEvent ID: 4\nTitle: Triple-buffered interactive contingency\nDate: 2025-10-30\nStart Time: 14:30\nEnd Time: 16:00\nLocation: Library C220\n\nEvent ID: 3\nTitle: Decentralized actuating software\nDate: 2025-10-29\nStart Time: 08:15\nEnd Time: 09:30\nLocation: Library C250\n\nEvent ID: 2\nTitle: Cross-platform clear-thinking structure\nDate: 2025-10-25\nStart Time: 17:00\nEnd Time: 19:00\nLocation: Student Center M101\n\nEvent ID: 5\nTitle: User-centric global access\nDate: 2025-10-24\nStart Time: 12:00\nEnd Time: 16:00\nLocation: Administration Block A101\n\n"

  # Create new instance of empty Dynamic Array
  da_empty = dynamic_array.DynamicArray()
  # When calling list_all on empty array, it should return error: There are no events
  assert da_empty.list_all() == "There are no events."

# Delete operation
# Test 1: Delete event ID 4 which exists, expected to delete successfully
# Test 2: Delete event ID 7 which does not exist, expected to return error
@pytest.mark.parametrize("event_id, expected", [
  (4, f"Event ID 4: \"Triple-buffered interactive contingency\" has been deleted from the array."),
  (7, "Error: Event ID 7 does not exist in array.")
]
)
def test_delete(event_id, expected):
  assert da.delete(event_id) == expected  
