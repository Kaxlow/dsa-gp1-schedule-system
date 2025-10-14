
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from searching import linear_search, binary_search


def make_events_unsorted():
    
    return [
        {"id": 1, "title": "Meeting A", "date": "2024-01-01", "time": "10:00", "end": "11:00"},
        {"id": 3, "title": "Meeting B",     "date": "2024-01-01", "time": "12:00", "end": "13:00"},
        {"id": 5, "title": "Meeting c",     "date": "2024-01-01", "time": "14:00", "end": "16:00"},
        {"id": 7, "title": "Meeting D",      "date": "2024-01-02", "time": "09:00", "end": "10:30"},
        {"id": 9, "title": "Meeting E",    "date": "2024-01-02", "time": "15:00", "end": "16:30"},
    ]


def make_events_sorted_by_id():
   
    return [
        {"id": 1, "title": "Meeting A", "date": "2024-01-01", "time": "10:00", "end": "11:00"},
        {"id": 3, "title": "Meetig B",     "date": "2024-01-01", "time": "12:00", "end": "13:00"},
        {"id": 5, "title": "Meeting C",     "date": "2024-01-01", "time": "14:00", "end": "16:00"},
        {"id": 7, "title": "Meeting D",      "date": "2024-01-02", "time": "09:00", "end": "10:30"},
        {"id": 9, "title": "Meetig E",    "date": "2024-01-02", "time": "15:00", "end": "16:30"},
    ]




def test_linear_search_found_middle():
    events = make_events_unsorted()
    assert linear_search(events, 5) == 2   # id=5 at index 2

def test_linear_search_first_last_and_miss():
    events = make_events_unsorted()
    assert linear_search(events, 1) == 0   # first element
    assert linear_search(events, 9) == 4   # last element
    assert linear_search(events, 42) == -1 # not found



def test_binary_search_found_indices():
    events = make_events_sorted_by_id()
    assert binary_search(events, 1) == 0
    assert binary_search(events, 5) == 2
    assert binary_search(events, 9) == 4

def test_binary_search_not_found():
    events = make_events_sorted_by_id()
    assert binary_search(events, 4) == -1
    assert binary_search(events, -10) == -1
    assert binary_search(events, 100) == -1
