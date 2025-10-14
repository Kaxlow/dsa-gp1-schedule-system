import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from conflict import detect_conflicts


def test_no_conflict(): ## Two events occur back to back on same date so no conflict, no overlap
    events = [
        {"id": 1, "title": "Meeting", "date": "2024-01-01", "time": "09:00", "end": "10:00"},
        {"id": 2, "title": "Lunch",   "date": "2024-01-01", "time": "10:00", "end": "11:00"},
    ]
    assert detect_conflicts(events) == []


def test_one_conflict(): ## one conflict the end time of event 1 is more than start time of event 2
    events = [
        {"id": 1, "title": "Meeting", "date": "2024-01-01", "time": "09:00", "end": "10:30"},
        {"id": 2, "title": "Call",    "date": "2024-01-01", "time": "10:00", "end": "11:00"},
    ]
    assert detect_conflicts(events) == [(1, 2)] ## event 1 and 2 overlap in time and it retuns the list


def test_multiple_conflicts():
    events = [
        {"id": 1, "title": "Meeting", "date": "2024-01-02", "time": "09:00", "end": "10:30"},
        {"id": 2, "title": "Workshop","date": "2024-01-02", "time": "10:00", "end": "11:30"},
        {"id": 3, "title": "Review",  "date": "2024-01-02", "time": "11:00", "end": "12:00"},
    ]
    assert detect_conflicts(events) == [(1, 2), (2, 3)]
