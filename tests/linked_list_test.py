# Import modules
import time
import pytest
import json

# Import LinkedList class
from py_classes_ken import linked_list, utils

# Create an instance of LinkedList
ll = linked_list.LinkedList()

# Insert random events which are not necessarily in any order
with open("tests/test_events.json") as f:
  new_events = json.load(f)
for event in new_events:
  ll.insert(event)

# Pytest on operations

# List-all operation

# Expected to return first 5 events from random_events.json
def test_list_all():
  assert ll.list_all() == "Event ID: 3\nTitle: Synchronized demand-driven framework\nDate: 2025-10-30\nStart Time: 07:00\nEnd Time: 09:00\nLocation: Library C220\n\nEvent ID: 4\nTitle: Triple-buffered interactive contingency\nDate: 2025-10-30\nStart Time: 14:30\nEnd Time: 16:00\nLocation: Library C220\n\nEvent ID: 1\nTitle: Decentralized actuating software\nDate: 2025-10-29\nStart Time: 08:15\nEnd Time: 09:30\nLocation: Library C250\n\nEvent ID: 2\nTitle: Cross-platform clear-thinking structure\nDate: 2025-10-25\nStart Time: 17:00\nEnd Time: 19:00\nLocation: Student Center M101\n\nEvent ID: 5\nTitle: User-centric global access\nDate: 2025-10-24\nStart Time: 12:00\nEnd Time: 16:00\nLocation: Administration Block A101\n\nEvent ID: 6\nTitle: Managing a cross-functional team\nDate: 2025-10-27\nStart Time: 09:00\nEnd Time: 12:00\nLocation: East Wing D300\n\n"

  # Create new instance of empty Linked List
  ll_empty = linked_list.LinkedList()
  # When calling list_all on empty linked list, it should return error: There are no events
  assert ll_empty.list_all() == "There are no events."

# Sort operations

# Test with insertion, merge, and quick sorts, sort by date-time
# Among the events used in the test, the event with the earliest date is 2025-10-24.
@pytest.mark.parametrize("sort_type, expected", [
  ("insertion", "2025-10-24"),
  ("merge", "2025-10-24"),
  ("quick", "2025-10-24"),
]
)
def test_sort_by_datetime(sort_type, expected):
  assert ll.sort(sort_type, sort_by = "date-time")._head._value["date"] == expected

# Test with insertion, merge, and quick sorts, sort by id
@pytest.mark.parametrize("sort_type, expected", [
  ("insertion", 1),
  ("merge", 1),
  ("quick", 1)
]
)
def test_sort_by_id(sort_type, expected):
  assert ll.sort(sort_type, sort_by = "id")._head._value["id"] == expected

# Test with invalid sort_type argument
@pytest.mark.parametrize("sort_type, sort_by, expected", [
  ("bubble", "date-time", "Error: sort_type must be \"insertion\", \"merge\", or \"quick\"."),
  ("bubble", "id", "Error: sort_type must be \"insertion\", \"merge\", or \"quick\".")
])
def test_sort_invalid(sort_type, sort_by, expected):
  assert ll.sort(sort_type, sort_by) == expected

# Search operations

# Run two tests each for linear search and binary search
# Test 1: Search for event ID 1 which exists, expected to return the event
# Test 2: Search for event ID 8 which does not exist, expected to return None
@pytest.mark.parametrize("id, expected", [
  (1, {
    "id": 1,
    "title": "Decentralized actuating software",
    "date": "2025-10-29",
    "time_start": "08:15",
    "time_end": "09:30",
    "location": "Library C250"
    }
    ),
  (8, 
   None
   )
  ]
)
class TestSearchById:
  # Linear search by event ID
  def test_linear_search(self, id, expected):
    assert ll.linear_search(id) == expected

  # Binary search by event ID
  def test_binary_search(self, id, expected):
    # First sort the linked list by event ID
    assert ll.binary_search(id) == expected

# Conflict detection operation

# Create new events to test conflict detection
# event_1 should cause no conflict
event_1 = {
    "id": 7,
    "title": "An Introduction to Symbiosis",
    "date": "2025-10-29",
    "time_start": "10:00",
    "time_end": "12:00",
    "location": "East Wing 440"
  }

# event_2 should conflict with another event
event_2 = {
    "id": 8,
    "title": "Dissection of High-Speed Wireless Networks",
    "date": "2025-10-30",
    "time_start": "15:00",
    "time_end": "17:00",
    "location": "Library C220"
  }

def test_conflict_detect():
  assert ll.conflict_detect(event_1) == False
  assert ll.conflict_detect(event_2) == True

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
  (event_1, f"Event ID 7: \"An Introduction to Symbiosis\" has been inserted into the linked list."),
  (event_2, "Error: There is already another existing event scheduled for the same date, time, and location."),
  (event_3, "Error: Event ID already exists.")
]
)
def test_insert(new_event, expected):
  assert ll.insert(new_event) == expected

# Search-by-id operation

# Run two tests each for linear search and binary search
# Test 1: Search for event ID 3 which exists, expected to return the event's details
# Test 2: Search for event ID 7 which does not exist, expected to return error: Event ID not found
# Finally, test with an invalid search_method argument, which should return the error: search_method must be "linear" or "binary"
@pytest.mark.parametrize("event_id, search_method, expected", [
  (3, "linear", f"Event ID 3 pertains to:\nTitle: Synchronized demand-driven framework\nDate: 2025-10-30\nStart Time: 07:00\nEnd Time: 09:00\nLocation: Library C220"),
  (3, "binary", f"Event ID 3 pertains to:\nTitle: Synchronized demand-driven framework\nDate: 2025-10-30\nStart Time: 07:00\nEnd Time: 09:00\nLocation: Library C220"),
  (8, "linear", "Error: Event ID not found."),
  (8, "binary", "Error: Event ID not found."),
  (2, "colinear", "Error: search_method must be \"linear\" or \"binary\".")
]
)
def test_search_by_id(event_id, search_method, expected):
  assert ll.search_by_id(event_id, search_method) == expected

# Delete operation
# Test 1: Delete event ID 4 which exists, expected to delete successfully
# Test 2: Delete event ID 8 which does not exist, expected to return error
@pytest.mark.parametrize("event_id, expected", [
  (4, f"Event ID 4: \"Triple-buffered interactive contingency\" has been deleted from the linked list."),
  (8, "Error: Event ID 8 does not exist in the linked list.")
]
)

def test_delete(event_id, expected):
  assert ll.delete(event_id) == expected